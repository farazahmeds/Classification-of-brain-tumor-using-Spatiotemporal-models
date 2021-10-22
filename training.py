import torch
import torch.nn as nn
import torch.optim as optim
from torch import utils
from torch.utils.data import dataset
from torch.utils.data import DataLoader
import torch.nn.functional as F
from torch.autograd import Variable
from torch.optim import lr_scheduler
import torch.multiprocessing
import torchvision
from torchvision import datasets, models, transforms

from dataset.datasets import Datasets

import hydra
from omegaconf import DictConfig, OmegaConf

import torchio
from torchio.transforms import (
    CropOrPad
    OneOf
    RescaleIntensity,
    RandomAffine,
    RandomElasticDeformation,
    RandomFlip
    Compose,
)

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom
from livelossplot import PlotLosses

import os
import numpy as np
from torchvision.transforms import transforms
from torch.utils.tensorboard import SummaryWriter
from apex import amp

from dataset import brats

from sklearn.metrics import confusion_matrix
from plotcm import plot_confusion_matrix


load_model = config.load_model

cwd = os.getcwd()

path_to_volumes = Path(cwd, 'dataset')

config = OmegaConf.load(Path(cwd, 'configs/config.yaml'))

volumes = Datasets(path_to_volumes)

total_Samples=volumes.return_total_samples()

torch.manual_seed(config.global_seed)

class_weights = torch.FloatTensor([3.54,1,1]).cuda()

#Transforms
rescale = RescaleIntensity((0.05, 99.5))
randaffine = torchio.RandomAffine(scales=(0.9,1.2),degrees=10, isotropic=True, image_interpolation='nearest')
flip = torchio.RandomFlip(axes=('LR'), p=0.5)
croporpad = CropOrPad(target_shape=(240, 240, 155))
transforms = [rescale, flip, randaffine]

transform = Compose(transforms)

# ImagesDataset is a subclass of torch.data.utils.Dataset
subjects_dataset = torchio.SubjectsDataset(total_Samples, transform=transform)

trainset, testset = torch.utils.data.random_split(subjects_dataset, [confg.dataset.train_samples, config.dataset.test_samples], generator=torch.Generator().manual_seed(confg.dataset.train_test_split_seed))

trainloader = DataLoader(dataset=trainset,  batch_size=1, shuffle=True)
testloader = DataLoader(dataset=testset,   batch_size=1, shuffle=True)

# class R2Plus1dStem4MRI(nn.Sequential):
#     """R(2+1)D stem is different than the default one as it uses separated 3D convolution
#     """
#
#     def __init__(self):
#         super(R2Plus1dStem4MRI, self).__init__(
#             nn.Conv3d(1, 45, kernel_size=(1, 7, 7),
#                       stride=(1, 2, 2), padding=(0, 3, 3),
#                       bias=False),
#             nn.BatchNorm3d(45),
#             nn.ReLU(inplace=True),
#
#             nn.Conv3d(45, 64, kernel_size=(3, 1, 1),
#                       stride=(1, 1, 1), padding=(1, 0, 0),
#                       bias=False),
#             nn.BatchNorm3d(64),
#             nn.ReLU(inplace=True))

class modifybasicstem(nn.Sequential):
    """The default conv-batchnorm-relu stem
    """
    def __init__(self):
        super(modifybasicstem, self).__init__(
            nn.Conv3d(1, 64, kernel_size=(3, 7, 7), stride=(1, 2, 2),
                      padding=(1, 3, 3), bias=False),
            nn.BatchNorm3d(64),
            nn.ReLU(inplace=True))

model = torchvision.models.video.mc3_18(pretrained=True)

# model.stem =  R2Plus1dStem4MRI()
model.stem = modifybasicstem() # change the stem based on the  model 


# regularization

model.fc = nn.Sequential(
    nn.Dropout(0.3),
    nn.Linear(model.fc.in_features, config.training.num_classes)
)

liveloss = PlotLosses()

model.to('cuda:0')

criterion = nn.CrossEntropyLoss(weight=class_weights)

optimizer = torch.optim.Adam(model.parameters(), lr=config.training.learning_rate, weight_decay=config.training.weight_decay)

# Initialize the prediction and label lists(tensors) for confusion matrix
predlist = torch.zeros(0, dtype=torch.long).to('cuda:0')
lbllist = torch.zeros(0, dtype=torch.long).to('cuda:0')

model, optimizer = amp.initialize(model, optimizer, opt_level=config.model.opt_level)

tb = SummaryWriter(Path(cwd, 'runs'))


