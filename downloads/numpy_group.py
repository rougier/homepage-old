#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2010, Nicolas P. Rougier
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided
#        with the distribution.
#
#     * Neither the name of Nicolas P. Rougier nor the names of any
#        contributors may be used to endorse or promote products derived
#        from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
A group object represents a multidimensional, homogeneous group of contiguous
numpy arrays.  An associated data-type object describes the format of each
element in the group (its byte-order, how many bytes it occupies in memory,
whether it is an integer or a floating point number, etc.).
'''
import numpy


class group(object):
    '''
    A group object represents a multidimensional, homogeneous group of
    contiguous numpy arrays.  An associated data-type object describes the
    format of each element in the group (its byte-order, how many bytes it
    occupies in memory, whether it is an integer or a floating point number,
    etc.).

    Groups should be constructed using `ones`, `zeros` or `empty` (refer to
    the ``See Also`` section below).  The parameters given here describe a
    low-level method for instantiating a group.

    See also
    --------
    * :meth:`group.zeros` : Return a new group setting values to zero.
    * :meth:`group.ones` : Return a new group setting values to one.
    * :meth:`group.empty` : Return an unitialized group.
    * :meth:`group.zeros_like` : Return a group of zeros with shape and type of input.
    * :meth:`group.ones_like` : Return a group of ones with shape and type of input.
    * :meth:`group.empty_like` : Return a empty group with shape and type of input.
    '''

    def __init__(self, shape=(), dtype=float, order='C', fill=None):
        '''
        Creates a new group
      
        Parameters
        ----------
        shape : tuple of ints
            Shape of created group.
        dtype : data-type, optional
            Any object that can be interpreted as a numpy data type.
        order : {'C', 'F'}, optional
            Row-major or column-major order.
        '''
        if type(shape) is int:
            shape = (shape,)
        elif type(shape) is numpy.ndarray:
            obj = shape
            shape = obj.shape
            dtype = obj.dtype
            if fill is None:
                fill = obj
        if not isinstance(dtype,numpy.dtype):
            if type(dtype) == list:
                d = [(n,t) for n,t in dtype]
                dtype = d
            else:
                dtype = [('f0', numpy.dtype(dtype)),]
        elif dtype.type is numpy.void:
            d = [(name,dtype[i]) for i, name in enumerate(dtype.names)]
            dtype = d
        else:
            dtype = [('f0', numpy.dtype(dtype)),]
        object.__setattr__(self, '_dtype', numpy.dtype(dtype))
        object.__setattr__(self, '_shape', shape)
        object.__setattr__(self, '_data', {})
        object.__setattr__(self, '_locked', True)
        object.__setattr__(self, '_scalar', None)
        object.__setattr__(self, '_order', order)
        object.__setattr__(self, '_keys', numpy.dtype(dtype).names)
        for key in self._keys:
            self._data[key] = numpy.empty(shape=shape,
                                          dtype=self._dtype[key],
                                          order=order)
            if fill is not None:
                if type(fill) in [bool,int,float]:
                    self._data[key][...] = fill
                elif type(fill) is numpy.ndarray:
                    self._data[key][...] = fill[key] 
        if type(fill) in [tuple, list]:
            self[...] = fill


    # def item(self):
    #     '''
    #     Copy the first element of group to a standard Python scalar and return
    #     it. The group must be of size one.
    #     '''
    #     return self._data[self._data.keys()[0]]

    def reshape(self, shape):
        '''
        Gives a new shape to the group without changing its data.

        Parameters
        ----------
        shape : {tuple, int}
            The new shape should be compatible with the original shape. If
            an integer, then the result will be a 1-D group of that length.
            One shape dimension can be -1. In this case, the value is inferred
            from the length of the array and remaining dimensions.

        Returns
        -------
        reshaped_group : group
            This will be a new view object if possible; otherwise, it will
            be a copy.

        Examples
        --------
        >>> g = group([[1,2,3], [4,5,6]])
        >>> g.reshape(6)
        group([1, 2, 3, 4, 5, 6])
        '''
        G = group(shape=(), dtype=self.dtype)
        for key in G._keys:
            G._data[key] = self._data[key].reshape(shape)
        G._shape = shape
        return G

    def lock(self):
        '''
        Locks group.

        Fields cannot be created or deleted anymore.
        '''
        self._locked = True

    def unlock(self):
        '''
        UnLocks group.

        Fields can be created or deleted on the fly.
        '''
        self._locked = False

    def __len__(self):
        ''' x.__len__() <==> len(x) '''
        if self.shape: return self.shape[0]
        raise TypeError, 'len() of unsized object'

    def __getattr__(self, key):
        if key in self._keys:
            return self._data[key]
        else:
            return object.__getattribute__(self, key)

    def __setattr__(self, key, value):
        if key in self._keys:
            self._data[key][...] = value
        else:
            object.__setattr__(self, key, value)

    def _get_shape(self):
        return self._shape

    def _set_shape(self, shape):
        for key in self._dtype.names:            
            self._data[key].shape = shape
        self._shape = shape
    shape = property(_get_shape, _set_shape,
                     doc='''Tuple of group dimensions.''')

    def _get_size(self):
        return self._data.values()[0].size
    size = property(_get_size,
                    doc = '''Number of elements in the group.''')

    def _get_dtype(self):
        return self._dtype
    dtype = property(_get_dtype,
                     doc='''Data-type for the group.''')

    def __getitem__(self, key):
        if type(key) is str:
            if key in self._keys:
                return self._data[key]
            else:
                raise ValueError, 'field named %s not found' % key
        elif type(key) in [int, slice, tuple]:
            shape = self._data.values()[0][key].shape
            if shape is not ():
                G = group(shape, self._dtype)
                for name in self._dtype.names:
                    G._data[name] = self._data[name][key]
                return G
            elif len(self._data) == 1:
                return self._data.values()[0][key]
            else:
                return tuple(self._data[k][key] for k in self._keys)

        elif key is Ellipsis:
            return self
        elif not len(self._shape):
            if key is Ellipsis:
                return self
            if type(key) is str:
                raise ValueError, 'field named %s not found' % key
            elif type(key) is slice:
                raise ValueError, 'cannot slice a 0-d group'
            elif type(key) is tuple:
                raise IndexError, \
                    '''0-d groups can only use a single () or a ''' \
                    '''list of newaxes (and a single ...) as an index'''
            else:
                raise IndexError, "0-d groups can't be indexed"

        raise IndexError, 'index must be either an int or a sequence'

    def __setitem__(self, key, value):
        if type(key) is str:
            if key in self._keys:
                self._data[key][...] = value
                return
            else:
                if self._locked:
                    raise ValueError, \
                        "field named '%s' not found and group is locked" % key
                else:
                    if type(value) in [int, float, bool]:
                        Z = numpy.ones(shape=self._shape, dtype=type(value), order=self._order)*value
                        self._data[key] = Z
                        dtype = [(name,self.dtype[i]) for i, name in enumerate(self.dtype.names)]
                        dtype.append((key,Z.dtype))
                        self._dtype = numpy.dtype(dtype)
                        self._keys = numpy.dtype(dtype).names
                        return
                    elif type(value) is numpy.ndarray:
                        if value.size == self.size and value.dtype.names == None:
                            self._data[key] = value.reshape(self.shape)
                            dtype = [(name,self.dtype[i]) for i, name in enumerate(self.dtype.names)]
                            dtype.append((key,value.dtype))
                            self._dtype = numpy.dtype(dtype)
                            self._keys = numpy.dtype(dtype).names                        
                            return
                        elif value.dtype.names is not None:
                            raise ValueError, \
                                "Data cannot be a record array"
                        else:
                            raise ValueError, \
                                "Data size must match group size"
                    else:
                        raise ValueError, \
                            "Data-type not understood"                        
        elif type(key) in [int, slice, tuple] or key is Ellipsis:
            if key is Ellipsis:
                G = self
            else:
                G = self.__getitem__(key)
            if type(G) is group:
                if type(value) in [bool,int,float]:
                    for k in self._keys:
                        G._data[k][...] = value
                    return
                elif type(value) in [tuple,list]:
                    if len(value) == len(self._keys):
                        for i,k in enumerate(self._keys):
                            G._data[k][...] = value[i]
                        return
                    else:
                        raise ValueError, \
                            'size of tuple must match number of fields.'
                else:
                    raise ValueError, \
                        "Data type not understood"
            elif type(G) is tuple:
                if type(value) in [bool,int,float]:
                    for k in self._keys:
                        self._data[k][key] = value
                    return
                elif type(value) is tuple:
                    if len(value) == len(self._keys):
                        for i,k in enumerate(self._keys):
                            self._data[k][key] = value[i]
                        return
                    else:
                        raise ValueError, \
                            'size of tuple must match number of fields.'
        raise IndexError, 'index must be either an int or a sequence'
 
    def __delitem__(self, key):
        if type(key) is not str:
            raise ValueError, 'key must be a string'
        if self._locked:
            raise ValueError, 'group is locked'
        if key not in self._keys:
            raise ValueError, \
                "field named '%s' does not exist" % key
        del self._data[key]        
        dtype= []
        for i, name in enumerate(self.dtype.names):
            if name != key:
                dtype.append((name,self.dtype[i]))
        self._dtype = numpy.dtype(dtype)
        self._keys = numpy.dtype(dtype).names

    def asarray(self):
        ''' Return a ndarray copy of this group '''
        return numpy.array(self, dtype=self.dtype)

    def __str__(self):
        ''' x.__str__() <==> str(x) '''
        return numpy.array_str(self)

    def __repr__(self):
        ''' x.__repr__() <==> repr(x) '''
        return numpy.array_repr(self)

