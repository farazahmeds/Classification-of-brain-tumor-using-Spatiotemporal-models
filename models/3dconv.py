import torch.nn as nn
from torch.nn import Sequential


class modifybasicstem(nn.Sequential):
    """The default conv-batchnorm-relu stem
    """

    def __init__(self):
        super(modifybasicstem, self).__init__(
            nn.Conv3d(1, 64, kernel_size=(3, 7, 7), stride=(1, 2, 2),
                      padding=(1, 3, 3), bias=False),
            nn.BatchNorm3d(64),
            nn.ReLU(inplace=True))
