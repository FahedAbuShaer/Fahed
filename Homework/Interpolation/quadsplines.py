import numpy as np

x =np.linspace(-20, 20, 10)
y = 1 / (x**2 + 1)
n = len(x)
A = np.zeros([3 * n - 4, 3 * n - 4])
Y = np.zeros(3 * n - 4)
print(x, '\n', y)
for i in range(2):
    A[i, 0] = x[i]
    A[i, 1] = 1
j = 0
for i in range(2, 2 * n - 2, 2):
    k = int(i/2)
    A[i, j + 2] = x[k] ** 2
    A[i + 1, j + 2] = x[k + 1] ** 2
    A[i, j + 3] = x[k]
    A[i + 1, j + 3] = x[k + 1]
    A[i, j + 4] = 1
    A[i + 1, j + 4] = 1
    j = j + 3
A[2 * n - 2, 0] = 1
A[2 * n - 2, 1] = -2 * x[1]
A[2 * n - 2, 3] = -1
m, l = 0, 2
for i in range(2 * n - 1, 3 * n - 4):
    A[i, m + 2] = 2 * x[l]
    A[i, m + 3] = 1
    A[i, m + 5] = -2 * x[l]
    A[i, m + 6] = -1
    m = m + 3
    l = l + 1
print(A, "\n")
Y[0] = y[0]
Y[1] = y[1]
for i in range(2, 2 * n - 2):
    if i % 2 == 0:
        k = int(i/2)
    else:
        k = int(i/2) + 1
    Y[i] = y[k]
print("\n", Y)