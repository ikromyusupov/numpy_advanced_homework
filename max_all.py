import numpy as np

def max_all(arr: np.ndarray) -> int:
    """
    Returns the max of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: max of all numbers
    """
    max = arr[0]
    for k in range(1, len(arr)):
        if arr[k] > max:
            max = arr[k]
    return max