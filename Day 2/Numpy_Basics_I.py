# %%
import numpy as np 

# 1) Ranges of numbers

# Create a range of numbers from 0 to 10 with a step size of 0.5
my_range = np.arange(0, 10.5, 0.5)
print(my_range)

# Or you can use linspace
my_range = np.linspace(0, 10, 21)
print(my_range)

# %%
# Create an array of all 0s of size 10
my_array = np.zeros(10)
print(my_array)
# Create an array of all 1s of size 10
my_array = np.ones(10)
print(my_array)
# Create an array of all 100s of size 10
my_array = np.full(10, 100)
print(my_array)

# You now want to take the my_array with all 100s and change all elements to 200s
my_array.fill(200)
print(my_array)
# %%
# 2) 2-D Arrays
# Numpy makes it easy to create 2-D arrays

# Create a 2-D array of all 0s of size 3x3
my_array = np.zeros((3, 3)) #((row, column, depth))
print(my_array)
# And it stays the same for all functions we used 
# before, just instead of the size being a single
# number, it is now a tuple
# %%
# 3) Reshaping arrays
# You can reshape arrays to be different sizes
# as long as the number of elements is the same

# say you have an array of size 9 
array = np.arange(9)

# You can reshape it to be a 3x3 array
array1 = np.reshape(array, (3, 3))
print(array1)
# NOTE: to get the shape of an array you can use
# the shape attribute
print(array1.shape) # This gives a tuple of the shape

# Also you can just specify one dimension and the 
# second one will just be calculated by numpy
# Just put -1 on the dimension you want numpy to    
# calculate. example:
array2 = np.reshape(array, (3, -1))
print('array2: ', array2)
# NOTE: you can only have one -1 in the tuple 
# if you have a 3-D array you have to specify at least 
# 2 dimensions
# %%
# 4) Indexing arrays 
# All the rules from normal python lists apply
# but there are some extra things you can do
# with numpy arrays. example:

# Create a 2-D array of size 10x10    
array = np.arange(0,100)
array = np.reshape(array, (10, 10))
print(array, '\n')
# You can index a specific row
print(array[3], '\n')
# You can index a specific column
print(array[:,3], '\n')
# You can index a specific element
print(array[2, 5], '\n')

# You can also take a slice of the array
# Say you want the first 2 rows
print(array[:2, :], '\n')
# Say you want the first 2 columns
print(array[:, :2], '\n')
# Say you want the first 2 rows and columns
print(array[:2, :2], '\n')
# You can also use the step 
# Say you want every other row
print(array[::2,:], '\n')
# Say you want every other column
print(array[:, ::2], '\n')
# Say you want every other row and column
print(array[::2,::2], '\n')

# You can also index with a list
# Say you want the first and last row
print(array[(0,-1),:], '\n')
# Say you want the first and last column
print(array[:,(0,-1)],'\n')

# Now try to only get the diagonal elements
print(array[(np.arange(10)), (np.arange(10))], '\n')
print(np.diagonal(array), '\n')
# %%
# But now Try to get the anti diagonal elements
print(array[(np.arange(0, 10)), (np.arange(9, -1, -1))], '\n')
# But you can use a workaround in numpy 
# by flipping the array left to right
# and then using the diag function
array1 = np.fliplr(array)
print(np.diagonal(array1), '\n')

# You can also index with a boolean array
# Say you want all the elements greater than 50
print(array[array>50])
# Say you want all the elements that are even
print(array[array % 2 == 0])
# %%
# If you need to change the type of variable 
# in an array you can use the astype function
# or the dtype attribute to change this
# example:
numbers = np.arange(10)
print('numbers: ', numbers)
numbers = np.arange(10, dtype=np.float32)
print('numbers float : ', numbers)
numbers = numbers.astype(np.complex64)
print('numbers complex: ', numbers)
# %%