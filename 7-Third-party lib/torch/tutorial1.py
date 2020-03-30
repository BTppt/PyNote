import torch

# Tensor
x = torch.empty(4, 3)
print(x)
print(torch.rand(3, 3))
print(torch.zeros(4, 4, dtype=torch.int64))
print(torch.tensor([[11, 12, 13], [21, 22, 23], [31, 32, 33]]))
print(torch.randn_like(x, dtype=torch.float))
print(x.size())
# resizing
y = x.view(-1, 6)
print(y.shape)
# Operations
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([4, 3, 2, 1], dtype=torch.float)
print(x+y)
print(torch.add(x, y))
print(x-y)
print(x*y)
print(x % y)
print(x/y)
print(torch.div(x, y))
# in-place addition
x.add_(x)
# Numpy bridge
# Converting a Torch Tensor to a NumPy array and vice versa is a breeze.
# The Torch Tensor and NumPy array will share their underlying memory locations
# (if the Torch Tensor is on CPU), and changing one will change the other.
z = x.numpy()
print(z)
# z = torch.from_numpy(numpy.narray)
# CUDA Tensor
if torch.cuda.is_available():
    device = torch.device('cuda')
    z = torch.ones_like(x, device=device)
    w = x.to(device)
    print(z)
    print(w)
else:
    print(" NO GPU")

# Automatic Differentiation
t1 = torch.tensor([1, 2, 3, 4], dtype=torch.float, requires_grad=True)
print(t1.requires_grad)
print(t1.grad_fn)
print(t1.grad)
y = t1.sum()
y = y**2
y = y + t1.sum()
y.backward()
print(t1.grad)