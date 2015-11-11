#! /usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
numpy.random.seed(12)


def compute(mode = 'synchronous',
            x=0.,y=0., alpha=.5, I=1.0,
            dt=0.025, t = 15.0):
    x_, y_ = x, y
    X, Y= [x], [y]
    for i in range(int(t/dt)):
        if mode == 'synchronous':
            y += dt*(-alpha*y_ + (y_-x_)*(1-y_) + alpha*I)
            x += dt*(-alpha*x_ + (x_-y_)*(1-x_) + alpha*I)
        elif mode == 'asynchronous':
            if numpy.random.random() < 0.5:
                y += dt*(-alpha*y_ + (y_-x_)*(1-y_) + alpha*I)
            else:
                x += dt*(-alpha*x_ + (x_-y_)*(1-x_) + alpha*I)
        elif mode == 'asynchronous-uniform':
            if numpy.random.random() < 0.5:
                y += dt*(-alpha*y + (y-x)*(1-y) + alpha*I)
                x += dt*(-alpha*x + (x-y)*(1-x) + alpha*I)
            else:
                x += dt*(-alpha*x + (x-y)*(1-x) + alpha*I)
                y += dt*(-alpha*y + (y-x)*(1-y) + alpha*I)
        x = numpy.minimum(numpy.maximum(0,x),1)
        y = numpy.minimum(numpy.maximum(0,y),1)
        X.append(x)
        Y.append(y)
        x_,y_ = x,y
    return X,Y

fig = plt.figure(figsize=(12,8))
fig.patch.set_alpha(0.0)

plt.subplot(111)
Xs, Ys = compute('synchronous')
plt.plot(numpy.array(Xs),Ys, color='blue', lw=3)
plt.plot(numpy.array(Xs),Ys, 'bo', alpha=.05, color='blue')

for k in range(3):
    for i in range(10000):
        Xa, Ya = compute('asynchronous')
        d = numpy.sqrt(((Xa[-1])**2 +(Ya[-1]-1)**2))
        print i, d
        if d < .05:
            break
    Xa = numpy.array(Xa)
    plt.plot(Xa,Ya, color='red', lw=1)
    plt.plot(Xa,Ya, 'bo', alpha=.05, color='red')

for k in range(3):
    for i in range(10000):
        Xa, Ya = compute('asynchronous')
        d = numpy.sqrt(((Xa[-1]-1)**2 +(Ya[-1])**2))
        print i, d
        if d <.05:
            break
    Xa = numpy.array(Xa)
    plt.plot(Xa,Ya, color='red', lw=1)
    plt.plot(Xa,Ya, 'bo', alpha=.05, color='red')

for k in range(3):
    for i in range(10000):
        Xa, Ya = compute('asynchronous', t=20)
        d = numpy.sqrt(((Xa[-1]-1)**2 +(Ya[-1]-1)**2))
        print i, d
        if d <.01:
            break
    Xa = numpy.array(Xa)
    plt.plot(Xa,Ya, color='red', lw=1)
    plt.plot(Xa,Ya, 'bo', alpha=.05, color='red')

#plt.axis([0,2,0,1])
plt.xlabel('x', fontsize=32)
plt.ylabel('y', fontsize=32)
#plt.xticks([])
#plt.yticks([])
fig.savefig('asynchronous.png', dpi=150)
#plt.show()


