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