def empty(shape, dtype=float, order='C'):
    '''
    Return a new group of given shape and type, without initialising entries.

    Parameters
    ----------
    shape : {tuple of ints, int}
        Shape of the new group, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the group, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.
    
    Returns
    -------
    out : group
        Group with the given shape, dtype, and order.

    See also
    --------
    * :meth:`group.zeros` : Return a new group setting values to zero.
    * :meth:`group.ones` : Return a new group setting values to one.
    * :meth:`group.zeros_like` : Return a group of zeros with shape and type of input.
    * :meth:`group.ones_like` : Return a group of ones with shape and type of input.
    * :meth:`group.empty_like` : Return a empty group with shape and type of input.

    Notes
    -----
    `empty`, unlike `zeros`, does not set the group values to zero, and may
    therefore be marginally faster.  On the other hand, it requires the user
    to manually set all the values in the group, and should be used with
    caution.

    Examples
    --------
    >>> group.empty((2,2))
    group([[6.94248367807e-310, 1.34841898023e-316],
           [1.34841977073e-316, 0.0]], 
          dtype=[('f0', '<f8')])
    '''
    return group(shape=shape, dtype=dtype, order=order, fill=None)

def zeros(shape, dtype=float, order='C'):
    '''
    Return a new group of given shape and type, filled with zeros.

    Parameters
    ----------
    shape : {tuple of ints, int}
        Shape of the new group, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the group, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.
    
    Returns
    -------
    out : group
        Group with the given shape, dtype, and order, filled with zeros.

    See also
    --------
    * :meth:`group.ones` : Return a new group setting values to one.
    * :meth:`group.empty` : Return a new uninitialized group.
    * :meth:`group.zeros_like` : Return an group of zeros with shape and type of input.
    * :meth:`group.ones_like` : Return an group of ones with shape and type of input.
    * :meth:`group.empty_like` : Return an empty group with shape and type of input.

    Examples
    --------
    >>> group.zeros((2,2))
    group([[0.0, 0.0],
           [0.0, 0.0]], 
          dtype=[('f0', '<f8')])
    >>> group.zeros((2,2), dtype=int)
    group([[0, 0],
           [0, 0]], 
          dtype=[('f0', '<f8')])
    '''
    return group(shape=shape, dtype=dtype, order=order, fill=0)

