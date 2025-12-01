from math import *

def getRadius(per):
    return per/(2*pi)

def getRadius2(per):
    if per >=0:
        return per/(2*pi)
    else:
        return -1
    
def getRadius3(per):
    if per >=0:
        return per/(2*pi)
    else:
        raise ValueError('Negative value')
    
    
def f (a, b):
    if b == 0:
        return -1
    if a/b < 0:
        
        return -2
    
    return sqrt(a/b)

def f2 (a, b):
    try:
        return sqrt(a/b)
    
    except ValueError:
        return -1
    
    except ZeroDivisionError:
        return -2
    
    except TypeError:
        return -3
    
def f3 (a, b):
    try:
        return sqrt(a/b)
        
    except Exception:
            return -1
    

def f4 (a, b):
    try:
        return sqrt(a/b)
    
    except ValueError:
        raise ValueError ('Negative value a/b', a/b)
    
    except ZeroDivisionError:
        raise ZeroDivisionError('b is zero', b)
    
    except Exception:
        raise Exception('Unspecified exception')   



def main():
    sin(1)
    #Sin(1)

    x1 = 1
    x2 = 2 
    x3 = 4
    x4 = 7

    x =0.25*(x1 + x2  + x3 + x4)
    x =0.25*x1 + x2  + x3 + x4
    
    #Get radius,OK
    per = 10
    r = getRadius(per)
    print(r)
    
    #Get radius, error
    per = 10
    r = getRadius(per)
    print(r)
    
    #Get radius,if
    r = getRadius2(per)
    if r >= 0:
        print(r)
    else:
        print('Error')    
    
    #Get radius, raise exception
    r = getRadius3(per)
    if r >= 0:
        print(r)
    else:
        print('Error')    
        
    #Fraction, if
    a = 5
    b = -6
    #b = [-6]
    c = f(a, b)
    if c < 0:
        print('Error')
    else:
        print(c)
        
    #Fraction, try-except
    a = 5
    b = -6
    b = [-6]
    c = f2(a, b)
    if c < 0:
        print('Error')
    else:
        print(c)

    #Fraction, try-except, general
    a = 5
    b = -6
    #b = [-6]
    c = f3(a, b)
    if c < 0:
        print('Error')
    else:
        print(c)

    #Fraction, try-except + raise
    a = 5
    b = -6
    b = [-6]
    try:
        c = f4(a, b)
    except Exception as e:
        print(e)

main()
