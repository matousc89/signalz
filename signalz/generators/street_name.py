"""
.. versionadded:: 0.9

This function randomly create street names.

Example Usage
===============

One random street name:

.. code-block:: python

    >>> signalz.street_name()
    'Mulberry Drive'

Five different streets:

.. code-block:: python

    >>> signalz.street_name(n=5)
    ['Onion Street', 'Mulberry Avenue', 'Meadow Hill', 'Apple Way', 'Oak Hill']

If you need only small sample, you can make all names unique
with argument `repeat`:

.. code-block:: python

    >>> signalz.street_name(n=5, repeat=False)

Function Documentation
======================================
"""
import random

FIRSTS = [
    "Beach", "Sandy", "Meadow", "Madison", "Eagle", "Oak", "Walnut"
    "Mahagony", "Tulip", "Cork", "Willow", "Maple", "Cucumber",
    "Cedar", "Beech", "Apple", "Hazel", "Ash", "Hawthorn", "Birch",
    "Long", "Spruce", "Cypress", "Platanus", "Larch", "Olive",
    "Mulberry", "Pie", "Cake", "Onion",
]

SECONDS = [
    "Drive", "Street", "Avenue", "Hill", "Road", "Way",
]

def build_name(f=False, s=False):
    """
    :param f: first word, optional
    :param s: second word, optional
    :return: full street name
    """
    f = f if f else random.choice(FIRSTS)
    s = s if s else random.choice(SECONDS)
    return "{} {}".format(f, s)


def street_name(n=1, repeat=True):
    """
    Function that randomly buid street name or names.

    :param n: size of sample (how many streets)
    :param repeat: if the street names can repeat in sample
    :return: one name of street (string), or list of names
    """
    if n == 1:
        return build_name()
    else:
        if not repeat:
            if n > len(FIRSTS):
                raise Exception('n should not exceed {}'
                    .format(len(FIRSTS)))
            return [build_name(f) for f in random.sample(FIRSTS, n)]
        else:
            return [build_name() for _ in range(n)]