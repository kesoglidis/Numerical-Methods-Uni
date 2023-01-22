import numpy as np

def f(x):
    return np.exp(np.sin(x)**3) + x**6 -2*x**4 -x**3 -1

def df(x):
    h = 10e-6
    return (f(x+h)-f(x-h))/(2*h)
    
def ddf(x):
    h = 10e-6
    return (df(x+h)-df(x-h))/(2*h)
    
def accuracy(new, old, accuracy):
    distance = abs(new - old)
    if(distance <= accuracy):
        return True
    return False

def bisection(a, b):
    mid = (a+b)/2.0
    if(f(mid)*f(a) < 0):
        return a , mid, mid
    else:
        return mid , b , mid
        
def newton_raphson(x):
    return x-f(x)/df(x)
    
def secant(xn, x):
    diff = (f(xn)*(xn-x))/(f(xn)-f(x))
    return xn-diff, xn

a = -2.0
b = -1.0
loops = 1
accurate = False
a ,b, old = bisection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = bisection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [-2,-1] bisection loops " + str(loops)+ " times and the root is " + str(mid))

a = 1.0
b = 2.0
loops = 1
accurate = False
a ,b, old = bisection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = bisection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [ 1, 2] bisection loops " + str(loops)+ " times and the root is " + str(mid))

a = -1.75
loops = 1
accurate = False
old = newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x = -1.75 Newton-Raphson loops " + str(loops) + " times and the root is " + str(a))

a = 0.3
loops = 1
accurate = False
old = newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x =  0.3 Newton-Raphson loops " + str(loops) + " times and the root is " + str(a))

a = 1.75
loops = 1
accurate = False
old = newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x =  1.75 Newton-Raphson loops " + str(loops) + " times and the root is " + str(a))

a = -1.75
b = -2
loops = 1
accurate = False
new, old = secant(a, b)
while(not(accurate)):
    loops += 1
    new, old = secant(new, old)        
    accurate = accuracy(new, old, 10**-5)
print("For x0 = -1.75 and x1 = -2 secant loops " + str(loops) + " times and the root is " + str(new))

a = 0.3
b = 0.5
loops = 1
accurate = False
new, old = secant(a, b)
while(not(accurate)):
    loops += 1
    new, old = secant(new, old)        
    accurate = accuracy(new, old, 10**-5)
print("For x0 = 0.3 and x1 = 0.5 secant loops " + str(loops) + " times and the root is " + str(new))

a = 1.75
b = 2
loops = 1
accurate = False
new, old = secant(a, b)
while(not(accurate)):
    loops += 1
    new, old = secant(new, old)        
    accurate = accuracy(new, old, 10**-5)
print("For x0 =  1.75 and x1 =  2 secant loops " + str(loops) + " times and the root is " + str(new))