"""
.. versionadded:: 0.1
.. versionchanged:: 0.2

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

This AR can be simulated with following code (1000 samples).

.. code-block:: python

    import signalz

    # AR model parameters
    a = [-0.41, 1.27, -1.85, 1.79]

    # number of samples
    N = 1000
    
    # get AR data
    x = signalz.autoregressive_model(N, a, noise="white")

The next example shows, how to introduce parameter changes during the data
generation.
    
.. code-block:: python

    import signalz

    # number of samples
    N = 1000

    # AM model default parameters
    a = [-0.41, 1.27, -1.85, 1.79]

    # parameters for all samples
    A = np.ones((N,4))
    A = A*a

    # change of parameters starting from time index 500
    A[500:] = a + np.array([0.01, 0.02, 0.01, -0.02])

    # get AR data
    x = signalz.autoregressive_model(N, A, noise="white")
    

Function Documentation
======================================
"""
import numpy as np
from signalz.generators.gaussian_white_noise import gaussian_white_noise

import signalz
    
def autoregressive_model(n, a, const=0, noise="white", initials="none"):
    """
    Autoregressive model (stochastic difference equation)
    
    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    * `a` - coefficients of the model (1d array, 2d array), in case of a vector
      are used the same parameters for whole generation. In case of a matrix,
      every row represents parameters for one time sample.
    
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
    a = np.array(a)
    taps = a.shape[-1]
    a = signalz.matrixize_input(a, n)
    # handle noise
    if type(noise) == str:
        if noise == "none":
            noise = np.zeros(n)
        elif noise == "white":
            noise = gaussian_white_noise(n)
    else:
        try:
            noise = np.array(noise)
        except:
            raise ValueError('Noise is not numpy array or similar.')
        if not len(noise) == n:
            raise ValueError('Noise array is not same length as n.')
    x = np.zeros(n)
    # handle initials
    if type(initials) == str:
        if initials == "random":
            x[:taps] = gaussian_white_noise(taps)
        elif initials == "none":
            pass
    else:
        x[:taps] = initials
    # simulate system
    for k in range(taps,n-1):
        x[k+1] = const + np.dot(a[k], x[k+1-taps:k+1]) + noise[k+1]
    return x  
    


