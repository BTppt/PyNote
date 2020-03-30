import torchvision
from pathlib import *
import os


def CleanDir(target_path):
    for x in target_path.iterdir():
        if x.is_dir():
            CleanDir(x)
        else:
            os.remove(x)
    target_path.rmdir()


# Dataset
Data_Save_Path = Path('D:\\DataSet\\TorchVision')
File_Path = Data_Save_Path/'MNIST'
if File_Path.exists() and File_Path.is_dir():
    CleanDir(File_Path)
mnist = torchvision.datasets.MNIST(Data_Save_Path, train=True, download=True)
