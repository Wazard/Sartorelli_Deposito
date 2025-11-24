import numpy as np

array = np.arange(10,50,1,dtype='int32')

print(array, array.dtype, array.shape)
float_array = array.astype('float64')

print(float_array, float_array.dtype, float_array.shape)

def matrix_compare(input, func, breaker = 5):
    test_matrix = np.array([[0]*len(input),[1]*len(input)])
    count = 0
    while count<breaker:
        for i in input:
            if func(i):
                test_matrix = flip_random(test_matrix, 0, 1)
            else:
                test_matrix = flip_random(test_matrix, 1, 0)
    return test_matrix

def flip_random(matrix, value, new_value):
    coords = np.where(matrix == value)
    if len(coords[0]) == 0:
        return matrix
    idx = np.random.choice(len(coords[0]))
    i, j = coords[0][idx], coords[1][idx]
    matrix[i, j] = new_value
    return matrix


