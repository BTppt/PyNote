import torch
import torch.nn as nn
import torch.cuda
import torch.nn.functional as f
import torchvision
from torchvision import transforms
import numpy as np
#import torchsnooper
import matplotlib.pyplot as plt

dataset = torchvision.datasets.MNIST(root='E:/dataset/',download=False,transform=transforms.ToTensor(),train=True)
dataloader = torch.utils.data.DataLoader(dataset,batch_size=256)
# network
class LeNet(nn.Module):
    def __init__(self):
        super(LeNet,self).__init__()
        self.conv1 = nn.Conv2d(1,6,5,padding=2)
        self.conv2 = nn.Conv2d(6,16,5)
        self.fc1 = nn.Linear(16*5*5,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)
        self.pool2d = nn.MaxPool2d(2)
    #@torchsnooper.snoop()
    def forward(self,x):
        output = f.relu(self.conv1(x))
        output = self.pool2d(output)
        output = f.relu(self.conv2(output))
        output = self.pool2d(output)
        output = output.view(output.size(0),-1)
        output = f.relu(self.fc1(output))
        output = f.relu(self.fc2(output))
        output = self.fc3(output)
        return output

# train
cuda0 = torch.device('cuda')
criterion = nn.CrossEntropyLoss().cuda(cuda0)
model = LeNet().cuda(cuda0)
optimizer = torch.optim.SGD(model.parameters(),lr=0.1)

for i in range(10):
    print("In epoch {}:".format(i))
    loss_record = []
    for imgs, labels in dataloader:
        imgs = imgs.to(cuda0)
        labels = labels.to(cuda0)
        preds = model(imgs)
        loss = criterion(preds, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss_record.append(loss.item())
        print("Loss function {:.3f}".format(loss.item()),end = '\r')
    print("")
    print("Average loss in epoch {} is {:.3f}".format(i,np.mean(loss_record)))
# test
dataset_test = torchvision.datasets.MNIST(root="E:/dataset/", download=False,transform=transforms.ToTensor(),train=False)
plt.imshow(dataset_test[0][0].squeeze().numpy())
plt.show()
print(dataset_test[0][1])
print(model(dataset_test[0][0].unsqueeze(0).cuda(cuda0)).softmax(-1).argmax())
