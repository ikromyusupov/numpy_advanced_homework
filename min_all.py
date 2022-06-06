import numpy as np

def min_all(arr: np.ndarray) -> int:
    """
    Returns the min of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: min of all numbers
    """
    min = arr[0]
    for k in range(1,len(arr)):
        if arr[k] < min:
            min = arr[k]
    return min