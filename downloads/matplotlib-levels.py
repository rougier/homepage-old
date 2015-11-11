#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (C) 2011  Nicolas P. Rougier
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the glumpy Development Team nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# -----------------------------------------------------------------------------
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


# Data to be represented
# ----------
labels = ['January', 'Feburary', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
n = len(labels)
data = np.random.uniform(0,1,n)
# ----------



# Make figure square and background the same colors as axes (white)
fig = plt.figure(figsize=(12,12), facecolor='white')

# Make a new polar axis
axes = plt.subplot(111, polar=True, axisbelow=True)

# Put labels on outer 
T = np.arange(np.pi/n, 2*np.pi, 2*np.pi/n)
R = np.ones(n)*10
width = 2*np.pi/n

# Label background
bars  = axes.bar(T, R, width=width, bottom=9,
                 linewidth = 2, facecolor = '0.9', edgecolor='1.00')
# Labels
for i in range(T.size):
    theta = T[n-1-i]+np.pi/n + np.pi/2
    plt.text(theta, 9.5, labels[i], rotation=180*theta/np.pi-90,
             family='Helvetica Neue', size=12,
             horizontalalignment="center", verticalalignment="center")

# Data
R = 1 + data*6
bars = axes.bar(T, R, width=width, bottom=2,
                linewidth=1, facecolor = '0.75', edgecolor='1.00')
for i,bar in enumerate(bars):
    bar.set_facecolor(plt.cm.hot(R[i]/10))

# Text i the center
plt.text(1*np.pi/2, 0.05, "2012",
         size=28, family='Helvetica Neue Light',
         horizontalalignment="center", verticalalignment="bottom")
plt.text(3*np.pi/2, 0.05, "some levels", color="0.50",
         size=15, family='Helvetica Neue Light',
         horizontalalignment="center", verticalalignment="top")

# Set ticks, tick labels and grid
plt.ylim(0,10)
plt.xticks(T)
plt.yticks(np.arange(2,9))
axes.grid(which='major', axis='y', linestyle='-', color='0.75')
axes.grid(which='major', axis='x', linestyle='-', color='1.00')
for theta in T:
    axes.plot([theta,theta], [4,9], color='w', zorder=2, lw=1)
axes.set_xticklabels([])
axes.set_yticklabels([])

fig.savefig('matplotlib-levels.png', facecolor='white')
plt.show()
