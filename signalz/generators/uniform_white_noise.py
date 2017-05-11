"""
.. versionadded:: 0.4

This function generates Uniform white noise series. This function uses
`numpy.random.uniform`.

Function Documentation
======================================
"""
import numpy as np

def uniform_white_noise(n, minimum=-1, maximum=1):
    """
    Random values with uniform distribution.

    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**

    * `minimum` - minimal value (float)
         
    * `maximum` - maximal value (float)
    
    **Returns:**
    
    * vector of values representing the noise (1d array)   
    """
    return np.random.uniform(low=minimum, high=maximum, size=n)
