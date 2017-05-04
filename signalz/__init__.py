"""
Current version: |version| (:ref:`changelog`)

This library is designed to simplify testing data obtaining with Python.
For code optimisation,
this library uses `Numpy <http://www.numpy.org/>`_ for array operations.

.. toctree::
    :maxdepth: 2
    
    index

License
===============

This project is under `MIT License <https://en.wikipedia.org/wiki/MIT_License>`_.

Instalation
====================
With `pip <https://pypi.python.org/pypi/pip>`_ from terminal:
``$ pip install signalz``

Or download you can download the source codes from Github
(`link <https://github.com/matousc89/signalz>`_)

The User Quide
=====================

Here is complete documentation for all implemented functions.


.. cssclass:: funcitem

    * :ref:`generators-sinus`

.. cssclass:: functag

    :ref:`tags-goniometric` 

.. cssclass:: funcitem

    * :ref:`generators-cosinus`

.. cssclass:: functag

    :ref:`tags-goniometric` 

.. cssclass:: funcitem

    * :ref:`generators-steps`

.. cssclass:: functag

    :ref:`tags-steps` 

.. cssclass:: funcitem

    * :ref:`generators-random_steps`

.. cssclass:: functag

    :ref:`tags-steps`, :ref:`tags-random` 

.. cssclass:: funcitem

    * :ref:`generators-mackey_glass`

.. cssclass:: functag

    :ref:`tags-chaotic` 

.. cssclass:: funcitem

    * :ref:`generators-white_noise`

.. cssclass:: functag

    :ref:`tags-random` 

.. cssclass:: funcitem

    * :ref:`generators-autoregressive_model`

.. cssclass:: functag

    :ref:`tags-autoregressive` 

.. cssclass:: funcitem

    * :ref:`generators-logistic_map`

.. cssclass:: functag

    :ref:`tags-population_model`, :ref:`tags-chaotic`  



Contact
=====================

By email: matousc@gmail.com


Changelog
======================

For informations about versions and updates see :ref:`changelog`.

Indices and tables
===========================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

"""

from generators import *
from misc import *

