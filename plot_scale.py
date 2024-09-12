#!/usr/bin/env python

#   Copyright (C) 2024 Simon Crase

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''Template for python script using pytorch'''

# https://machinelearningmastery.com/develop-your-first-neural-network-with-pytorch-step-by-step/

from argparse import ArgumentParser
from os.path import join
from time import time
import numpy as np
import matplotlib.pyplot as plt

def parse_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--data', default='./data')
    return parser.parse_args()

if __name__=='__main__':
    plt.rcParams['text.usetex'] = True
    start  = time()
    args = parse_args()

    ts = np.linspace(0,500,500)
    As = ts**(2/3)
    Bs = ts**(1/2)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(ts,As,label=r'$a=t^{\frac{2}{3}}$')
    ax.set_xlabel('t')
    ax.set_ylabel('a')
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    ax.legend()
    fig.savefig('figs/cosmo-2-a-t')

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(ts,As,label=r'Matter dominated: $a=t^{\frac{2}{3}}$')
    ax.plot(ts,Bs,label=r'Radiation dominated: $a=t^{\frac{1}{2}}$')
    ax.set_xlabel('t')
    ax.set_ylabel('a')
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    ax.legend()
    fig.savefig('figs/cosmo-2-a-r')

    elapsed = time() - start
    minutes = int(elapsed/60)
    seconds = elapsed - 60*minutes
    print (f'Elapsed Time {minutes} m {seconds:.2f} s')
    plt.show()
