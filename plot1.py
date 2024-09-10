#!/usr/bin/env python

# snarfed from https://gist.github.com/cswiercz/1fde0a82f8e9e1b0660a
import numpy as np
from matplotlib import cm, colors
from matplotlib import pyplot as plt

branching_number = 2

Nr = 16
Ntheta = 32

# compute the theta,R domain
theta = np.linspace(0,2*np.pi*branching_number, Ntheta)
r = np.linspace(0,1,Nr)
Theta, R = np.meshgrid(theta,r)

z = R*np.exp(1j*Theta)

# compute w^2 = z. THE KEY IDEA is to pass the exponentiation by 1/2 into exp().
w = np.sqrt(R)*np.exp(1j*Theta/2)

# color by argument
arguments = np.angle(w)
norm = colors.Normalize(arguments.min(), arguments.max())
color = cm.jet(norm(arguments))

fig = plt.figure(figsize=(16,8))

# plot the real part
ax_real = fig.add_subplot(1,2,1,projection='3d')
ax_real.plot_surface(z.real, z.imag, w.real,
                    rstride=1, cstride=1, alpha=0.5, facecolors=color)

# plot the imaginary part
ax_imag = fig.add_subplot(1,2,2,projection='3d')
ax_imag.plot_surface(z.real, z.imag, w.imag,
                    rstride=1, cstride=1, alpha=0.5, facecolors=color)
plt.show()
