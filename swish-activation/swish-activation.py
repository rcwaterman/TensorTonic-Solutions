import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    arr = np.array(x)
    return arr*(1/(1+np.exp(-arr)))