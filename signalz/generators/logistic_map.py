"""
.. versionadded:: 0.3

This function simulates logistic map equation. This logisti map is described
by following equation

:math:`x(k+1) = r x(k) (1 - x(k))`,

where :math:`x` is population (between 0 and 1) and :math:`x` is parameter
denoted as value of interest.

The logistic map can result in logistic behaviour for some values of :math:`r`.

For more information see great page about
`logistic map on Wikipedia <https://en.wikipedia.org/wiki/Logistic_map>`_

Example Usage
===============

Simple example

.. code-block:: python

    N = 200 # number of samples
    x = signalz.logistic_map(N, r=3)

Function Documentation
======================================
"""
import numpy as np

def logistic_map(n, r=4, initial=0.5):
    """
    Logist map equation

    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**
    
    * `r` - function parameter (float)
    
    * `initial` - initial value (float), default is 0.1,
      should be in range from 0 to 1
    
    **Returns:**
    
    * simulation output - vector of numbers between 0 and 1
    """
    x = np.zeros(n)
    x[0] = initial
    for k in range(n-1):
        x[k+1] = r*x[k]*(1-x[k])
    return x


