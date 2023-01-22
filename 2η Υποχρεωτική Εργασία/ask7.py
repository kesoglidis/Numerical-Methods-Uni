import numpy as np

def polynomial(x, coeff):
    poly = 0
    for i, scalar in enumerate(coeff):
        poly += scalar*x**(len(coeff)-1-i)
    return poly

def least_squares(x, X, Y, deg):
    n = len(X)
    A = [[0.0]*(deg+1) for i in range(n)]
    for i in range(n):
        for j in range(deg+1):
            A[i][j] = X[i]**(deg-j)
    At = np.transpose(A)
    b = np.dot(np.linalg.inv(np.dot(At,A)), np.dot(At,Y))
    
    # import matplotlib.pyplot as plt
    # plt.figure(figsize=(15,4))
    # plt.plot(X,polynomial(X,b))
    # plt.plot(X,Y, color ='b')
    # plt.show()

    return np.round(polynomial(x, b)*10**4)/10**4

X = np.arange(0,10)
X_date = [-1, 0, 3, 4, 5, 6, 7, 10, 11, 12]
Y_Elpe = [6.25, 6.26, 6.41, 6.49, 6.48, 6.49, 6.48, 6.53, 6.43, 6.44]

print("For Elpe")
print("13/10/2022 actual price: 6.5")
print("2nd /3rd /4th degrees predictions")
print(least_squares(10, X, Y_Elpe, 2), end=" /")
print(least_squares(10, X, Y_Elpe, 3), end=" /")
print(least_squares(10, X, Y_Elpe, 4))

print("20/10/2020 actual price: 6.84")
print("2nd /3rd /4th degrees predictions")
print(least_squares(15, X, Y_Elpe, 2), end=" /")
print(least_squares(15, X, Y_Elpe, 3), end=" /")
print(least_squares(15, X, Y_Elpe, 4))

Y_Inkat = [1.4440, 1.4370, 1.3600, 1.3690, 1.3940, 1.4370, 1.4110, 1.4110, 1.37, 1.355]

print("For Inkat")
print("13/10/2022 actual price 1.372")
print("2nd /3rd /4th degrees predictions")
print(least_squares(10, X, Y_Inkat, 2), end=" /")
print(least_squares(10, X, Y_Inkat, 3), end=" /")
print(least_squares(10, X, Y_Inkat, 4))

print("20/10/2020 actual price 1.406")
print("2nd /3rd /4th degrees predictions")
print(least_squares(15, X, Y_Inkat, 2), end=" /")
print(least_squares(15, X, Y_Inkat, 3), end=" /")
print(least_squares(15, X, Y_Inkat, 4))