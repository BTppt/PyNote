import scipy.io
import scipy.io.matlab.miobase as me
import torch
import numpy

d1 = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
content = {'key1': ['w1', 'w2'], 'key2': [2, 3], '__globals__': 6, 'key3': d1.numpy()}
scipy.io.savemat('.\\resource\\test.mat', content)

try:
    content = scipy.io.loadmat('.\\resource\\test.mat')
    for k, v in content.items():
        if isinstance(v, (numpy.ndarray,)):
            v = v.squeeze()
        print(k, v)
except me.MatReadError:
    print(me.MatReadError)
