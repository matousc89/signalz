"""
.. versionadded:: 0.4

This function generates Brownian noise series. The noise is produced by
integration of white noise (gaussian or uniform).

This function uses
`numpy.random.normal` and `numpy.random.uniform`

Example Usage
==================

The following example produce 1000 samples of brownian noise starting in
value 10 (`start=10`). The noise is produced by integration of white gaussian
noise (`source="gaussian"`) with standard deviation of 1 (`std=1`).
To keep in noise in some reasonable range,
it is used 10% leaky integration (`leak=0.1`).

.. code-block:: python

    import signalz
    x = signalz.brownian_noise(1000, leak=0.1, start=10, std=1, source="gaussian")

Function Documentation
======================================
"""
import numpy as np

from signalz.misc import check_type_or_raise
from signalz.generators.gaussian_white_noise import gaussian_white_noise
from signalz.generators.uniform_white_noise import uniform_white_noise

def brownian_noise(n, leak=0., start=0, std=1., source="gaussian"):
    """
    This function produces Browninan noise.

    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**
    
    * `leak` - leakage during integration (float), this should prevent signal
      from wander off. Possible value is `0 <= leak < 1`
      
    * `start` - offset on the start (float)

    * `std` - standard deviation of source white noise (float), in case of
      uniform distribution it is the difference between min and max value. 
    
    * `source` - distribution of source white noise (str). Options are
      `gaussian` or `uniform`
    
    **Returns:**
    
    * vector of values representing the noise (1d array)
    """
    # check inputs
    check_type_or_raise(n, int, "n")
    check_type_or_raise(leak, float, "leak")
    if not 0. <= leak < 1:
        raise ValueError("Leak must be between 0. and 1.")
    # generate white noise
    if source == "gaussian":
        x = np.random.normal(0, std, n)
    elif source == "uniform":
        x = np.random.uniform(-std/2., std/2., n)
    else:
        raise ValueError("Source must be gaussian or uniform")
    # add offset
    x[0] = start
    # integrate the white noise    
    for i in range(1,n):
        x[i] += x[i-1]*(1-leak)
    return x
