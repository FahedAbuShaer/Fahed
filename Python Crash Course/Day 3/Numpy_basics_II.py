# %%
import numpy as np

# 1) Random numbers in numpy 
# The Numpy library has a lot of functions for 
# generating random numbers
# You can access them by using np.random.function_name

# a) Random numbers from a uniform distribution
dist = np.random.uniform(0, 10, (5, 5))
print(dist)
# b) Random numbers from a normal distribution
dist = np.random.normal(0, 10, (5,5))
print(dist)
# c) Random integers
dist = np.random.randint(0, 50, (5, 5))
print(dist)
# d) Random choice
import string
AllLetters = [i for i in string.ascii_lowercase] # This is a list of all
# Letters in the alphabet
list = np.random.choice(AllLetters, 26)
print(list)
# Without replacement
list = np.random.choice(AllLetters, 26, replace=False)
print(list)

# You can also shuffle an array
# Fill in 
np.random.shuffle(AllLetters)
print(AllLetters)

# After knowing how to shuffle an array, you can
# you must also know how to sort an array
# 4) Sorting arrays with numpy
# a) Sorting an array
# Fill in
sort = np.sort(list)
print(sort)
# or
# Fill in 

# b) you can also sort an array by its index
# This will return the indices of the sorted array
# but not the array itself
arc = np.argsort(list)
print(arc)
print(list[list.argsort()])
# Fill in

# or 
# Fill in


# 3) Mathematical operations with numpy
# a) Element-wise operations + - * / ** % ~ and the 
# more mystic ones: & | ^ >> << (bitwise operations)
# This means that it will operate on each element of   
# the array. Example:

a = np.arange(10)
b = np.arange(10,20)

print('a: ', a)
print('b: ', b)
print('a+b: ', a+b)
print('a-b: ', a-b)
# NOTE: The ~ that I added above is the bitwise not 
# operator but I included it in the regular operators 
# because it is useful for Boolean arrays
# It will invert the Boolean array. Example:
Bools = np.array([True, False, True, False])
print('Bools: ', Bools)
print('not Bools: ', ~Bools)
# %%
# 4) Linear Algebra with numpy
# NOTE: for all the operations that we will see
# you need to make sure that the dimensions of the
# matrices are compatible 


# a)Matrix addition and subtraction
# we already saw how to do matrix addition and 
# subtraction just use + and - operators 
# b) Matrix multiplication
a = np.arange(10).reshape(2,5)
b = np.arange(10,20).reshape(5,2)
print('a: \n', a)
print('b: \n', b)

# Fill in 
print('\n a * b: \n', a @ b)
# %%
# c) Matrix transpose
a = np.arange(10).reshape(2,5)
print('a: \n', a)

# Fill in
print('\nTranspose of a', a.T)

# %%
# d) More complex linear algebra operations

# We want to solve the following system of equations
# 3x + 2y = 26
# 4x + 5y = 58
# This is equivalent to solving the following matrix
# equation
# Ax = b
# where
A = np.array([[3,2],[4,5]])
b = np.array([26,58])

# Fill in to solve the system of equations
answer = np.linalg.solve(A, b)
print(answer)

# Similarly we can calculate many other things like
# the determinant of a matrix/ inverse of a matrix/ 
# eigenvalues /...
# You can look them up on the numpy docs
# %%
# e)Special matrices
# There are many special matrices that you can create
# using numpy. For example:

# Identity matrix
# The identity matrix is a square matrix with ones on
# the diagonal and zeros everywhere else
# Create a 5x5 identity matrix
# Fill in
I = np.identity(5)
print(I)

# or
I = np.eye(5, 7)
print(I)



# Diagonal matrix
# The diagonal matrix is a square matrix with the
# specified values on the diagonal and zeros everywhere
# else
# Create a 5x5 matrix with 1,2,3,4,5 on the
# diagonal and zeros everywhere else

# Fill in
# %%