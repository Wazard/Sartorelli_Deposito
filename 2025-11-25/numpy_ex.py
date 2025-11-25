import numpy as np

## EXERCISE 1 ##

arr = np.random.randint(1, 101, size=15)
print(arr)

arr_sum = np.sum(arr)
arr_avg = np.average(arr)

print(f"SUM: {arr_sum}\nAVG: {arr_avg}")

## EXERCISE 2 ##

mat = np.random.randint(1, 26, size=(5,5))
print(mat)

mat_col_2 = mat[:,1]
mat_row_3 = mat[2,:]
mat_diag = np.diag(mat)
sum_mat_diag = np.sum(mat_diag)

print(
    f"COL2: {mat_col_2}\n",
    f"ROW3: {mat_row_3}\n",
    f"DIAGL: {mat_diag}\n",
    f"DIAG_SUM: {sum_mat_diag}"
    )

## EXERCISE 3 ##

mat_0 = np.random.randint(10,51,size=(4,4))

mask = [(0,1),(1,3),(2,2),(3,0)]
mat_0_indexes = np.array([mat_0[r, c] for r, c in mask])
mat_0_odd_rows = mat_0[1::2]
mat_0_broad = np.copy(mat_0)
mat_0_broad[mask] += 10

print(
    f"MAT:\n {mat_0}\n",
    f"INDEXES: {mat_0_indexes}\n",
    f"ODD_ROWS:\n{mat_0_odd_rows}\n",
    f"BROAD_MAT:\n{mat_0_broad}"
)