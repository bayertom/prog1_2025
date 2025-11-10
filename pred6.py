#Factorial, definition
def fact(n):
    fn = 1

    while n > 1:
        fn = n * fn
        n = n - 1
        
    return fn

def fact2(n=1):
    fn = 1

    while n > 1:
        fn = n * fn
        n = n - 1
        
    return fn

def calc(a, b):
    c = a + b
    d = a - b
    e = a * b
    
    return c, d, e

def calc2(a, b):
   return a + b, a - b, a * b

def f1(a):
    print(a)
    print(id(a))
    a = a + 1
    print(a)
    print(id(a))
    
def f2(L):
    print(L)
    print(id(L))
    L[0] = 1233
    print(L)
    print(id(L))
    L.append(2025)
    print(L)
    print(id(L))
    
def dist(dx = 0, dy = 0):
    return (dx*dx + dy * dy)**(0.5)

def comb(n, k):
    fn = fact(n)
    fnk = fact(n-k)
    fk = fact(k)
    
    return fn / (fk * fnk)

def comb2(n, k, funct):
    fn = funct(n)
    fnk = funct(n-k)
    fk = funct(k)
    
    return fn / (fk * fnk)

def fsum(*X):
    sum = 0
    for x in X:
        sum = sum + x
    print(sum)

#Factorial
n=5
fn = fact(n)
print(fn)
n=10
fn2 = fact(n)
print(fn2)

#Return multiple values
a1 = 5
b1 = 10

v1, v2, v3 = calc(a1, b1)
print(v1, v2, v3)

v4, v5, v6 = calc2(a1, b1)
print(v4, v5, v6)

#Immutable object
a = 1
print(a)
print(id(a))
a = a + 1
print(a)
print(id(a))

#Mutable object
L = []
print(id(L))
L.append(1)
print(id(L))
L.append(2)
print(id(L))

#Immutable object, pass by value
a1 = 10;
print(id(a1))
f1(a1)
print(id(a1))
print(a1)

#Mutable object, pass by value
L = [1, 2, 3, 4]
print(L)
print(id(L))
f2(L)
print(L)
print(id(L))

#Default values
n = 10
fn = fact2(10)
fn2 = fact2()

dx = 3
dy = 4
d = dist(dy)
print(d)

#Compute (n, k)
n = 10
k = 5
c1 = comb(n,k)
c2 = comb2(n, k, fact)

#Positional arguments, compute sum
fsum(1, 2, 3, 4, 5)