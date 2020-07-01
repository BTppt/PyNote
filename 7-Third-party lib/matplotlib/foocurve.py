import matplotlib.pyplot as plt
import numpy as np

# 2-d curve
x = np.linspace(0, 2, 100)
plt.title('Example')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.xlim((0, 4))
plt.ylim((0, 4))
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.legend()
plt.show()

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
