===================
100 numpy exercices
===================

-------------------------------
A joint effort of the community
-------------------------------

.. contents::
   :local:
   :depth: 1


Neophyte
========

1. Import the numpy package under the name ``np``

   .. code:: python

      import numpy as np


#. Print the numpy version and the configuration.

   .. code:: python

      print np.__version__
      np.__config__.show()




#. Create a null vector of size 10

   .. code:: python

      Z = np.zeros(10)

#. Create a null vector of size 10 but the fifth value which is 1

   .. code:: python

      Z = np.zeros(10)
      Z[4] = 1

#. Create a vector with values ranging from 10 to 99

   .. code:: python

      Z = 10 + np.arange(90)

#. Create a 3x3 matrix with values ranging from 0 to 8

   .. code:: python

      Z = np.arange(9).reshape(3,3)
 

#. Declare a 3x3 identity matrix

   .. code:: python

      Z = np.eye(3)

#. Declare a 4x4 matrix with values 1,2,3,4 on the diagonal

   .. code:: python

      Z = np.diag(1+np.arange(4))

#. Declare a 5x5 matrix with values 1,2,3,4 just below the diagonal

   .. code:: python

      Z = np.diag(1+np.arange(4),k=-1)
   

#. Declare a 10x10x10 array with random values

   .. code:: python

      Z = np.random.random((10,10,10))



Novice
======

1. Declare a 8x8 matrix and fill it with a checkerboard pattern

   .. code:: python

      Z = np.zeros((8,8))
      Z[1::2,::2] = 1
      Z[::2,1::2] = 1

#. Declare a 10x10 array with random values and find the minimum and maximum values

   .. code:: python

      Z = np.random.random((10,10,10))
      Zmin, Zmax = Z.min(), Z.max()

#. Create a checkerboard 8x8 matrix using the tile function

   .. code:: python

      Z = np.tile( np.array([[0,1],[1,0]]), (4,4))

#. Normalize (between 0 and 1) a 5x5 random matrix()

   .. code:: python

      Z = np.random.random((5,5))
      Zmax,Zmin = Z.max(), Z.min()
      Z = (Z - Zmin)/(Zmax - Zmin)


#. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

   .. code:: python

      Z = np.dot(np.ones((5,3)), np.ones((3,2)))


#. Create a 10x10 matrix with row values ranging from 0 to 9

   .. code:: python
 
    Z = np.zeros((10,10))
    Z += np.arange(10)

#. Create a vector of size 1000 with values ranging from 0 to 1, both excluded

   .. code:: python
 
    Z = np.random.linspace(0,1,1002,endpoint=True)[1:-1]

#. Create random vector of size 100 and replace the maximum value by 0

   .. code:: python
 
    Z = np.random.random(100)
    Z[Z.argmax()] = 0

#. Create a random vector of size 100 and sort it

   .. code:: python
 
    Z = np.random.random(100)
    Z.sort()

#. Consider a random 100x2 matrix representing cartesian coordinates, convert
   them to polar coordinates

   .. code:: python
 
      Z = np.random.random((100,2))
      X,Y = Z[:,0], Z[:,1]
      R = np.sqrt(X**2+Y**2)
      T = np.arctan2(Y,X)




  


Apprentice
==========

Journeyman
==========

1. Consider a given vector, how to add 1 to each element indexed by a second
   vector (be careful with repeated indices) ?

   .. code:: python

      # Author: Brett Olsen

      Z = np.ones(10)
      I = np.random.randint(0,len(Z),20)
      Z += np.bincount(I, minlength=len(Z))


#. How to accumulate elements of a vector (X) to an array (F) based on an index
   list (I) ?

   .. code:: python

      # Author: Alan G Isaac

      X = [1,2,3,4,5,6]
      I = [1,3,9,3,4,1]
      F = np.bincount(I,X)




Craftsman
=========

Artisan
=======

1. Considering a 100x3 matrix, extract rows with unequal value (e.g. [2,2,3])

   .. code:: python

      # Author: Robert Kern

      Z = np.random.randint(0,5,(100,3))
      E = np.logical_and.reduce(Z[:,1:] == Z[:,:-1], axis=1)
      U = Z[~E]


Adept
=====

1. Convert a vector of ints into a matrix binary representation.

   .. code:: python

      # Author: Warren Weckesser

      I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])
      B = ((I.reshape(-1,1) & (2**np.arange(8))) != 0).astype(int)
      B = B[:,::-1]


Expert
======

Master
======

Archmaster
==========



