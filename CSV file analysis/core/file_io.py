import csv
import numpy as np
import warnings

def get_from_csv(path: str) -> np.ndarray:
    """
    Load a CSV file and return its contents as a NumPy array.
    
    Parameters
    ----------
    path : str
        Path to the CSV file.
    
    Returns
    -------
    np.ndarray
        Matrix if multiple rows, array if single row.
    """
    try:
        with open(path, newline='') as f:
            reader = csv.reader(f)
            data = [list(map(float, row)) for row in reader if row]
    
    except Exception as e:
        warnings.warn(f"Could not read file: {e}")
        return None
    
    f.close()

    arr = np.array(data)
    if arr.size == 0:
        warnings.warn("CSV file is empty")
        return None
    
    if arr.shape[0] == 1:
        return arr.flatten()
    return arr

def load_to_csv(path: str, data: np.ndarray) -> bool:
    """
    Save a NumPy array or matrix to a CSV file.

    Parameters
    ----------
    path : str
        Path to the CSV file.
    data : np.ndarray
        Array or matrix to save.

    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    try:
        with open(path, "w", newline="") as f:   # write mode
            writer = csv.writer(f)

            if data.ndim == 1:   # 1D array
                writer.writerow([x for x in data])
            else:                # 2D matrix
                writer.writerows(data)

        return True
    except Exception as e:
        warnings.warn(f"Could not write to file: {e}")
        return False

'''
arr = np.array([1, 2, 3, 4])
mat = np.array([[1, 2, 3], [4, 2, 6]])

load_to_csv("array.csv", arr)
load_to_csv("matrix.csv", mat)
'''