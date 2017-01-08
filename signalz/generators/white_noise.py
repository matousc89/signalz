"""
.. versionadded:: 0.1

This function generates white noise series. This function uses
`numpy.random.normal`.

Function Documentation
======================================
"""
import numpy as np

def white_noise(n, offset=0, std=1):
    """
    Random values with normal distribution.

    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**

    * `offset` - mean value (float)
         
    * `std` - standard deviation (float)
    
    **Returns:**
    
    * vector of random values (1d array)   
    """
    return np.random.normal(offset, std, n)