def ones(shape, dtype=float, order='C'):
    '''
    Return a new group of given shape and type, filled with ones.

    Parameters
    ----------
    shape : {tuple of ints, int}
        Shape of the new group, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the group, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.
    
    Returns
    -------
    out : group
        Group with the given shape, dtype, and order, filled with ones.

    See also
    --------
    * :meth:`group.zeros` : Return a new group setting values to zero.
    * :meth:`group.empty` : Return a new uninitialized group.
    * :meth:`group.zeros_like` : Return an group of zeros with shape and type of input.
    * :meth:`group.ones_like` : Return an group of ones with shape and type of input.
    * :meth:`group.empty_like` : Return an empty group with shape and type of input.

    Examples
    --------
    >>> group.ones((2,2))
    group([[1.0, 1.0],
           [1.0, 1.0]], 
          dtype=[('f0', '<f8')])
    >>> group.ones((2,2), dtype=int)
    group([[1, 1],
           [1, 1]], 
          dtype=[('f0', '<f8')])
    '''
    return group(shape=shape, dtype=dtype, order=order, fill=1)

def empty_like(other):
    ''' 
    Create a new group with the same shape and type as another.

    Parameters
    ----------
    other : array_like
        The shape and data-type of `other` defines the parameters of the
        returned group.

    Returns
    -------
    out : group
        Unintialized group with same shape and type as `other`.

    See also
    --------
    * :meth:`group.zeros` : Return a new group setting values to zero.
    * :meth:`group.ones` : Return a new group setting values to one.
    * :meth:`group.empty` : Return a new uninitialized group.
    * :meth:`group.ones_like` : Return a group of ones with shape and type of input.
    * :meth:`group.zeros_like` : Return a group of zeros with shape and type of input.

    Examples
    --------
    >>> x = np.arange(6)
    >>> x = x.reshape((2, 3))
    >>> x
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> np.zeros_like(x)
    array([[0, 0, 0],
           [0, 0, 0]])
    '''
    return group(shape=other.shape, dtype=other.dtype, fill=None)

