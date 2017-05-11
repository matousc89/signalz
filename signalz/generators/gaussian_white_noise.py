"""
.. versionadded:: 0.1
.. versionchanged:: 0.4

This function generates Gaussian white noise series. This function uses
`numpy.random.normal`.

Function Documentation
======================================
"""
import numpy as np

def gaussian_white_noise(n, offset=0, std=1):
    """
    Random values with normal distribution.

    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**

    * `offset` - mean value (float)
         
    * `std` - standard deviation (float)
    
    **Returns:**
    
    * vector of values representing the noise (1d array)   
    """
    return np.random.normal(offset, std, n)
