import numpy as np

def gauss(A, b):
    n = len(A)
    
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    
    P = [[0.0] * n for i in range(n)]
    x = np.empty(n)

    for i in range(n):
        P[i][i] = 1.0
    
    #Pivot
    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(A[i][j]))
        if j != row:
            P[j], P[row] = P[row], P[j]
    
    PA = [[0] * n for i in range(n)]
    for j in range(n):
        for i in range(n):
            PA[i][j] = sum(P[i][k] * A[k][j] for k in range(n))
            
    Pb = b.copy()
    for i in range(n):
        Pb[i] = sum(P[i][k] * b[k] for k in range(n))
    
    for j in range(n):
        L[j][j] = 1
        for i in range(j+1):
            s1 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = PA[i][j] - s1
            
        for i in range(j, n):
            s2 = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]
            
    y = np.empty(n)
    for i in range(n):
        if L[i][i] == 0:
            x[i] = 0
        else:
            value = Pb[i]
            
            for j in range(i):
                value -= L[i][j] * y[j]

            value /= L[i][i]
            y[i] = value
    
    x = np.empty(n)
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            x[i] = 0
        else:
            value = y[i]
            
            for j in range(i + 1, n, 1):
                value -= U[i][j] * x[j]
            
            value /= U[i][i]
            x[i] = value
    return x

def cholesky(A):
    n = len(A)
    
    L = [[0.0] * n for i in range(n)]
    
    for i in range(n):
        s = sum(pow(L[i][k], 2) for k in range(i))
        L[i][i] = np.sqrt(A[i][i]- s)
        
        for j in range(i+1, n):
            s = sum(L[i][k]*L[j][k] for k in range(j))
            L[j][i] = (A[j][i] - s)/L[i][i]
    return L
    
def gaussSeidel(A, b):
    n = len(A)
    x = np.empty(n)
    oldx = np.empty(n)
    norm = 1
    
    while norm > 0.5*pow(10,-4):
        oldx = x.copy()
        for i in range(n):
            s1 = sum(A[i][j]* x[j] for j in range(i))
            s2 = sum(A[i][j]*x[j] for j in range(i+1,n))
                    
            x[i] = (b[i]-s1-s2)/A[i][i]

        norm = max(abs((x[i] - oldx[i])) for i in range(n))
    
    return x

#3.1
A = np.array([
    [6, 6, 8, 1], 
    [2, 7, 8, 2], 
    [0, 2, 1, 9], 
    [3, 2, 2, 5]])
b = [6, 4, 9, 2]

x = gauss(A, b)
print("The result Ax = b is: ")
print(x)

#3.2
B = np.array([
    [7, 3, -1, 2], 
    [3, 8, 1, -4], 
    [-1, 1, 4, -1], 
    [2, -4, -1, 6]])

L = cholesky(B)
print("The cholesky analysis is:")
print(L)

#3.3
n = 10
C = [[0.0] * n for i in range(n)]
for i in range(n):
    C[i][i] = 5

for i in range(n-1):
    C[i][i+1] = -2
    C[i+1][i] = -2
b = [1.0 for i in range(n)]
b[0] = 3
b[n-1] = 3

x = gaussSeidel(C ,b)
isCorrect = True
for i in range(n):
    if(abs(x[i]-1)) > pow(10,-4):
        isCorrect = False

print("The result for n = 10 is " + str(isCorrect))

n = 10000
C = [[0.0] * n for i in range(n)]
for i in range(n):
    C[i][i] = 5

for i in range(n-1):
    C[i][i+1] = -2
    C[i+1][i] = -2
b = [1.0 for i in range(n)]
b[0] = 3
b[n-1] = 3

x = gaussSeidel(C ,b)
print("The result for n = 10000 is " + str(isCorrect))