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

from collections import OrderedDict

from torchsampler import ImbalancedDatasetSampler

import torchvision
from torchvision import datasets, models, transforms

import torchio
from torchio.transforms import OneOf
from torchio.transforms import (
    RescaleIntensity,
    RandomAffine,
    RandomElasticDeformation,
    Compose,
)
from torchio import RandomFlip

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom
from livelossplot import PlotLosses
from torchio.transforms import CropOrPad

import time
import os
import pandas as pd
from skimage import io
import numpy as np
from torchvision.transforms import transforms
from torch.utils.tensorboard import SummaryWriter
from apex import amp

from sklearn.metrics import confusion_matrix
import itertools

from dataset import brats
from plotcm import plot_confusion_matrix

torch.manual_seed(23)
os.environ['TORCH_HOME'] = '/scratch/faraz/tmp4'
num_classes = 3
learning_rate = 0.00001
num_epochs = 100
num_workers = 5
opt_level = 'O1'
load_model=True




# class weights

# normedWeights = [1 - (x / sum(weights)) for x in weights]
# normedWeights = torch.FloatTensor(normedWeights)


# class_weights = torch.FloatTensor([0.8760, 0.5617, 0.5617]).cuda()

class_weights = torch.FloatTensor([3.54,1,1]).cuda()

#
# Let's use one preprocessing transform and one augmentation transform
# This transform will be applied only to torchio.INTENSITY images:

rescale = RescaleIntensity((0.05, 99.5))

# As RandomAffine is faster then RandomElasticDeformation, we choose to
# apply RandomAffine 80% of the times and RandomElasticDeformation the rest
# Also, there is a 25% chance that none of them will be applied

randaffine = torchio.RandomAffine(scales=(0.9,1.2),degrees=10, isotropic=True, image_interpolation='nearest')

flip = torchio.RandomFlip(axes=('LR'), p=0.5)
croporpad = CropOrPad(target_shape=(240, 240, 155))

# Transforms can be composed as in torchvision.transforms
transforms = [rescale, flip, randaffine]

transform = Compose(transforms)

# ImagesDataset is a subclass of torch.data.utils.Dataset
subjects_dataset = torchio.SubjectsDataset(brats(), transform=transform)

# Images are processed in parallel thanks to a PyTorch DataLoader

trainset, testset = torch.utils.data.random_split(subjects_dataset, [414, 177], generator=torch.Generator().manual_seed(19))



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
    nn.Linear(model.fc.in_features, num_classes)
)

liveloss = PlotLosses()

model.to('cuda:0')

criterion = nn.CrossEntropyLoss(weight=class_weights)

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=1e-3)
# scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[50,100,150], gamma=0.1)

# Initialize the prediction and label lists(tensors) for confusion matrix
predlist = torch.zeros(0, dtype=torch.long).to('cuda:0')
lbllist = torch.zeros(0, dtype=torch.long).to('cuda:0')

model, optimizer = amp.initialize(model, optimizer, opt_level=opt_level)

tb = SummaryWriter(f'/scratch/faraz/Thesis/runs')




def save_checkpoint(state,filename="/run/media/faraz/USB/model/cross_fold_mixed_conv2.pth.tar"):
    torch.save(state,filename)


if load_model:
    # load_checkpoint(torch.load("/run/media/faraz/USB/model/lucky13.pth.tar"))
    from resume_from_checkpoint import resume_from_checkpoint
    fpath = '/run/media/faraz/USB/model/cross_fold_mixed_conv2.pth.tar'
    start_epoch = resume_from_checkpoint(fpath, model, optimizer)


# init_start_epoch = start_epoch

for epoch in range(num_epochs):

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
        images = F.interpolate(traindata['t1'][torchio.DATA], scale_factor=(0.5,0.5,0.5)).to('cuda:0')
        labels = traindata['t1']['mylabel'].to('cuda:0')

        # print(labels)



        optimizer.zero_grad()


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
          .format(epoch + 1, num_epochs, i + 1, len(trainloader), (total_loss / total_images),
                  (total_correct / total_images) * 100))



    # Testing the model

    with torch.no_grad():
        correct = 0
        total = 0

        for testdata in testloader:
            # print ("for testdata in testloader, len of testdata",len(testdata))
            images = F.interpolate(testdata['t1'][torchio.DATA], scale_factor=(0.5,0.5,0.5)).to('cuda:0')

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
