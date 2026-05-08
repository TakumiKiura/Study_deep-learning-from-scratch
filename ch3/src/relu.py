# Code from:
# <https://github.com/oreilly-japan/deep-learning-from-scratch/blob/master/ch03/relu.py>
# Copyright (c) 2016 Koki Saitoh
# Licensed under the MIT License

# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()