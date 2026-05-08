# Code from:
# <https://github.com/oreilly-japan/deep-learning-from-scratch/blob/master/ch03/sigmoid.py>
# Copyright (c) 2016 Koki Saitoh
# Licensed under the MIT License

# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    

X = np.arange(-5.0, 5.0, 0.1)
Y = sigmoid(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()