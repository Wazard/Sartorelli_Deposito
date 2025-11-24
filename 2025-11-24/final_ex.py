import numpy as np

# Create an empty array of 100 integers (uninitialized values at first)
ndarray = np.empty(100, dtype='int32')

# Fill the first 50 elements with values 0..49
ndarray[:50] = np.arange(50)

# Fill the last 50 elements with random integers between 49 and 101 (inclusive of 49, exclusive of 102)
ndarray[50:] = np.random.randint(49, 102, 50)

# Print the array, its data type, and its shape
print(ndarray, ndarray.dtype, ndarray.shape)

# Convert the integer array to float32 type
float_array = ndarray.astype('float32')
print(float_array, float_array.dtype, float_array.shape)

# Slice examples:
first_10 = ndarray[:10]        # first 10 elements
last_7 = ndarray[-7:]          # last 7 elements
from_5_to_20 = ndarray[5:20]   # elements from index 5 up to (but not including) 20
each_4 = ndarray[::4]          # every 4th element

# Copy the original array and modify indices 10..14 (inclusive) to 999
new_ndarray = ndarray.copy()
new_ndarray[10:15] = 999

# Fancy indexing: pick specific positions
fancy_values = ndarray[[0, 3, 7, 12, 25, 33, 48]]

# Boolean mask: select only even numbers
evendarray = ndarray[ndarray % 2 == 0]

# Compute the median of the array
med = np.median(ndarray)

# Build a mask with a lambda: True where values > median
mask = (lambda x: x > med)(ndarray)

# Apply the mask to select only values greater than the median
mediandarray = ndarray[mask]

# Print everything in a formatted way
print(f"OG: {ndarray}\n"
      f"FLOAT: {float_array}\n"
      f"F_10: {first_10}\n"
      f"L7: {last_7}\n"
      f"5TO20: {from_5_to_20}\n"
      f"EACH4: {each_4}\n"
      f"5TO20-999: {new_ndarray}\n"
      f"RANDPOS: {fancy_values}\n"
      f"EVEN: {evendarray}\n"
      f">MED: {mediandarray} med:{med}")