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
    f"COL2: {mat_col_2}",
    f"ROW3: {mat_row_3}",
    f"DIAGL: {mat_diag}",
    f"DIAG_SUM: {sum_mat_diag}"
    )

## EXERCISE 3 ##

mat_0 = np.random.randint(10,51,size=(4,4))
mat_0_indexes = mat_0[1::2]

