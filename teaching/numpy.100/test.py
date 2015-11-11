import numpy as np
from numpy.lib import stride_tricks

# Z = np.random.randint(0,2,(5,5))
# n = 3
# i = 1 + (Z.shape[0]-3)
# j = 1 + (Z.shape[1]-3)
# C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)

# print Z
# C = C.reshape(i,j,n*n)
# print
# print C.sum(axis=2) - Z[1:-1,1:-1]


def count_1(Z):
    N = np.zeros(Z.shape, int)
    N[1:-1,1:-1] += (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
                     Z[1:-1,0:-2]                + Z[1:-1,2:] +
                     Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])
    return N

def count_2(Z):
    n = 3
    i = 1 + (Z.shape[0]-3)
    j = 1 + (Z.shape[1]-3)
    C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
    C = C.reshape(i,j,n*n)
    return C.sum(axis=2) - Z[1:-1,1:-1]




# w,h = 16,16
# I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
# F = I[...,0]*256*256 + I[...,1]*256 +I[...,2]
# colors = I.reshape(h*w,3)[np.unique(F,return_index=True)[1]]
# print len(colors)



# Z = np.array([1,2,3,4,5])
# nz = 3
# Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
# Z0[::(nz+1)] = Z
# print Z0


# Z = np.random.random((25,25))
# shape = (3,3)
# fill  = 0
# position = (0,0)

# R = np.ones(shape, dtype=Z.dtype)*fill
# P  = np.array(list(position)).astype(int)
# Rs = np.array(list(R.shape)).astype(int)
# Zs = np.array(list(Z.shape)).astype(int)

# R_start = np.zeros((len(shape),)).astype(int)
# R_stop  = np.array(list(shape)).astype(int)
# Z_start = (P-Rs//2)
# Z_stop  = (P+Rs//2)+Rs%2

# R_start = (R_start - np.minimum(Z_start,0)).tolist()
# Z_start = (np.maximum(Z_start,0)).tolist()
# R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop-Zs,0))).tolist()
# Z_stop = (np.minimum(Z_stop,Zs)).tolist()

# r = [slice(start,stop) for start,stop in zip(R_start,R_stop)]
# z = [slice(start,stop) for start,stop in zip(Z_start,Z_stop)]
# R[r] = Z[z]

# print R
