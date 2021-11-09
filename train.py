import hydra
from omegaconf import DictConfig, OmegaConf
from hydra.utils import instantiate

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

import torchio

from torchio.transforms import (
    CropOrPad,
    OneOf,
    RescaleIntensity,
    RandomAffine,
    RandomElasticDeformation,
    RandomFlip,
    Compose,
)

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom

import os
from pathlib import Path

import numpy as np
from torchvision.transforms import transforms

from sklearn.metrics import confusion_matrix
from score_gen.confmatrix import plot_confusion_matrix

from dataset.datasets import Datasets
import wandb



def train(config: DictConfig) -> None:
    wandb.init(project=config.wandb_logger.project, entity=config.wandb_logger.entity, group=config.wandb_logger.group)

    cwd = os.getcwd()

    volumes = hydra.utils.instantiate(config.dataset_)

    total_Samples = volumes.return_total_samples()
    
    torch.manual_seed(config.global_seed)

    load_model = config.load_model
    
    class_weights = torch.FloatTensor([3.54,1,1]).cuda() #for dataset being unbalanced for classes [LGG, HGG, Healthy]

    #Transforms
    
    rescale = RescaleIntensity((0.05, 99.5))
    randaffine = torchio.RandomAffine(scales=(0.9,1.2),degrees=10, isotropic=True, image_interpolation='nearest')
    flip = torchio.RandomFlip(axes=('LR'), p=0.5)
    croporpad = CropOrPad(target_shape=(240, 240, 155))
    transforms = [rescale, flip, randaffine]

    transform = Compose(transforms)

    subjects_dataset = torchio.SubjectsDataset(total_Samples, transform=transform)

    train_set_samples = (int(len(total_Samples)-0.3*len(total_Samples)))  #train_test_split
    test_set_samples =  (int(len(total_Samples))-(train_set_samples))

    trainset, testset = torch.utils.data.random_split(subjects_dataset, [train_set_samples, test_set_samples], generator=torch.Generator().manual_seed(config.dataset.train_test_split_seed))

    trainloader = DataLoader(dataset=trainset,  batch_size=config.training.batch_size, shuffle=True)
    testloader = DataLoader(dataset=testset,   batch_size=config.training.batch_size, shuffle=True)

    #instantiate the overriden classes:
    
    if config.models.model == 'resnet2p1':
        model = torchvision.models.video.r2plus1d_18(pretrained=config.pretrain)
        model.stem = hydra.utils.instantiate(config.resnet2p1Stem)
    elif config.models.model == 'resnet_mixed_conv':
        model = torchvision.models.video.mc3_18(pretrained=config.pretrain)
        model.stem = hydra.utils.instantiate(config.resnet_mixed_convStem)
    else:
        model = torchvision.models.video.r3d_18(pretrained=config.pretrain)
        model.stem = hydra.utils.instantiate(config.conv3dStem)

    # regularization
    
    model.fc = nn.Sequential(
        nn.Dropout(config.training.dropout),
        nn.Linear(model.fc.in_features, config.training.num_classes)
    )

    model.to('cuda:0')

    criterion = nn.CrossEntropyLoss(weight=class_weights)

    optimizer = torch.optim.Adam(model.parameters(), lr=config.training.learning_rate, weight_decay=config.training.weight_decay)

    # Initialize the prediction and label lists(tensors) for confusion matrix
    predlist = torch.zeros(0, dtype=torch.long).to('cuda:0')
    lbllist = torch.zeros(0, dtype=torch.long).to('cuda:0')

    
    if load_model:
        the_model = torch.load(Path(cwd,'outputs'))

    for epoch in range(config.training.num_epoch):

        logs = {}
        total_correct = 0
        total_loss = 0
        total_images = 0
        total_val_loss = 0

        if epoch % 5 == 0:
            checkpoint = {'epoch': epoch+1, 'state_dict': model.state_dict(), 'optimizer': optimizer.state_dict()}
            print("Load True: saving checkpoint")
            torch.save(model.state_dict(), Path(cwd,'outputs'))

            # else:
            #     checkpoint = {'epoch': epoch + 1, 'state_dict': model.state_dict(),
            #                   'optimizer': optimizer.state_dict()}
            #     print("Loade False: saving checkpoint")
            #     save_checkpoint(checkpoint)

        for i, traindata in enumerate(trainloader):
            images = F.interpolate(traindata['t1'][torchio.DATA], scale_factor=(config.dataset.img_scale_factor,config.dataset.img_scale_factor,config.dataset.img_scale_factor)).to('cuda:0')
            labels = traindata['label'].to('cuda:0')
            optimizer.zero_grad()

            # Forward propagation
            outputs = model(images)


            # Calculating loss with softmax to obtain cross entropy loss

            # loss = criterion(outputs, labels)

            loss = criterion(outputs, labels)  # ....>

            # Backward prop
            loss.backward()

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
            wandb.log({'training accuracy': running_trainacc})


        print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'
              .format(epoch + 1, config.training.num_epoch, i + 1, len(trainloader), (total_loss / total_images),
                      (total_correct / total_images) * 100))


        # Testing the model

        with torch.no_grad():
            correct = 0
            total = 0

            for testdata in testloader:

                images = F.interpolate(testdata['t1'][torchio.DATA], scale_factor=(config.dataset.img_scale_factor,config.dataset.img_scale_factor,config.dataset.img_scale_factor)).to('cuda:0')

                labels = testdata['label'].to('cuda:0')
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

            wandb.log({'test accuracy': validationacc, 'val loss': validationloss})

        conf_mat = confusion_matrix(lbllist.cpu().numpy(), predlist.cpu().numpy())
        print(conf_mat)
        cls = ["lower grade glioma (LGG)", "Glioblastoma (GBM/high grade glioma)", "Normal Brain"]
        # Per-class accuracy
        class_accuracy = 100 * conf_mat.diagonal() / conf_mat.sum(1)
        print(class_accuracy)

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
