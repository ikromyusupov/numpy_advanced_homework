import numpy as np

def sum_all(arr: np.ndarray) -> int:
    """
    Returns the sum of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: sum of all numbers
    """
    s = 0
    for rows in arr:
        for row in rows:
            s += row

    return s