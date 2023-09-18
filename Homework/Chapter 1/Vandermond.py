import numpy as np 

x = np.linspace(-50, 50, 20)
y = x**2 + 0.1*np.random.randint(1, 9)
n = 2
V = np.empty([len(x), n + 1])
for i in range(len(x) - 1):
    for j in range(n + 1):
        V[i, j] = x[i] ** (n - j)
print(V)