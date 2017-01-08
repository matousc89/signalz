"""
.. versionadded:: 0.1

This function generates sinus waves with given period, amplitude and offset.
It is also possible to use delay defined in samples to crop the first wave.

Example Usage
===============

Simple example

.. code-block:: python

    N = 200 # number of samples
    x = signalz.sinus(N)

Function Documentation
======================================
"""
import numpy as np

def sinus(n, period=100, amplitude=2, offset=0, delay=0):
    """
    Sinus waves generator.

    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**
    
    * `period` - length of one sinus wave period (1 / frequency)
    
    * `amplitude` - difference between minimal and maximal value of waves 

    * `offset` - mean value (float)
         
    * `delay` - how many samples should be croped from first wave (does not
      influence full length of data)
    
    **Returns:**
    
    * vector of sinus waves (1d array)   
    """
    t = np.arange(n) + delay
    return np.sin(t*2*np.pi/100.)*0.5*amplitude + offset


