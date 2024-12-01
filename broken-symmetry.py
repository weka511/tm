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

''' Explore broken symmetry from lecture 7'''

from argparse import ArgumentParser
import numpy as np
from matplotlib.pyplot import figure, show
from time import time

def parse_argumeents():
    parser = ArgumentParser (__doc__)
    parser.add_argument('--m',type=int,default=100,help='Number of spins')
    parser.add_argument('--n',type=int,default=1000,help='Number of iterations for fixed temperature')
    parser.add_argument('--N',type=int,default=25,help='Number of steps in temperature')
    parser.add_argument('--seed',type=int,default=None,help='Seed for random number generator')
    parser.add_argument('--clamped',default=False, action='store_true',help='Clamp endsS')
    parser.add_argument('--T',type=float, default=0.001,help='Starting value of temperature in Bolzmann units')
    parser.add_argument('-cool',type=float, default=0.01,help='rate of cooling')
    return parser.parse_args()

def get_energy(S,i,flipped=False, clamped=False):
    state = - S[i] if flipped else S[i]
    left = (-1 if clamped else 0) if i==0 else S[i-1]
    right = (+1 if clamped else 0) if i>= args.m-1 else S[i+1]
    return -1 *(left + right) * state

if __name__=='__main__':
    start  = time()
    args = parse_argumeents()
    rng = np.random.default_rng(args.seed)
    S = rng.choice([-1,1], size=args.m)
    t = args.T
    fig = figure(figsize=(10,10))
    K1 = int(np.sqrt(args.N + 1))
    K2 = args.N //K1
    while K1 * K2 < args.N + 1:
        K2 +=1

    ax = fig.add_subplot(K1,K2,1)
    ax.scatter(range(len(S)),S,c=S,s=1)
    for i in range(args.N):
        E = sum(get_energy(S,j) for j in range(len(S)))

        for _ in range(args.n):
            low = 1 if args.clamped else 0
            high = len(S) - low
            j = rng.integers(low,high=high)
            E0 = get_energy(S,j,clamped=args.clamped)
            E1 = get_energy(S,j,flipped=True,clamped=args.clamped)
            if E1 < E0:
                S[j] *= -1
                E += (E1-E0)
            else:
                deltaE = E1 - E0
                x = rng.random()
                threshold = np.exp(-deltaE/t)
                if x < threshold:
                    S[j] *= -1
                    E += (E1-E0)
        ax = fig.add_subplot(K1,K2,i+2)
        ax.scatter(range(len(S)),S,c=S,s=1)
        t /= (1+args.cool)

    elapsed = time() - start
    minutes = int(elapsed/60)
    seconds = elapsed - 60*minutes
    print (f'Elapsed Time {minutes} m {seconds:.2f} s')
    show()
