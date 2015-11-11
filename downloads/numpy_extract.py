# Copyright (c) 2009, Nicolas Rougier
# All rights reserved.
#
# Redistribution  and  use  in  source   and  binary  forms,  with  or  without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code  must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions  in  binary form  must  reproduce  the above  copyright
#       notice, this  list of  conditions and the  following disclaimer  in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name  of Nicolas Rougier nor the  names of its contributors
#       may be used  to endorse or promote products  derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE  IS PROVIDED BY  Nicolas Rougier ''AS  IS'' AND ANY  EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT  LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND  FITNESS FOR A  PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO
# EVENT  SHALL   <copyright  holder>  BE  LIABLE  FOR   ANY  DIRECT,  INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT  OF SUBSTITUTE GOODS OR SERVICES;  LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS  INTERRUPTION) HOWEVER CAUSED  AND ON ANY  THEORY OF
# LIABILITY,  WHETHER  IN  CONTRACT,   STRICT  LIABILITY,  OR  TORT  (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY  WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import numpy

def extract(Z, shape, position, fill=numpy.NaN):
    """ Extract a sub-array from Z using given shape and centered on position.
        If some part of the sub-array is out of Z bounds, result will be padded
        with fill value.

        **Parameters**
            `Z` : array_like
               Input array.

           `shape` : tuple
               Shape of the output array

           `position` : tuple
               Position within Z

           `fill` : scalar
               Fill value

        **Returns**
            `out` : array_like
                Z slice with given shape and center

        **Examples**

        >>> Z = numpy.arange(0,16).reshape((4,4))
        >>> extract(Z, shape=(3,3), position=(0,0))
        [[ NaN  NaN  NaN]
         [ NaN   0.   1.]
         [ NaN   4.   5.]]

        Schema:

            +-----------+
            | 0   0   0 | = extract (Z, shape=(3,3), position=(0,0))
            |   +---------------+
            | 0 | 0   1 | 2   3 | = Z
            |   |       |       |
            | 0 | 4   5 | 6   7 |
            +---|-------+       |
                | 8   9  10  11 |
                |               |
                | 12 13  14  15 |
                +---------------+

        >>> Z = numpy.arange(0,16).reshape((4,4))
        >>> extract(Z, shape=(3,3), position=(3,3))
        [[ 10.  11.  NaN]
         [ 14.  15.  NaN]
         [ NaN  NaN  NaN]]

        Schema:

            +---------------+
            | 0   1   2   3 | = Z
            |               |
            | 4   5   6   7 |
            |       +-----------+
            | 8   9 |10  11 | 0 | = extract (Z, shape=(3,3), position=(3,3))
            |       |       |   |
            | 12 13 |14  15 | 0 |
            +---------------+   |
                    | 0   0   0 |
                    +-----------+
    """
    assert(len(position) == len(Z.shape))
    if len(shape) < len(Z.shape):
        shape = shape + Z.shape[len(Z.shape)-len(shape):]

    R = numpy.ones(shape, dtype=Z.dtype)*fill
    P  = numpy.array(list(position)).astype(int)
    Rs = numpy.array(list(R.shape)).astype(int)
    Zs = numpy.array(list(Z.shape)).astype(int)

    R_start = numpy.zeros((len(shape),)).astype(int)
    R_stop  = numpy.array(list(shape)).astype(int)
    Z_start = (P-Rs//2)
    Z_stop  = (P+Rs//2)+Rs%2

    R_start = (R_start - numpy.minimum(Z_start,0)).tolist()
    Z_start = (numpy.maximum(Z_start,0)).tolist()
    R_stop = numpy.maximum(R_start, (R_stop - numpy.maximum(Z_stop-Zs,0))).tolist()
    Z_stop = (numpy.minimum(Z_stop,Zs)).tolist()

    r = [slice(start,stop) for start,stop in zip(R_start,R_stop)]
    z = [slice(start,stop) for start,stop in zip(Z_start,Z_stop)]

    R[r] = Z[z]

    return R

Z = numpy.arange(0,16).reshape((4,4))
print Z
print
print extract(Z, shape=(3,3), position=(0,0))
print
print extract(Z, shape=(3,3), position=(3,3))

