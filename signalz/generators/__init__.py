try:    
    import numpy

    # fancy stuff
    from signalz.generators.autoregressive_model import autoregressive_model
    from signalz.generators.mackey_glass import mackey_glass
    from signalz.generators.logistic_map import logistic_map
    from signalz.generators.ecgsyn import ecgsyn

    # noises and walks
    from signalz.generators.gaussian_white_noise import gaussian_white_noise
    from signalz.generators.uniform_white_noise import uniform_white_noise
    from signalz.generators.brownian_noise import brownian_noise
    from signalz.generators.levy_noise import levy_noise
    from signalz.generators.levy_flight import levy_flight
    from signalz.generators.levy_walk import levy_walk

    # basic shapes and functions
    from signalz.generators.sinus import sinus
    from signalz.generators.cosinus import cosinus
    from signalz.generators.steps import steps
    from signalz.generators.random_steps import random_steps

    # others
    from signalz.generators.card_dealer import card_dealer_numpy as card_dealer

except ImportError:
    """
    Numpy was not loaded. Number of functions you can use is limited.
    Some functions can work in a slightly different way.
    """
    from signalz.generators.card_dealer import card_dealer



# lorem ipsum
import signalz.generators.lorem_ipsum 



