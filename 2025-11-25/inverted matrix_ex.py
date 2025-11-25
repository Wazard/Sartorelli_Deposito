""" import numpy as np

A = np.array([[1,2],[3,4]])

A_inv = np.linalg.inv(A)
print(A, f"\n{A_inv}")

v = np.array([3,4])
norm_v = np.linalg.norm(v)
print(v,'\n',norm_v)
 """
import numpy as np

A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

# Rank
print("Rank:", np.linalg.matrix_rank(A))

# Determinant
print("Determinant:", np.linalg.det(A))

# Inverse
print("Inverse:\n", np.linalg.inv(A))

# Eigenvalues & eigenvectors
vals, vecs = np.linalg.eig(A)
print("Eigenvalues:", vals)
print("Eigenvectors:\n", vecs)

# Solve Ax = b
b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)
print("Solution to Ax=b:", x)