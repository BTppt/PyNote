# AUTOGRAD: AUTOMATIC DIFFERENTIATION

import torch.autograd

a = torch.Tensor([[1,2],[2,3]])
a.requires_grad = True
b = a**2
c = 3*b.sum()
c.backward()
print(a, '\n', b, '\n', c)
print(b.grad)
print(a.grad)

b = torch.Tensor([[1,3],[5,2]])
b.requires_grad = True
c = a*b
d = c.sum()
d.backward()
print(b.grad)
print(a.grad)

