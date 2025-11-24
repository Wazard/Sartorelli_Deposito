import numpy as np

def matrix_compare(input, func, breaker = 5):
    test_matrix = np.array([[0]*len(input),[1]*len(input)])
    count = 0
    while count<breaker:
        if np.all(test_matrix==0) or np.all(test_matrix==1):
            return test_matrix
        for i in input:
            if func(i):
                test_matrix = flip_random(test_matrix, 0, 1)
            else:
                test_matrix = flip_random(test_matrix, 1, 0)
        count+=1
    return test_matrix

def flip_random(matrix, value, new_value):
    coords = np.where(matrix == value)
    if len(coords[0]) == 0:
        return matrix
    idx = np.random.choice(len(coords[0]))
    i, j = coords[0][idx], coords[1][idx]
    matrix[i, j] = new_value
    return matrix


input_data = np.arange(0, 240, 2)   # [0, 2, 4, ..., 238]

# Function: True if the number is even
func = lambda x: x % 2 == 0

# Run the comparison
result = matrix_compare(input_data, func, breaker=50)

# Verify if the matrix is all ones
is_all_one = np.all(result == 1)

print("Matrix shape:", result.shape)
print("Matrix:\n", result)
print("All ones?", is_all_one)
