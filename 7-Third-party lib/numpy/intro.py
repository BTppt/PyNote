import numpy as np

a = np.array([[1, 11, 2, 4]])
b = np.array([[1, 2, 0, 4], [1, 11, 2, 4]])
print(np.sort(b))
print(np.concatenate((a, b), axis=0))
print(b.ndim)
print(b.size)
print(b.shape)
print(b.reshape(1, 8))
print(np.array([0, 1, 2, 4]))
print(np.linspace(0, 4, 5))
print(np.arange(4))
# new axis
print(b[0:1, :])
print(b[:, 0:2])
d = np.array([1, 2, 3, 4])
print(d[:, np.newaxis])
print(d[np.newaxis, :])
# basic operation
x = np.array([0, 1, 2, 3])
y = np.array([4, 3, 2, 1])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(1.5*x)  # broadcasting
print(x**2)
print(x.dot(y.transpose()))  # matrix product
print(x@y.transpose())       # matrix product
print(x.min())
print(x.max())
print(x.sum())
print(np.exp(x))
# random number
print(np.random.randint(0, 5, size=(3, 3)))
rng = np.random.default_rng()
print(rng.standard_normal(10))

