"""
.. versionadded:: 0.5

This function generates Levy walk by interpolation of Levy flight.

The Levy distribution is defined by two parameters :math:`\\alpha`
and :math:`\\beta`. The Gaussian distribution is special case of 
Levy distribution with :math:`\\alpha=2` and :math:`\\beta=0`.

This function uses :ref:`generators-levy_noise`.

Example Usage
==================

The following example produce 1000 samples of Levy walk created from
500 samples of Levy noise (`ns=500`) located (mean value) at 0 (`position`),
with characteristic exponent index of 1.4 (`alpha`),
skeewness of 0 (`beta`) and diffusion of 1. (`sigma`). 


.. code-block:: python

    import signalz
    x = signalz.levy_walk(1000, ns=500, alpha=1.4, beta=0., sigma=1., position=0)

Function Documentation
======================================
"""
import numpy as np

from signalz.misc import check_type_or_raise
import signalz

def levy_walk(n, ns=0, alpha=2., beta=1., sigma=1., position=0.):
    """
    This function produces Levy walk.
    
    **Args:**
    
    * `n` - length of the output data (int) -
      how many samples will be on output
    
    * `ns` - number of points (int) in original noise before interpolation,
      this number cannot be higher than desired length of data;
      if it is set to 0, then `ns=n` is used; this number is related to number
      of direction changes in resulting walk
    
    **Kwargs:**
    
    * `alpha` - characteristic exponent index of used Levy noise
      (float) in range `0<alpha<2`
      
    * `beta` - skeewness of used Levy noise (float) in range `-1<beta<1`

    * `sigma` - diffusion of used Levy noise (float);
      in case of gaussian distribution it is
      standard deviation

    * `position` - position parameter (float) of used Levy noise
    
    **Returns:**
    
    * vector of values representing the walk (1d array)
    """
    # check params
    check_type_or_raise(ns, int, "ns")
    check_type_or_raise(n, int, "n")
    if ns == 0:
        ns = n
    elif ns > n:
        raise ValueError("Argument ns cannot be higher than argument n")
    # generate levy random variable
    x = signalz.levy_noise(ns, alpha, beta, sigma, position)
    # interpolate new points
    xt = np.cumsum(np.abs(x))  
    xf = np.cumsum(x)
    t = np.linspace(0, xt[-1], n)
    return np.interp(t, xt, xf)
        
        

