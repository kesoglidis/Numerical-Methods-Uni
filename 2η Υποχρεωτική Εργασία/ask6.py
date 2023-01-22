import numpy as np


def trapezoid(Y, X):
    N = len(X)
    s = sum(Y[i] for i in range(1, N-1))
    integral = (X[-1]-X[0]) /(2*(N-1)) *(Y[0] +Y[-1] +2*s)
    return integral

def simpson(Y, X):
    N = len(X)
    s = 2*sum(Y[2*i] for i in range(1, int(N/2))) +4*sum(Y[2*i-1] for i in range(1,int(N/2+1)))
    integral = (X[-1]-X[0])/(3*(N-1))*(Y[0]+ Y[-1] +s)
    return integral

N = 11
X = np.linspace(0, np.pi/2, N, True)
Y = [np.sin(i) for i in X]

print("Trapezoid method:")
print(trapezoid(Y, X))
print("Simpson's method:")
print(simpson(Y, X))