import numpy as np
from core.custom_errors import UnsortedArrayError

## Base Statistics

def arr_min(arr:np.ndarray) -> float:
    return np.min(arr)

def arr_max(arr:np.ndarray) -> float:
    return np.max(arr)

def arr_mean(arr:np.ndarray) -> float:
    return np.mean(arr)

def arr_deviation(arr:np.ndarray) -> float:
    return np.std(arr)


## Position analysis

def arr_min_idx(arr:np.ndarray) -> int:
    return np.argmin(arr)

def arr_max_idx(arr:np.ndarray) -> int:
    return np.argmax(arr)

def arr_percentile(arr:np.ndarray) -> float:
    return np.percentile(arr, 50)

def arr_search_sorted(master, arr:np.ndarray, value:float):
    if not np.all(arr[:-1] <= arr[1:]):
        raise UnsortedArrayError(master,"Array is not sorted")
    return np.searchsorted(arr, value)