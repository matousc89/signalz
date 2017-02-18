"""
.. versionadded:: 0.2

This function generates steps according to given sequence of values and
given width of steps. Function also can repeat given
sequence of steps.

Example Usage
==================

Usage is as simple as

.. code-block:: python

    import signalz
    x = signalz.steps(2, [1, 2, 3], repeat=2)
    
where the `2` stands for step width, `[1, 2, 3]` are values for steps and
`repeat=2` make the sequence of steps repeat twice. So the returned output is

>>> [1 1 2 2 3 3 1 1 2 2 3 3]


Function Documentation
======================================
"""
import numpy as np
import matplotlib.pylab as plt

def steps(step_width, values, repeat=1):
    """
    This function generates steps from given values.
    
    **Args:**
    
    * `step_width` - desired width of every step (int)
    
    * `values` - values for steps (1d array) 
    
    **Kwargs:**
         
    * `repeat` - number of step sequence repetions (int)
    
    **Returns:**
    
    * `x` - array of values describing desired steps (1d array)
    """
    try:
        step_width = int(step_width)
    except:
        raise ValueError('Step widht must be an int.') 
    try:
        repeat = int(repeat)
    except:
        raise ValueError('Repeat arg must be an int.') 
    try:
        values = np.array(values)
    except:
        raise ValueError('Values must be a numpy array or similar.') 
    # generate steps
    x = np.repeat(values, step_width)  
    # repeat if needed  
    x = np.tile(x, repeat)
    return x





