# import numpy as np

# def df(x, T):
#     h = 6.62607015e-34
#     c = 299792458
#     k = 1.380649e-23
#     n = (2*h*(c**2))*((((5*k*T*x)-(h*c))*np.exp((h*c)/(k*T*x))) - (5*k*T*x))
#     d = (k*T*(x**7))*((np.exp((h*c)/(k*T*x))-1)**2)
#     dB = -(n/d)
#     return dB

# def ddf(x, T):
#     h = 6.62607015e-34
#     c = 299792458
#     k = 1.380649e-23
#     cn = 2 * h * (c**2)
#     n1 = ((30*(T**2)*(k**2)*(x**2)) - 12*T*h*c*k*x + (c**2)*(h**2))*np.exp((2*c*h)/(k*T*x))
#     n2 = (-60*(T**2)*(k**2)*(x**2) + 12*T*c*h*k*x + (c**2)*(h**2))*np.exp((h*c)/(k*T*x))
#     n3 = 30*(T**2)*(k**2)*(x**2)
#     d = ((T**2)*(k**2)*(x**9)) * ((np.exp((h*c)/(k*T*x))-1)**3)
#     ddB = (cn * (n1+n2+n3))/d
#     return ddB

# def NewtonRaphson(x0, T):
#     iteration = 100
#     df0 = df(x0, T)
#     ddf0 = ddf(x0, T)
#     x = x0 - (df0/ddf0)
#     i = 0
#     while i<iteration:
#         df1 = df(x, T)
#         ddf1 = ddf(x, T)
#         x = x - (df1/ddf1)
#         i += 1
#     return x

# T = 5000
# x0 = 6e-7
# l = NewtonRaphson(x0, T)
# print(l)
import sympy as syp
m = syp.Symbol('m')
k = syp.Symbol('k')
def f(i,j):
    if i == j:
        return 2 * (k/m)
    elif i+1 == j or i-1 == j:
        return -1 * (k/m)
    else:
        return 0
L = syp.Matrix(10, 10, f)
l = L.eigenvals()
v = L.eigenvects()
print(L)
print(l)
print(v)