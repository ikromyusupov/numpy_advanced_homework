import numpy as np

def arr_product(arr: np.ndarray) -> int:
    """
    Returns the product of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: product of all numbers
    """
    return arr.prod()