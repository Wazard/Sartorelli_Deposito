import numpy as np

ndarray = np.empty(100,dtype='int32')

ndarray[:50] = np.arange(50)
ndarray[50:] = np.random.randint(49,102,50)
print(ndarray, ndarray.dtype, ndarray.shape)

float_array = ndarray.astype('float32')
print(float_array, float_array.dtype, float_array.shape)

first_10 = ndarray[:10]
last_7 = ndarray[-7:]
from_5_to_20 = ndarray[5:20]
each_4 = ndarray[::4]

new_ndarray = ndarray.copy()
new_ndarray[10:15] = 999

fancy_values = ndarray[[0,3,7,12,25,33,48]]
evendarray = ndarray[ndarray%2==0]
med = np.median(ndarray)
mask = (lambda x: x>med)(ndarray)
mediandarray = ndarray[mask]

print(f"OG: {ndarray}\nFLOAT: {float_array}\nF_10: {first_10}\nL7: {last_7}\n5TO20: {from_5_to_20}\nEACH4: {each_4}\n5TO20-999: {new_ndarray}\nRANDPOS: {fancy_values}\nEVEN: {evendarray}\n>MED: {mediandarray}med:{med}")