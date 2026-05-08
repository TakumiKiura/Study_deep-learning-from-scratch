# Code from:
# <https://github.com/oreilly-japan/deep-learning-from-scratch/blob/master/ch03/step_function.py>
# Copyright (c) 2016 Koki Saitoh
# Licensed under the MIT License

# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=int)

X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # 図で描画するy軸の範囲を指定
plt.show()