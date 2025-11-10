from math import *

#Recursion, general function
def f(n):
    print("C(" + str(n)+")")
    
    #Non-recursive solution
    if (n == 1):
        print("D");
        
    #Recursive approach
    else:
        print("f(" + str(n-1) + ")")
        f(n - 1)
        
    print("E(" + str(n) + ")")


def fact(n):
    #Non-recursive solution
    if n == 1:
        return 1
    
    #Recursive approach
    else:
        return n * fact(n-1)
    
    
def fact2(n):
    #Non-recursive solution
    if n > 1:
        return n * fact2(n-1)
    
    #Recursive approach
    else:
        return 1
    
    
def fib(n):
    #Non-recursive solution
    if n<=1:
        print(n)
        return 1
    
    #Two recursive calls
    else:
        print(n)
        return fib(n-1) + fib(n-2)
    
    
def f2(n):
    #Non-recursive solution
    if n == 1:
        return 1
    
    #Recursive approach
    else:
        print('n=', n)
        return n * f2(n-2)
    
    
def maximum(X, l, r):
    #Non-recursive solution
    if r <= l+1:
        return max(X[l], X[r]) 

    #Recursive solution
    else:
        #Mid index
        m = (l + r)//2
        
        #Process left subinterval
        lmax= maximum(X, l, m)
        
        #Process right subinterval
        rmax = maximum(X, m+1, r)
        
        #Return max of both values
        return max(lmax, rmax) 
    
def bSearch(X, a, l, r):
    #Find element using bisection
    #Crossed left and right index, non-recursive solution
    if (l > r):
       return -1      

    #Recursive solution
    else:
        #Mid index
        m = (l + r)//2            

        #Number a equal to mid element
        if a == X[m]:
            return m                      

        #Number in the left subset
        elif a < X[m]:
            return bSearch(X, a, l, m - 1)

        #Number in the right subset
        else:
            return bSearch(X, a, m + 1, r )
            

#Illustration, recursive function
f(3)

#Factorial
fn = fact(4)
print(fn)

#Fibonacci numbers
fb = fib(10)

#Wrong construction
res = f2(3)
#res = f2(4)

#Find maximum
X = [1, 9, 34, 17, -6, 27]
max = maximum(X, 0, len(X)-1)
print(max)

#Find element, binary search
X = [1, 9, 34, 70, 106, 127]
idx = bSearch(X, 106, 0, len(X) - 1)
print(idx)
