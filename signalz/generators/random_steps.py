"""
.. versionadded:: 0.2

This function generates random steps according to given width of steps and
desired number of steps.

Example Usage
==================

Simplest example (10 steps with width 50 samples, normal distribution
with unit standard deviation and zero mean) follows.

.. code-block:: python

    import signalz
    x = signalz.random_steps(50, 10)
       
More complicated example with normal distribution (standard deviation and
mean value is changed) follows.

.. code-block:: python

    import signalz
    x = signalz.random_steps(50, 10, distribution="normal", std=30, mean=-10)
    
Another example, this time with uniform distribution - values in range from 10
to 20.

.. code-block:: python

    import signalz
    x = signalz.random_steps(50, 10, distribution="uniform", minimum=10, maximum=20)

Function Documentation
======================================
"""
import numpy as np
import matplotlib.pylab as plt

import signalz

def random_steps(steps_count, step_width, distribution="normal", maximum=1,
    minimum=0, std=1, mean=0):
    """
    This function generates random steps.
    
    **Args:**
    
    * `steps_count` - desired number steps (int)
    
    * `step_width` - desired width of every step (int)
    
    **Kwargs:**
         
    * `repeat` - number of step sequence repetions (int)
    
    * `distribution` - distribution of random numbers (str), Options are
      `normal` and `uniform`.
      
    * `maximum` - maximal value for steps (float), this value is used
      in case of uniform distribution.
    
    * `minimum` - minimal value for steps (float), this value is used
      in case of uniform distribution.
    
    * `std` - standard deviation of random variable (float), this value
      is used in case of normal distribution.
      
    * `mean` - mean value of random variable (float), this value
      is used in case of normal distribution.
    
    **Returns:**
    
    * `x` - array of values describing desired steps (1d array)
    """ 
    # generate values
    values = False
    if distribution == "normal":
        values = np.random.normal(mean, std, 10)    
    elif distribution == "uniform":
        values = np.random.random(steps_count) * float(maximum-minimum)
        values = values + minimum
    # generate steps
    x = signalz.steps(step_width, values)
    return x