def zeros_like(other):
    ''' 
    Create a new group of zeros with the same shape and type as another.

    Parameters
    ----------
    other : array_like
        The shape and data-type of `other` defines the parameters of the
        returned group.

    Returns
    -------
    out : group
        Group of zeros with same shape and type as `other`.

    See also
    --------
    * :meth:`group.zeros` : Return a new group setting values to zero.
    * :meth:`group.ones` : Return a new group setting values to one.
    * :meth:`group.empty` : Return a new uninitialized group.
    * :meth:`group.empty_like` : Return an uninitialized group shape and type of input.
    * :meth:`group.ones_like` : Return a group of ones with shape and type of input.

    Examples
    --------
    >>> x = np.arange(6)
    >>> x = x.reshape((2, 3))
    >>> x
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> np.zeros_like(x)
    array([[0, 0, 0],
           [0, 0, 0]])
    '''
    return group(shape=other.shape, dtype=other.dtype, fill=0)

def ones_like(other):
    '''
    Returns a group of ones with the same shape and type as a given array.

    Parameters
    ----------
    other : group_like
        The shape and data-type of other defines the parameters of the
        returned group.

    Returns
    -------
    out : group
        Group of ones with same shape and type as other.

    See also
    --------
    * :meth:`group.zeros` : Return a new group setting values to zero.
    * :meth:`group.ones` : Return a new group setting values to one.
    * :meth:`group.empty` : Return a new uninitialized group.
    * :meth:`group.empty_like` : Return an empty group with shape and type of input.
    * :meth:`group.zeros_like` : Return a group of zeros with shape and type of input.

    Examples
    --------
    >>> x = np.arange(6)
    >>> x = x.reshape((2, 3))
    >>> x
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> zeros_like(x)
    group([[0, 0, 0],
           [0, 0, 0]])
    '''
    return group(shape=other, dtype=other.dtype, fill=1)


if __name__ == '__main__':
    
    G = zeros((3,3), dtype=[('x',float), ('y', float)])
    print G

    
