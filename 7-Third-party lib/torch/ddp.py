import torch
import torch.distributed
import torch.nn.parallel
import torch.multiprocessing
import torch.nn as nn
import torch.utils.data as tud
import torch.nn.functional as f


class TrainData(tud.Dataset):

    def __init__(self):
        super(TrainData, self).__init__()
        self.data = torch.rand(100, 100)

    def __getitem__(self, item):
        return self.data[item, :]

    def __len__(self):
        return 100


class Model(nn.Module):

    def __int__(self):
        super(Model, self).__init__()
        self.fc0 = nn.Linear(100, 50)
        self.fc1 = nn.Linear(50, 1)

    def forward(self, x):
        y = f.relu(self.fc0(x))
        y = f.relu(self.fc1(y))
        return y


def main_process():
    pass


def train_process(rank, world_size, *args):
    pass

