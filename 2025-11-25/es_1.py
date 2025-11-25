import numpy as np

array = np.linspace(start=0,stop=1,num=12)
print(array)

mat = array.reshape(3,4)
print(mat)

mat_1 = np.random.rand(3,4)
print(mat_1)

print(mat+mat_1)