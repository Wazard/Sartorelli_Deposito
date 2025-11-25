import numpy as np
import time
import os
import warnings

def get_new_matrix(r:int, c:int, seed:int=None) -> np.ndarray:
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(0, 100, size=(r, c))

def get_inner_sub_matrix(matrix:np.ndarray) -> np.ndarray:
    rows, cols = matrix.shape
    if rows <= 2 or cols <= 2:
        warnings.warn("Matrix too small to extract inner submatrix")
        return None
    return matrix[1:rows-1, 1:cols-1]

def get_transpose(matrix:np.ndarray) -> np.ndarray:
    return matrix.T

def get_sum_all(matrix:np.ndarray) -> float:
    return matrix.sum()

def multiply(matrix1:np.ndarray, matrix2:np.ndarray) -> np.ndarray:
    return matrix1 * matrix2

def get_mat_average(matrix:np.ndarray) -> float:
    return matrix.ave()

def get_determinant(matrix:np.ndarray) -> float:
    if matrix.shape[0] != matrix.shape[1]:
        warnings.warn("Matrix must be square")
        return None
    return np.linalg.det(matrix)

def get_inversion(matrix:np.ndarray) -> np.ndarray:
    if get_determinant(matrix) == 0:
        warnings.warn("Matrix is singular")
        return None
    return np.linalg.inv(matrix)

def get_sin_mat(matrix:np.ndarray) -> np.ndarray:
    return np.sin(matrix)

def get_greater_than_20(matrix:np.ndarray) -> np.ndarray:
    return matrix[matrix > 20]

def mat_exists(mat) -> bool:
    if mat is None:
        os.system('cls')
        print("Please, create a matrix first")
        time.sleep(1)
        os.system('cls')
        return False
    return True

# ---------------- MENU ----------------
def main():
    mat = None
    while True:
        time.sleep(.1)
        print("Matrix Utility Menu")
        print("1. Create new matrix")
        print("2. Get inner submatrix")
        print("3. Transpose matrix")
        print("4. Sum all elements")
        print("5. Multiply two matrices (element-wise)")
        print("6. Get matrix average")
        print("7. Get matrix determinant")
        print("8. Get matrix inversion")
        print("9. Apply sine to matrix")
        print("10. Get elements greater than 20")
        print("0. Exit")

        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            time.sleep(.8)
            os.system('cls')
            continue

        match(choice):
            case 1:
                r = int(input("Rows: "))
                c = int(input("Cols: "))
                mat = get_new_matrix(r,c)
                print("New matrix:\n", mat)

            case 2:
                if not mat_exists(mat):
                    continue
                print("Original:\n", mat)
                print("Inner submatrix:\n", get_inner_sub_matrix(mat))

            case 3:
                if not mat_exists(mat):
                    continue
                print("Original:\n", mat)
                print("Transpose:\n", get_transpose(mat))

            case 4:
                if not mat_exists(mat):
                    continue
                print("Matrix:\n", mat)
                print("Sum:", get_sum_all(mat))

            case 5:
                if not mat_exists(mat):
                    continue
                r = int(input("Rows for new matrix: "))
                c = int(input("Cols for new matrix: "))
                mat1 = get_new_matrix(r,c)
                print("Matrix1:\n", mat)
                print("Matrix2:\n", mat1)
                print("Element-wise product:\n", multiply(mat1, mat))

            case 6:
                if not mat_exists(mat):
                    continue
                print("Matrix:\n", mat)
                print("Average:", get_mat_average(mat))

            case 7:
                if not mat_exists(mat):
                    continue
                print("Matrix:\n", mat)
                print("Determinant:", get_determinant(mat))

            case 8:
                if not mat_exists(mat):
                    continue
                print("Matrix:\n", mat)
                print("Inversion:\n", get_inversion(mat))

            case 9:
                if not mat_exists(mat):
                    continue
                print("Matrix:\n", mat)
                print("Sine applied:\n", get_sin_mat(mat))

            case 10:
                if not mat_exists(mat):
                    continue
                print("Matrix:\n", mat)
                print("Elements greater than 20:\n", get_greater_than_20(mat))

            case 0:
                return

            case _:
                print("Invalid choice.")

        time.sleep(.8)


if __name__ == "__main__":
    main()
