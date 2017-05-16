"""
.. versionadded:: 0.5

This function generates Levy flight by integration of Levy
alpha-stable distribution (also reffered just as stable distribution).

The Levy distribution is defined by two parameters :math:`\\alpha`
and :math:`\\beta`. The Gaussian distribution is special case of 
Levy distribution with :math:`\\alpha=2` and :math:`\\beta=0`.
In case of Gaussian distribution the Levy flight is Brownian walk.

This function uses :ref:`generators-levy_noise`.

Example Usage
==================

The following example produce 500 samples of Levy flight produced from
Levy noise located (mean value) at 0 (`position`),
with characteristic exponent index of 1.8 (`alpha`),
skeewness of 0 (`beta`) and diffusion of 1. (`sigma`).

.. code-block:: python

    import signalz
    x = signalz.levy_flight(500, alpha=1.8, beta=0., sigma=1., position=0)

Function Documentation
======================================
"""
import numpy as np

import signalz

def levy_flight(n, alpha=2., beta=1., sigma=1., position=0.):
    """
    This function produces Levy flight.
    
    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**
    
    * `alpha` - characteristic exponent index of used Levy noise
      (float) in range `0<alpha<2`
      
    * `beta` - skeewness of used Levy noise (float) in range `-1<beta<1`

    * `sigma` - diffusion of used Levy noise (float),
      in case of gaussian distribution it is
      standard deviation

    * `position` - position parameter (float) of used Levy noise
    
    **Returns:**
    
    * vector of values representing the flight (1d array)
    """
    x = signalz.levy_noise(n, alpha, beta, sigma, position)
    return np.cumsum(x)  
        
        

