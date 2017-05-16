"""
.. versionadded:: 0.2
.. versionchanged:: 0.4

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
    x = signalz.random_steps(50, steps_count=10, distribution="normal", std=30, mean=-10)
    
Another example, this time the size of the data is not requested by number of
steps, but by number of samples (`size=500`). 

.. code-block:: python

    import signalz
    x = signalz.random_steps(50, size=500)

Function Documentation
======================================
"""
import numpy as np

from signalz.misc import check_type_or_raise
import signalz

def random_steps(step_width, steps_count=10, size=None, distribution="normal",
    maximum=1, minimum=0, std=1, mean=0):
    """
    This function generates random steps.
    
    **Args:**
    
    * `step_width` - desired width of every step (int)
       
    **Kwargs:**
    
    * `steps_count` - desired number steps (int), this variable is used,
      if the `size` is not defined
    
    * `size` - lenght of desired output in samples (int),
      if this variable is defined,
      it determines the size of data instead of `steps_count`
             
    * `distribution` - distribution of random numbers (str), Options are
      `normal` and `uniform`.
      
    * `maximum` - maximal value for steps (float), this value is used
      in case of uniform distribution.
    
    * `minimum` - minimal value for steps (float), this value is used
      in case of uniform distribution.
    
    * `std` - standard deviation of random variable (float), this value
      is used in case of gaussian (normal) distribution.
      
    * `mean` - mean value of random variable (float), this value
      is used in case of gaussian (normal) distribution.
    
    **Returns:**
    
    * vector of values representing desired steps (1d array)
    """ 
    # check values
    check_type_or_raise(steps_count, int, "steps count")
    check_type_or_raise(step_width, int, "step width")
    # get correct number of steps if size is defined
    if not size is None:
        check_type_or_raise(size, int, "size")
        steps_count = int(np.ceil(size / float(step_width)))
    # generate random values
    if distribution in ["normal", "gaussian"]:
        values = signalz.gaussian_white_noise(steps_count, offset=mean, std=std)   
    elif distribution == "uniform":
        values = signalz.uniform_white_noise(steps_count, minimum=minimum,
            maximum=maximum)
    # generate steps
    x = signalz.steps(step_width, values)
    if size is None:
        return x
    else:
        return x[:size]
        
