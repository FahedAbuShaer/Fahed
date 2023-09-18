import numpy as np
import matplotlib.pyplot as plt

def Vandermond(x, y, n):
    V = np.empty([len(x), n + 1])
    for i in range(n + 1):
        V[:, i] = x ** i
    return V

def LeastSquare(V, y):
    Vt = np.transpose(V)
    A = Vt @ V
    Y = Vt @ y
    b = np.linalg.solve(A, Y)
    return b

def fitpolynomial(x, b, n):
    Ps = np.zeros(len(x))
    for j in range(len(x)):
        p = 0
        for i in range(n + 1):
            p += b[i] * x[j] ** i
        Ps[j] = p
    return Ps

def SSE(P, y):
    k = np.subtract(P, y)
    error = np.sum(k * k)
    return error

x = np.linspace(-10, 10, 10)
x_train = np.random.choice(x, int(0.8*len(x)), replace = False)
y_train = np.random.uniform(0, 10, int(0.8*len(x))) * x_train ** 3 + np.random.uniform(0, 10, int(0.8*len(x)))
plt.scatter(x_train, y_train)
x_test = np.setdiff1d(x, x_train)
y_test = np.random.uniform(0, 10, int(0.2*len(x))) * x_test ** 3 + np.random.uniform(0, 10, int(0.2*len(x)))
n = 5
test_error = np.empty(n)
train_error = np.empty(n)
order = np.arange(1, n + 1, 1)
for i in range(n):
    V = Vandermond(x_train, y_train, order[i])
    b = LeastSquare(V, y_train)
    xs = np.linspace(-20, 20, 50)
    p = fitpolynomial(x_train, b, order[i])
    plt.plot(x_train, p)
    error = SSE(p, y_train)
    train_error[i] = error
    p = fitpolynomial(x_test, b, order[i])
    error = SSE(p, y_test)
    test_error[i] = error
print(train_error)
print(test_error)
plt.show()
plt.plot(order, train_error, label = "Train")
plt.plot(order, test_error, label = "Test")
plt.legend()
plt.show()