def save_checkpoint(state,filename=Path(cwd,'output/{}'.format('foo.pth.tar')):
    torch.save(state,filename)


if load_model:
    from resume_from_checkpoint import resume_from_checkpoint
    fpath = Path(cwd,'output/{}'.format('foo.pth.tar')
    start_epoch = resume_from_checkpoint(fpath, model, optimizer)


for epoch in range(config.training.num_epoch):

    logs = {}
    total_correct = 0
    total_loss = 0
    total_images = 0
    total_val_loss = 0

    if epoch % 5 == 0:
        checkpoint = {'epoch': epoch+1, 'state_dict': model.state_dict(), 'optimizer': optimizer.state_dict()}
        print("Load True: saving checkpoint")
        save_checkpoint(checkpoint)

        # else:
        #     checkpoint = {'epoch': epoch + 1, 'state_dict': model.state_dict(),
        #                   'optimizer': optimizer.state_dict()}
        #     print("Loade False: saving checkpoint")
        #     save_checkpoint(checkpoint)

    for i, traindata in enumerate(trainloader):
        images = F.interpolate(traindata['t1'][torchio.DATA], scale_factor=(config.dataset.img_scale_factor,config.dataset.img_scale_factor,config.dataset.img_scale_factor)).to('cuda:0')
        labels = traindata['t1']['mylabel'].to('cuda:0')

        optimizer.zero_grad()

        # Forward propagation
        outputs = model(images)


        # Calculating loss with softmax to obtain cross entropy loss

        # loss = criterion(outputs, labels)

        loss = criterion(outputs, labels)  # ....>

        # Backward prop
        # loss.backward()
        with amp.scale_loss(loss, optimizer) as scaled_loss:
            scaled_loss.backward()

        # Updating gradients
        optimizer.step()
        # scheduler.step()

        # Total number of labels
        total_images += labels.size(0)

        # Obtaining predictions from max value
        _, predicted = torch.max(outputs.data, 1)

        # Calculate the number of correct answers
        correct = (predicted == labels).sum().item()

        total_correct += correct
        total_loss += loss.item()

        running_trainacc = ((total_correct / total_images) * 100)

        logs['log loss'] = total_loss / total_images
        logs['Accuracy'] = ((total_correct / total_images) * 100)
    tb.add_scalar('Training loss', loss, global_step=epoch)
    tb.add_scalar('Training accuracy', running_trainacc, global_step=epoch)

    print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'
          .format(epoch + 1, config.tranining.num_epoch, i + 1, len(trainloader), (total_loss / total_images),
                  (total_correct / total_images) * 100))
                 

    # Testing the model

    with torch.no_grad():
        correct = 0
        total = 0

        for testdata in testloader:
            # print ("for testdata in testloader, len of testdata",len(testdata))
            images = F.interpolate(testdata['t1'][torchio.DATA], scale_factor=(config.dataset.img_scale_factor,config.dataset.img_scale_factor,config.dataset.img_scale_factor)).to('cuda:0')

            labels = testdata['t1']['mylabel'].to('cuda:0')
            outputs = model(images)

            _, predicted = torch.max(outputs.data, 1)

            predlist = torch.cat([predlist, predicted.view(-1)])  # Append batch prediction results

            lbllist = torch.cat([lbllist, labels.view(-1)])

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            total_losss = loss.item()

            accuracy = correct / total

        print('Test Accuracy of the model: {} %'.format(100 * correct / total))

        logs['val_' + 'log loss'] = total_loss / total
        validationloss = total_loss / total

        validationacc = ((correct / total) * 100)
        logs['val_' + 'Accuracy'] = ((correct / total) * 100)

    tb.add_scalar('Validation loss', validationloss, global_step=epoch)

    tb.add_scalar('Validation accuracy', validationacc, global_step=epoch)

    # logs['accuracy'] = accuracy
    liveloss.update(logs)
    # start_epoch+=1
    conf_mat = confusion_matrix(lbllist.cpu().numpy(), predlist.cpu().numpy())
    print(conf_mat)
    cls = ["lower grade glioma (LGG)", "Glioblastoma (GBM/high grade glioma)", "Normal Brain"]
    # Per-class accuracy
    class_accuracy = 100 * conf_mat.diagonal() / conf_mat.sum(1)
    print(class_accuracy)

liveloss.draw()
                 
#Computing metrics:
                 
# Confusion matrix
conf_mat = confusion_matrix(lbllist.cpu().numpy(), predlist.cpu().numpy())

print(conf_mat)
cls = ["lower grade glioma (LGG)", "Glioblastoma (GBM/high grade glioma)", "Normal Brain"]
# Per-class accuracy
class_accuracy = 100 * conf_mat.diagonal() / conf_mat.sum(1)
print(class_accuracy)

plt.figure(figsize=(10, 10))
plot_confusion_matrix(conf_mat, cls)
plt.show()
