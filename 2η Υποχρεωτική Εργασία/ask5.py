import numpy as np
import matplotlib.pyplot as plt

def mul(A, B):
    n = np.array(B[0]).size
    AB = [[0] * n for i in range(len(A))]
    if(n == 1):
        for i in range(len(A)):
                AB[i] = sum(A[i][k] * B[k] for k in range(min(len(A[0]),len(B))))
    else:
        for j in range(n):
            for i in range(len(A)):
                AB[i][j] = sum(A[i][k] * B[k][j] for k in range(min(len(A[0]),len(B))))
    return AB

def polynomial(x, coeff):
    poly = 0
    for i, scalar in enumerate(coeff):
        poly += scalar*x**(len(coeff)-1-i)
        if(coeff[0] > 0.08 and coeff[0] < 0.085):
            print(poly)
    return poly

def poly_approx(x, X, Y):
    p = 0
    for i in range(len(X)):
        jrange = [j for j in range(len(X))]
        jrange.remove(i)
        L = 1
        for j in jrange:
            L *= (x-X[j])/(X[i]-X[j])
        p += Y[i]*L
    return p

def splines(x, X, Y):
    n = len(X)
    A = [[0.0]*4*(n-1) for i in range(4*(n-1))]
    b = [0 for i in range(4*(n-1))]
    
    k = 0
    for i in range(n-1):
        b[i] = Y[i]
        k +=1
        for j in range(4*i, 4*i+4):
            A[i][j] = X[i]**(3-j%4)
        
    for i in range(n-1):
        b[k] = Y[i+1]
       
        for j in range(4*i, 4*i+4):
            A[k][j] = X[i+1]**(3-j%4)
        k +=1

    for i in range(0,n-2):
        A[k][4*i] = 3*X[i+1]**2
        A[k][4*i+1] = 2*X[i+1]
        A[k][4*i+2] = 1
        A[k][4*i+4] = -3*X[i+1]**2
        A[k][4*i+5] = -2*X[i+1]
        A[k][4*i+6] = -1
        k +=1

    for i in range(0,n-2):
        A[k][4*i] = 6*X[i+1]
        A[k][4*i+1] = 2
        A[k][4*i+4] = -6*X[i+1] 
        A[k][4*i+5] = -2
        k +=1

    A[k][0] = 6*X[0]
    A[k][1] = 2
    k +=1
    A[k][4*(n-2)] = 6*X[n-1] 
    A[k][4*(n-2)+1] = 2


    coeff = mul(np.linalg.inv(A), b)
    for i in range(1,n):
        if(x<X[i]):
            break

    x = polynomial(x,coeff[4*i-4:4*i])
    return x

# def least_squares(x, X, Y):
#     n = len(X)
#     A = [[0.0]*6 for i in range(n)]
#     for i in range(n):
#         for j in range(6):
#             A[i][j] = X[i]**(5-j)
#     At = np.transpose(A)
#     b = np.dot(np.linalg.inv(np.dot(At,A)), np.dot(At,Y))

#     return fifth(x, *b)

def least_squares(x, X, Y, deg):
    n = len(X)
    A = [[0.0]*(deg+1) for i in range(n)]
    for i in range(n):
        for j in range(deg+1):
            A[i][j] = X[i]**(deg-j)
    At = np.transpose(A)
    b = mul(np.linalg.inv(mul(At,A)), mul(At,Y))
    
    return np.round(polynomial(x, b)*10**4)/10**4

X = np.linspace(-np.pi, np.pi, 10)
Y = np.sin(X)

data = np.linspace(-np.pi, np.pi, 200)
Y_poly = []
Y_ls = []
Y_splines = []
for i in data:
    Y_poly.append(poly_approx(i, X, Y))
    Y_splines.append(splines(i, X ,Y))
    Y_ls.append(least_squares(i, X, Y, 5))

plt.plot(data, abs(np.sin(data)-Y_poly), label = 'Polynomial')
# plt.plot(data, abs(np.sin(data)-Y_splines), '--', label = 'Cubic Splines')
# plt.plot(data, abs(np.sin(data)-Y_ls), label = 'Least Squares')
# plt.plot(data, (Y_poly), label = 'Polynomial')
# plt.plot(data, (Y_splines), label = 'Cubic Splines')
# plt.plot(data, (Y_ls), label = 'Least Squares')
# for i in range(len(X)):
#     Y_vert = np.linspace(-1,1,10)
# plt.plot(X, np.zeros(len(X)),'.', color = 'k')
plt.title("Error of numerical methods")
plt.legend()
plt.show()

# for i in range(10):
#     x0 = np.pi*i/10 % (2*np.pi)
#     x0 = 2
#     print("x0 " + str(x0))
#     print(np.sin(x0))
#     print(poly_approx(x0, X, Y))
#     print(splines(x0, X, Y))
#     print(least_squares(x0, X, Y))


x0 = 1.789
# x = poly_approx(x0, X, Y)
# print(x)

# X = np.arange(-10,10)
# Y = np.sin(X)
# x = splines(x0, X, Y)
# print(x)


# for i in range(len(X)-1):
#     data = np.linspace(X[i],X[i+1],100)
#     plt.plot(data, cubic(data, x[4*i],x[4*i+1],x[4*i+2],x[4*i+3]))
# plt.plot(X,Y)
# plt.show()

# X = np.linspace(-np.pi,np.pi, 10)
# Y = np.sin(X)
# x = least_squares(x0, X, Y)
# print(x)
