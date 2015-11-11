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
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ----------
# Data to be represented

products = ['Vendor A - Product A', 'Vendor A - Product B', 'Vendor A - Product C',
            'Vendor B - Product A', 'Vendor B - Product B', 'Vendor B - Product C',
            'Vendor C - Product A', 'Vendor C - Product B', 'Vendor C - Product C']

values = np.random.uniform(10,60,len(products))

# ----------

# Choose some nice colors
matplotlib.rc('axes', facecolor = '#6E838A')
matplotlib.rc('axes', edgecolor = '#737373')
matplotlib.rc('axes', linewidth = 1)
matplotlib.rc('ytick', direction='out')
matplotlib.rc('xtick', direction='out')
matplotlib.rc('figure.subplot', left=0.25)

# Make figure background the same colors as axes
fig = plt.figure(figsize=(12,8), facecolor='#6E838A')

# Remove left and top axes spines
axes = plt.subplot(1,1,1)
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')

# Adjust yticks to the number of products
plt.yticks(np.arange(len(products)+1), [])

# Set tick labels color to white
for label in axes.get_xticklabels()+axes.get_yticklabels():
    label.set_color('white')

# Set tick labels line width to 1
for line in axes.get_xticklines() + axes.get_yticklines():
    line.set_markeredgewidth(1)

# Set axes limits
ymin, ymax = 0, len(products)
xmin, xmax = 0, 60
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

# Start with blue colormap
cmap = plt.cm.Blues

for i, label in enumerate(products):

    # Alternate band of light background
    if not i%2:
        p = patches.Rectangle(
            (0, i), xmax, 1, fill=True, transform=axes.transData,
            lw=0, facecolor='w', alpha=.1)
        axes.add_patch(p)

    # Product name left to the axes
    plt.text(-.5, i+0.5, label, color="white", 
             horizontalalignment='right', verticalalignment='center')

    # Plot the bar with gradient (1 to .65)
    value = values[i]
    X = np.array([1,.65]).reshape((1,2))
    axes.imshow(X,extent=(0,value,i+.25,i+.75),cmap=cmap, vmin=0, vmax=1)
    plt.text(value-0.5, i+0.5, '%.1f' % value, color="white", 
             horizontalalignment='right', verticalalignment='center')

    # Change colormap every 3 values
    if i >= 2: cmap = plt.cm.Greens
    if i >= 5: cmap = plt.cm.Reds

# Set a nice figure aspect
axes.set_aspect(4.5)

# Write some title & subtitle
plt.text(1, 10.0, "Vendor benchmarks", color="1.0", fontsize=16)
plt.text(1,  9.7, "(higher is better)", color="0.75", fontsize=12)

# Done
plt.savefig('benchmark.png', facecolor='#6E838A')
plt.show()
