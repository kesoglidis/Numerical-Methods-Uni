import random
import numpy as np

def f(x):
    return 94*np.cos(x)**3 -24*np.cos(x) + 177*np.sin(x)**2 - 108*np.sin(x)**4 - 72*np.cos(x)**3*np.sin(x)**2 - 65

def df(x):
    h = 10e-6
    return (f(x+h)-f(x-h))/(2*h)
    
def ddf(x):
    h = 10e-6
    return (df(x+h)-df(x-h))/(2*h)
    
def accuracy(new, old, accuracy):
    distance = abs(new - old)
    if(distance <= accuracy/2):
        return True
    return False

def randsection(a, b):
    mid = random.uniform(a, b)
    if(f(mid)*f(a) < 0):
        return a , mid, mid
    else:
        return mid , b , mid
        
def mod_newton_raphson(x):
    return x-(2*f(x)*df(x))/(2*df(x)**2 - f(x)*ddf(x))  

def mod_secant(x2, x1, x0):
    q = f(x0)/f(x1)
    r = f(x2)/f(x1)
    s = f(x2)/f(x0)
    diff = (r*(r-q)*(x2-x1)+(1-r)*s*(x2-x0))/((q-1)*(r-1)*(s-1))
    return x2-diff, x2 ,x1

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

#2.1
a = 0
b = 1
loops = 1
accurate = False
a ,b, old = randsection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = randsection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [0,1] randsection loops " + str(loops)+ " times and the root is " + str(mid))

a = 1
b = 2
loops = 1
accurate = False
a ,b, old = randsection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = randsection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [1,2] randsection loops " + str(loops)+ " times and the root is " + str(mid))

a = 2
b = 3
loops = 1
accurate = False
a ,b, old = randsection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = randsection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [2,3] randsection loops " + str(loops)+ " times and the root is " + str(mid))

a = 0.5
loops = 1
accurate = False
old = mod_newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = mod_newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x = 0.5 Halley loops " + str(loops) + " times and the root is " + str(a))

a = 1
loops = 1
accurate = False
old = mod_newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = mod_newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x = 1 Halley loops " + str(loops) + " times and the root is " + str(a))

a = 2.5
loops = 1
accurate = False
old = mod_newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = mod_newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x = 2.5 loops " + str(loops) + " times and the root is " + str(a))

x2 = 0.5
x1 = 0.25
x0 = 0
loops = 1
accurate = False
x2, x1, x0 = mod_secant(x2, x1, x0)
while(not(accurate)):
    loops += 1
    x2, x1, x0 = mod_secant(x2, x1, x0)        
    accurate = accuracy(x2, x1, 10**-5)
print("For x0 = 0, x1 = 0.25 and x2 = 0.5 Muller loops " + str(loops) + " times and the root is " + str(x2))

x2 = 1.2
x1 = 1.1
x0 = 1
loops = 1
accurate = False
x2, x1, x0 = mod_secant(x2, x1, x0)
while(not(accurate)):
    loops += 1
    x2, x1, x0 = mod_secant(x2, x1, x0)        
    accurate = accuracy(x2, x1, 10**-5)
print("For x0 = 1, x1 = 1.1 and x2 = 1.2 Muller loops " + str(loops) + " times and the root is " + str(x2))

x2 = 2.5
x1 = 2.75
x0 = 3
loops = 1
accurate = False
x2, x1, x0 = mod_secant(x2, x1, x0)
while(not(accurate)):
    loops += 1
    x2, x1, x0 = mod_secant(x2, x1, x0)        
    accurate = accuracy(x2, x1, 10**-5)
print("For x0 = 3, x1 = 2.75 and x2 = 2.5 Muller loops " + str(loops) + " times and the root is " + str(x2))

#2.2
result = ""
l = np.empty(10)
for i in range(10):
    a = 2
    b = 3
    loops = 1
    accurate = False
    a ,b, old = randsection(a,b)
    while(not(accurate)):
        loops += 1
        a ,b, mid = randsection(a,b)
        accurate = accuracy(mid, old, 10**-5)
        old = mid
    
    result += str(i + 1) +". " +str(loops) + " "

print(result)

#2.3
a = 0.0
b = 1.0
loops = 1
accurate = False
a ,b, old = bisection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = bisection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [0,1] bisection loops " + str(loops)+ " times and the root is " + str(mid))

a = 1
b = 2
loops = 1
accurate = False
a ,b, old = bisection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = bisection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [1,2] bisection loops " + str(loops)+ " times and the root is " + str(mid))

a = 2
b = 3
loops = 1
accurate = False
a ,b, old = bisection(a,b)
while(not(accurate)):
    loops += 1
    a ,b, mid = bisection(a,b)
    accurate = accuracy(mid, old, 10**-5)
    old = mid
print("For the interval [2,3] bisection loops " + str(loops)+ " times and the root is " + str(mid))

a = 0.5
loops = 1
accurate = False
old = newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x = 0.5 Newton-Raphson loops " + str(loops) + " times and the root is " + str(a))

a = 1
loops = 1
accurate = False
old = newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x = 1 Newton-Raphson loops " + str(loops) + " times and the root is " + str(a))

a = 2.5
loops = 1
accurate = False
old = newton_raphson(a)
while(not(accurate)):
    loops += 1
    a = newton_raphson(old)
    accurate = accuracy(a, old, 10**-5)
    old = a
print("For x = 2.5 Newton-Raphson loops " + str(loops) + " times and the root is " + str(a))

a = 0
b = 0.5
loops = 1
accurate = False
new, old = secant(a, b)
while(not(accurate)):
    loops += 1
    new, old = secant(new, old)        
    accurate = accuracy(new, old, 10**-5)
print("For x0 = 0 and x1 = 0.5 secant loops " + str(loops) + " times and the root is " + str(new))

a = 1
b = 1.2
loops = 1
accurate = False
new, old = secant(a, b)
while(not(accurate)):
    loops += 1
    new, old = secant(new, old)        
    accurate = accuracy(new, old, 10**-5)
print("For x0 = 1 and x1 = 1.2 secant loops " + str(loops) + " times and the root is " + str(new))

a = 2.5
b = 3
loops = 1
accurate = False
new, old = secant(a, b)
while(not(accurate)):
    loops += 1
    new, old = secant(new, old)        
    accurate = accuracy(new, old, 10**-5)
print("For x0 = 2.5 and x1 = 3 secant loops " + str(loops) + " times and the root is " + str(new))