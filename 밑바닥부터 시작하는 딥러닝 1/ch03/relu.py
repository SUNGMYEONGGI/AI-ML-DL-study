# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 8.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 20.5)
plt.show()
