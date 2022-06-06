import numpy as np

def sum_axis_1(arr: np.ndarray) -> int:
    """
    Returns the max of rows in the array
    Args:
        arr: np.ndarray
    Returns:
        np.ndarray: max of each row
    """
    max = arr[0]
    i = 0
    for k in range(1,len(arr)):
        i+=1
        if arr[k,i] > max:
            max = arr[k,i]
    return max