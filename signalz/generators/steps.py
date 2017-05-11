"""
.. versionadded:: 0.2
.. versionchanged:: 0.4

This function generates steps according to given sequence of values and
given width of steps. Function also can repeat given
sequence according required number of repeats, or desired lenght of data.

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

from signalz.misc import check_type_or_raise

def steps(step_width, values, repeat=1, size=None):
    """
    This function generates steps from given values.
    
    **Args:**
    
    * `step_width` - desired width of every step (int)
    
    * `values` - values for steps (1d array) 
    
    **Kwargs:**
         
    * `repeat` - number of step sequence repetions (int), this variable is used,
      if the `size` is not defined
    
    * `size` - size of output data in samples (int), if the `size` is used,
      the `repeat` is ignored.
    
    **Returns:**
    
    * array of values representing desired steps (1d array)
    """
    check_type_or_raise(step_width, int, "step width")
    check_type_or_raise(repeat, int, "repeat")
    try:
        values = np.array(values)
    except:
        raise ValueError('Values must be a numpy array or similar.') 
    # generate steps
    x = np.repeat(values, step_width)          
    if size is None:
        # repeat according to the desired repetions
        x_full = np.tile(x, repeat)      
    else:
        check_type_or_raise(size, int, "size")
        # repeat till size is reached and crop the data to match size
        repeat = int(np.ceil(size / float(len(x))))
        x_full = np.tile(x, repeat)[:size]
    return x_full





