import numpy as np

def sum_axis_1(arr: np.ndarray) -> int:
    """
    Returns the sum of rows in the array
    Args:
        arr: np.ndarray
    Returns:
        np.ndarray: sum of each row
    """
    sum_list = []

    for rows in arr:
        s = 0
        for row in rows:
            s += row
        sum_list.append(s)

    return np.array(sum_list)