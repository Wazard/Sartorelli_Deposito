import numpy as np

### Axis analysis

def sum_by_col(matrix:np.ndarray, axis=0) -> np.ndarray:
    return np.sum(matrix, axis=axis)

def sum_by_row(matrix:np.ndarray) -> np.ndarray:
    return sum_by_col(matrix, axis=1)

def mean_by_col(matrix:np.ndarray, axis=0) ->np.ndarray:
    return np.mean(matrix, axis=axis)

def mean_by_row(matrix:np.ndarray) ->np.ndarray:
    return mean_by_col(matrix, axis=1)


### Algebrical oops

def mat_dot(matrix:np.ndarray, matrix1:np.ndarray) -> np.ndarray:
    return matrix@matrix1

def mat_transpose(matrix:np.ndarray) -> np.ndarray:
    return np.transpose(matrix)

def mat_norm(matrix:np.ndarray) -> float:
    return np.linalg.norm(matrix)

def mat_covariant(matrix:np.ndarray) -> np.ndarray:
    return np.cov(matrix, rowvar=False)