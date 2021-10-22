import os
from os import getcwd
from pathlib import Path
import torchio


class Datasets:

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def brats(self):

        HGG = []  # High-grade glioma samples

        for path, currentDirectory, files in os.walk(os.path.join(self.dataset_path, 'data/MICCAI_BraTS_2019_Data/HGG')):
            for file in files:
                if file.endswith('_t1ce.nii.gz'):
                    img_path = Path(path + '/' + os.path.basename(path) + '_t1ce.nii.gz')
                    HGG.append(torchio.Subject(t1=torchio.ScalarImage(img_path), label=1,))

        LGG = []  # Low-grade glioma samples

        for path, currentDirectory, files in os.walk(os.path.join(self.dataset_path,'data/MICCAI_BraTS_2019_Data/LGG')):
            for file in files:
                if file.endswith('_t1ce.nii.gz'):
                    img_path = Path(path + '/' + os.path.basename(path) + '_t1ce.nii.gz')
                    LGG.append(torchio.Subject(t1=torchio.ScalarImage(img_path), label=0,))

        brats = HGG + LGG

        return brats

    def ixi(self):

        ixi = []

        for path, currentDirectory, files in os.walk(os.path.join(self.dataset_path, 'data/IXI')):
            for file in files:
                if file.endswith('.nii.gz'):
                    img_path = Path(path + '/' + file)
                    ixi.append(torchio.Subject(t1=torchio.ScalarImage(img_path), label=2,))

        return ixi

    def return_total_samples(self):
        return self.ixi() + self.brats()

