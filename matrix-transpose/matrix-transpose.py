import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.array(A)
    A_T = np.zeros((A.shape[1], A.shape[0]))

    for i, row in enumerate(A):
        A_T[:, i] = row

    return A_T
