import numpy as np

def vectorize_input(x, n):
    """
    Test if input parameter is a vector, if not, create array of desired lenght
    containing only the copies of input parameter.
    """
    if hasattr(x, '__len__') and (not isinstance(x, str)):
        pass
    else:    
        x = np.ones(n)*x  
    return x  
    
def matrixize_input(x, n):
    """
    Test if input vector 1d or a matrix, if it is matrix, then create matrix
    of desired lenght containing only the copies of input vector.
    """
    if len(x.shape) == 1:
        x = np.tile(x, (n, 1))
    return x  
    
def check_type_or_raise(obj, expected_type, obj_name):
    """
    This fuction raises error if the object does not have expected type.
    """
    if not isinstance(obj, expected_type):
        raise TypeError(
            "'{}' must be {}, not {}".format(
                obj_name,
                expected_type.__name__,
                obj.__class__.__name__)
            )
    
def rem(a, b):
    """
    Reminder estimation function (estimates reminder in different way
    than it is default in Pyton).
    """
    q = abs(a) % b
    s = np.sign(a)
    return q*s
    
def ode45_step(f, x, t, dt, *args):
    """
    One step of 4th Order Runge-Kutta method
    """
    k = dt
    k1 = k * f(t, x, *args)
    k2 = k * f(t + 0.5*k, x + 0.5*k1, *args)
    k3 = k * f(t + 0.5*k, x + 0.5*k2, *args)
    k4 = k * f(t + dt, x + k3, *args)
    return x + 1/6. * (k1 + k2 + k3 + k4)
 
def ode45(f, t, x0, *args):
    """
    4th Order Runge-Kutta method
    """
    n = len(t)
    x = np.zeros((n, len(x0)))
    x[0] = x0
    for i in range(n-1):
        dt = t[i+1] - t[i] 
        x[i+1] = ode45_step(f, x[i], t[i], dt, *args)
    return x
