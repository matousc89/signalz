"""
.. versionadded:: 0.2

This function generates cosinus waves with given period, amplitude and offset.
It is also possible to use delay defined in samples to crop the first wave.

Example Usage
===============

Simple example

.. code-block:: python

    N = 200 # number of samples
    x = signalz.cosinus(N)

Function Documentation
======================================
"""
import numpy as np

import signalz

def cosinus(n, period=100, amplitude=2, offset=0, delay=0):
    """
    Cosinus waves generator.

    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**
    
    * `period` - length of one sinus wave period (1 / frequency)
    
    * `amplitude` - difference between minimal and maximal value of waves 

    * `offset` - mean value (float)
         
    * `delay` - how many samples should be croped from first wave (does not
      influence full length of data)
    
    **Returns:**
    
    * vector of cosinus waves (1d array)   
    """
    delay += period/4.
    return signalz.sinus(n, period, amplitude, offset, delay)



