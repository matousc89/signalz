"""
.. versionadded:: 0.8

This function generates credit card number valid
according to the Luhn algorithm.

Example Usage
===============

Get credit card number (in default format - Visa):

.. code-block:: python

    signalz.credit_card_number("American Express")

Get credit card number in American Express card format:

.. code-block:: python

    signalz.credit_card_number("American Express")

Get credit card in custom format:

.. code-block:: python

    signalz.credit_card_number(prefix="321", length=10)


Function Documentation
======================================
"""
import random

def credit_card_number(brand="Visa", prefix=False, length=False):
    OPTIONS = {
        "Visa": {
            "prefix": ("4",),
            "length": 16,
        },
        "Mastercard": {
            "prefix": ("51", "55"),
            "length": 16,
        },
        "American Express": {
            "prefix": ("34", "37"),
            "length": 15,
        }
    }
    if not prefix:
        prefix = random.choice(OPTIONS[brand]["prefix"])
    if not length:
        length = OPTIONS[brand]["length"]
    prefix = [int(x) for x in prefix]
    n = length - 1 - len(prefix)
    digits = prefix + [random.choice(range(10)) for _ in range(n)] + [0]
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    checksum_digit = (10 - (odd_sum + even_sum) % 10) % 10
    all_digits = digits[:-1] + [checksum_digit]
    return "".join([str(_) for _ in all_digits])

def luhn_checksum(string):
    """
    Compute the Luhn checksum for the provided string
    (representing numbers).
    """
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def verify(string):
    """
    Check if the provided string of digits comply the Luhn.
    """
    return (luhn_checksum(string) == 0)




