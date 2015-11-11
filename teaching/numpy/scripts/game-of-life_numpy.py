#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright INRIA
# Contributors: Nicolas P. Rougier (Nicolas.Rougier@inria.fr)
#
# DANA is a computing framework for the simulation of distributed,
# asynchronous, numerical and adaptive models.
#
# This software is governed by the CeCILL license under French law and abiding
# by the rules of distribution of free software. You can use, modify and/ or
# redistribute the software under the terms of the CeCILL license as circulated
# by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info/index.en.html.
#
# As a counterpart to the access to the source code and rights to copy, modify
# and redistribute granted by the license, users are provided only with a
# limited warranty and the software's author, the holder of the economic
# rights, and the successive licensors have only limited liability.
#
# In this respect, the user's attention is drawn to the risks associated with
# loading, using, modifying and/or developing or reproducing the software by
# the user in light of its specific status of free software, that may mean that
# it is complicated to manipulate, and that also therefore means that it is
# reserved for developers and experienced professionals having in-depth
# computer knowledge. Users are therefore encouraged to load and test the
# software's suitability as regards their requirements in conditions enabling
# the security of their systems and/or data to be ensured and, more generally,
# to use and operate it in the same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
# -----------------------------------------------------------------------------
import numpy

def iterate(Z):
    # find number of neighbours that each square has
    N = numpy.zeros(Z.shape)
    N[1:, 1:] += Z[:-1, :-1]
    N[1:, :-1] += Z[:-1, 1:]
    N[:-1, 1:] += Z[1:, :-1]
    N[:-1, :-1] += Z[1:, 1:]
    N[:-1, :] += Z[1:, :]
    N[1:, :] += Z[:-1, :]
    N[:, :-1] += Z[:, 1:]
    N[:, 1:] += Z[:, :-1]
    # a live cell is killed if it has fewer 
    # than 2 or more than 3 neighbours.
    part1 = ((Z == 1) & (N < 4) & (N > 1)) 
    # a new cell forms if a square has exactly three members
    part2 = ((Z == 0) & (N == 3))
    return (part1 | part2).astype(int)


Z = numpy.array([[0,0,0,0,0,0],
                 [0,0,0,1,0,0],
                 [0,1,0,1,0,0],
                 [0,0,1,1,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]])

Z = numpy.random.randint(0,2,(80,40))
#print 'Initial state:\n', Z[1:-1,1:-1]

U = Z.copy()
for i in range(100):
    Z = iterate(Z)
    U = U/2. + Z


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

size = 10*np.array(Z.shape)
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
matplotlib.rcParams['figure.dpi']  = 72.0
matplotlib.rcParams['savefig.dpi'] = 72.0
matplotlib.rcParams['xtick.major.size'] = 0
matplotlib.rcParams['xtick.minor.size'] = 0
matplotlib.rcParams['ytick.major.size'] = 0
matplotlib.rcParams['ytick.minor.size'] = 0
fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")
axes = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)

X,Y = np.meshgrid(np.linspace(0,1,Z.shape[0]),np.linspace(0,1,Z.shape[1]))
plt.xlim(-0.025, 1.025)
plt.ylim(-0.05, 1.05)
plt.scatter(X,Y,c=U,s=80, cmap=plt.cm.Purples, linewidths=.05)

#plt.show()
plt.savefig("game-of-life.png")



#print 'Final state:\n', Z[1:-1,1:-1]
