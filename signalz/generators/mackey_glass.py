"""
.. versionadded:: 0.1
.. versionchanged:: 0.2

This function generates data according a discrete realization of Mackey-Glass 
equation as follows

:math:`x_{k+1} = c \cdot x_k + \\frac{\large{a \cdot x_{k-d}}}{b + x^{e}_{k-d}}`

The original Mackey-Glass equation :cite:`glass2010mackey` is the nonlinear
time delay differential equation.

Example Usage
===============

In this example is simulated 1000 samples with arguments that cause
chaotic behaviour.

.. code-block:: python

    N = 1000
    x = signalz.mackey_glass(N, a=0.2, b=0.8, c=0.9, d=23, e=10, initial=0.1)
    
The parameters  `a`, `b`, `c`, `d`, `e` can be a scalar or a vector. In case
of a vector, every item represents parameter for one sample.

References
============

.. bibliography:: mackey_glass.bib
    :style: plain

Function Documentation
======================================
"""
import numpy as np

import signalz

def mackey_glass(n, a=0.2, b=0.8, c=0.9, d=23, e=10, initial=0.1):
    """
    Mackey-Glass discrete equation.
    
    **Args:**
    
    * `n` - length of the output data (int) - how many samples will be on output

    **Kwargs:**
    
    Parameters  `a`, `b`, `c`, `d`, `e` can be a scalar or a vector. In case
    of a vector, every item represents parameter for one sample.

    * `a` - parameter of the model (float, 1d array), default is 0.2
    
    * `b` - parameter of the model (float, 1d array), default is 0.8
    
    * `c` - parameter of the model (float, 1d array), default is 0.9
    
    * `d` - time delay of the model (int, 1d array), default is 23
    
    * `e` - parameter of the model (float, 1d array), default is 10
    
    * `initial` - initial value (float), default is 0.1
    
    **Returns:**
    
    * `x` - output of Mackey-Glass equation   
    """    
    x = np.zeros(n)
    x[0] = initial
    d = int(d)
    a = signalz.vectorize_input(a, n)
    b = signalz.vectorize_input(b, n)
    c = signalz.vectorize_input(c, n)
    d = signalz.vectorize_input(d, n).astype("int")
    e = signalz.vectorize_input(e, n)
    for k in range(0,n-1):
        x[k+1]  = c[k]*x[k] + ( (a[k]*x[k-d[k]]) / (b[k] + ( x[k-d[k]]**e[k])) )   
    return x










