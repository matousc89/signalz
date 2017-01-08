"""
.. versionadded:: 0.1

This function generates data as autoregressive model (AR model) according to
following equation 

:math:`x(k) = c + \sum\limits_{n=1}^{\infty} a_{i} x(k-i) + v(k)`,

where :math:`k` is discrete time index, :math:`c` is an constant, 
:math:`a_i` is parameters of model and :math:`v(k)` is noise.

The AR model is also known as stochastic difference equation.

Example Usage
==================

Let us consider AR model as follows

:math:`x(k) = 1.79 x(k-1) - 1.85 x(k-2) + 1.27 x(k-3) - 0.41 x(k-4) + v(k)`.

This AR can be simulated with following code (1000 samples)

.. code-block:: python

    # AR model parameters
    a = [-0.41, 1.27, -1.85, 1.79]

    # number of samples
    N = 1000
    
    # get AR data
    x = signalz.autoregressive_model(N, a, noise="white")

Function Documentation
======================================
"""
import numpy as np
from signalz.generators.white_noise import white_noise
    
def autoregressive_model(n, a, const=0, noise="white", initials="none"):
    """
    Autoregressive model (stochastic difference equation)
    
    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    * `a` - coefficients of the model (1d array), 
    
    **Kwargs:**

    * `const` - constant of the model (float), default is 0
    
    * `noise` - model input (str or 1d array), default is "white",
      possible options are:
        
      * `"white"` - input noise has zero mean value and unit standard deviation
        
      * `"none"` - input noise are zeros
        
      * manually created array of inputs of length `n` 
         
    * `initials` - initial values (1d array) of the same size as `a`
    
    **Returns:**
    
    * `x` - output of the AR model (1d array)    
    """
    taps = len(a)
    if type(noise) == str:
        if noise == "none":
            noise = np.zeros(n)
        if noise == "white":
            noise = white_noise(n)
    x = np.zeros(n)
    # handle initials 
    if initials == "random":
        x[:taps] = white_noise(taps)
    elif initials == "none":
        pass   
    else:
        if not len(a) == len(initials):
            raise ValueError('The length of initials values and a must agree.')
        x[:taps] = initials
    # simulate system
    for k in range(taps,n-1):
        x[k+1] = const + np.dot(a, x[k+1-taps:k+1]) + noise[k+1]
    return x     


