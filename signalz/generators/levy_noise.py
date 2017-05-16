"""
.. versionadded:: 0.5

This function generates random variable with Levy alpha-stable distribution
(also reffered just as stable distribution).

The Levy distribution is defined by two parameters :math:`\\alpha`
and :math:`\\beta`. The Gaussian distribution is special case of 
Levy distribution with :math:`\\alpha=2` and :math:`\\beta=0`.

Notes about Implementation
==============================
The implemented algorithm is known as Chambers-Mallows-Stuck method
:cite:`weron1996chambers`. Using two random variables (one with exponential
distribution and one with uniform distribution). The input random variables
are obtained with `numpy.random.exponentinal` and `numpy.random.uniform`.

Example Usage
==================

The following example produce 1000 samples of Levy noise located (mean value)
at -2 (`position`), with characteristic exponent index of 1.5 (`alpha`),
skeewness of 1 (`beta`) and diffusion of 1. (`sigma`).

.. code-block:: python

    import signalz
    x = signalz.levy_noise(1000, alpha=1.5, beta=0.5, sigma=1., position=-2)

References
============

.. bibliography:: levy_noise.bib
    :style: plain

Function Documentation
======================================
"""
import numpy as np

from signalz.misc import check_type_or_raise

def levy_noise(n, alpha=2., beta=1., sigma=1., position=0.):
    """
    This function produces Levy noise.
    
    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output
    
    **Kwargs:**
    
    * `alpha` - characteristic exponent index (float) in range `0<alpha<2`
      
    * `beta` - skeewness (float) in range `-1<beta<1`

    * `sigma` - diffusion (float), in case of gaussian distribution it is
      standard deviation

    * `position` - position parameter (float)
    
    **Returns:**
    
    * vector of values representing the noise (1d array)
    """
    # correct the inputs or throw error
    alpha = float(alpha)
    beta = float(beta)
    check_type_or_raise(n, int, "n")
    if not 0. <= alpha <= 2.:
        raise ValueError("Alpha must be between 0 and 2")
    if not -1. <= beta <= 1.:
        raise ValueError("Beta must be between -1 and 1")
    # generate random variables
    v = np.random.uniform(-0.5 * np.pi, 0.5 * np.pi, n)
    w = np.random.exponential(1, n)
    # convert random variables to levy noise
    if alpha == 1.:
        arg1 = (0.5 * np.pi) + (beta * v)
        arg2 = w * np.cos(v)
        arg3 = 0.5 * np.pi * beta * sigma + np.log(sigma)
        x = 2 / np.pi * (arg1 * np.tan(v) - (beta * np.log(arg2 / arg1)))
        return (sigma * x) + arg3 + position
    else:
        arg1 = 0.5 * np.pi * alpha
        b_ab = np.arctan(beta * np.tan(arg1)) / alpha
        s_ab = (1 + (beta**2) * np.tan(arg1)**2)**(1/(2.*alpha))
        arg2 = alpha * (v + b_ab)
        n1 = np.sin(arg2)
        d1 = np.cos(v)**(1/alpha)
        n2 = np.cos(v - arg2)
        x = s_ab * (n1/d1) * (n2/w)**((1-alpha)/alpha)
        return (sigma * x) + position
