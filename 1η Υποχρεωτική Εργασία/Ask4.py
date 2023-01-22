import numpy as np

def powerMethod(G):
    n = len(G)
    p = [1 for i in range(n)] 
    eigenvalue = 1
    old = 0
    while abs(eigenvalue - old) > 0.5*pow(10,-4):
        p = np.matmul(G, p)
        old = eigenvalue
        eigenvalue = p[0]
        
        for i in range(n):
            p[i] = p[i]/eigenvalue

    return p / sum(p)
    
def googleMatrix(q, A):
    n = len(A)
    G = np.zeros((n,n))
    
    for j in range(n):
        nj = sum(A[j][i] for i in range(n))
        for i in range(n):
            G[i][j] = q/n + A[j][i]*(1-q)/nj
    return G

#4.2
A = np.array([
    [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]])

 
G = googleMatrix(0.15, A)

p = powerMethod(G)

print("Result for 4.2 is:")
print("p = " + str(p))

#4.3

B = A.copy()
B[2][1] = 0
B[1][0] = 1
B[2][0] = 1
B[3][0] = 1
B[5][0] = 1

G = googleMatrix(0.15, B)

p = powerMethod(G)

print("Result for 4.3 is:")
print("p = " + str(p))

#4.4(A)
G = googleMatrix(0.02, B)

p = powerMethod(G)

print("Result for q = 0.02 in 4.4(A) is:")
print("p = " + str(p))

#4.4(B)
G = googleMatrix(0.6, B)

p = powerMethod(G)

print("Result for q = 0.6 in 4.4(B) is:")
print("p = " + str(p))

#4.5
G = googleMatrix(0.15, A)

p = powerMethod(G)

print("Result for 4.5(before) is:")
print("p[10] = " + str(p[10]))
print("p[9] = " + str(p[9]))

newA = A.copy()
newA[7][10] = 3
newA[11][10] = 3

G = googleMatrix(0.15, newA)

p = powerMethod(G)

print("Result for 4.5(after) is:")
print("p[10] = " + str(p[10]))
print("p[9] = " + str(p[9]))

#4.6
n = len(A)
C = np.delete(A, 9, 0)
C = np.delete(C, 9, 1)

G = googleMatrix(0.15, C)

p1 = powerMethod(G)

G = googleMatrix(0.15, A)

p = powerMethod(G)

diff = [0 for i in range(14)]
for i in range(n-1):
    if (i < 9):
        diff[i] = p1[i] - p[i] 
    if (i > 9):
        diff[i] =  p1[i] - p[i+1]
    diff[i] = round(diff[i], 4)

print("Difference after deletion of site 10 for 4.6 is ")
print(diff)