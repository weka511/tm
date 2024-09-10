#!/usr/bin/env python

# Copyright (C) 2019-2024 Greenweaves Software Limited

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

a = 0.12
b = 0.1
L = 1.1
fig = plt.figure()
ax = plt.axes(projection='3d')

X = np.arange(-L, L, 0.05)
Y = np.arange(-L, L, 0.05)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

Z = -a*R + b *R *R

ax.contour3D(X, Y, Z, 50, cmap=cm.coolwarm)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
plt.savefig('figs/mexican-hat')

plt.show()
