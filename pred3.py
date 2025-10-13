#List
>>> L = []
>>> print(L)
[]
>>> L = [1,3,-7,19]
>>> print(L)
[1, 3, -7, 19]
>>> L.append(52)
>>> print(L)
[1, 3, -7, 19, 52]
>>> L.append('Hello world')
>>> print(L)
[1, 3, -7, 19, 52, 'Hello world']
>>> L[0]
1
>>> L[3]
19
>>> L[4]
52
>>> L[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> len(L)
6
>>> L[-1]
'Hello world'
>>> L[-6]
1
>>> L[-7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> c = L[0] + L[2]
>>> print(c)
-6
>>> print(L[1])
3
>>> L[5] = 2025
>>> print(L)
[1, 3, -7, 19, 52, 2025]
>>> L2 = [1,2,5, [17, -1, 19]]
>>> L2[0]
1
>>> L2[1]
2
>>> L2[3]
[17, -1, 19]
>>> L2[3][2]
19
>>> L2.pop()
[17, -1, 19]
>>> print(L2)
[1, 2, 5]
>>> L2.pop()
5
>>> print(L2)
[1, 2]
>>> L2.pop(0)
1
>>> print(L2)
[2]
>>> print(L)
[1, 3, -7, 19, 52, 2025]
>>> L.insert(2, 1234)
>>> print(L)
[1, 3, 1234, -7, 19, 52, 2025]

#List slices
>>> L[0:4]
[1, 3, 1234, -7]
>>> L[2:4]
[1234, -7]
>>> L[0:4:2]
[1, 1234]
>>> L[0:5:2]
[1, 1234, 19]
>>> L=[0,1,2,3,4,5,6]
>>> L[0:5:2]
[0, 2, 4]
>>> L[:3]
[0, 1, 2]
>>> L[2:]
[2, 3, 4, 5, 6]
>>> L[:]
[0, 1, 2, 3, 4, 5, 6]
>>> L[5:0:-1]
[5, 4, 3, 2, 1]
>>> L[::-1]
[6, 5, 4, 3, 2, 1, 0]
>>> T = 'Hello world'
>>> T[0]
'H'
>>> len(T)
11
>>> T[-1]
'd'
>>> T[::-1]
'dlrow olleH'
>>> T[0]='h'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> T[::2]
'Hlowrd'
>>> c = T[0]
>>> c
'H'
>>> ord(c)
72
>>> chr(72)
'H'

#Stack
>>> S = []
>>> S.append('M')
>>> S.append('T')
>>> S
['M', 'T']
>>> S.append('W')#
>>> S
['M', 'T', 'W']
>>> S.append('T')#
>>> S.append('F')
>>> S.append('S')
>>> S.append('S')
>>> S
['M', 'T', 'W', 'T', 'F', 'S', 'S']
>>> S.pop()
'S'
>>> S
['M', 'T', 'W', 'T', 'F', 'S']
>>> S.pop()
'S'
>>> M
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'M' is not defined
>>> S
['M', 'T', 'W', 'T', 'F']
>>> S.pop()
'F'
>>> S.pop()
'T'
>>> S.pop()
'W'
>>> S
['M', 'T']
>>> S.pop()
'T'
>>> S.pop()
'M'
>>> S
[]
>>> S.pop()

#Queue
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>> Q=[]
>>> Q.append('M')
>>> Q.append('T')
>>> Q.append('W')
>>> Q.append('T')
>>> Q.append('F')
>>> Q.append('S')
>>> Q.append('S')
>>> Q
['M', 'T', 'W', 'T', 'F', 'S', 'S']
>>> Q,.pop(0)
  File "<stdin>", line 1
    Q,.pop(0)
      ^
SyntaxError: invalid syntax
>>> Q.pop(0)
'M'
>>> Q
['T', 'W', 'T', 'F', 'S', 'S']
>>> Q.pop(0)
'T'
>>> Q
['W', 'T', 'F', 'S', 'S']

#Priority queue
>>> from queue import *
>>> PQ = PriorityQueue()
>>> PQ.put((1, 'M'))
>>> print(PQ)
<queue.PriorityQueue object at 0x000001E2FD276290>
>>> PQ.put((0, 'T'))
>>> PQ.put((9, 'W'))
>>> PQ.put((-2, 'S'))
>>> PQ.get()
(-2, 'S')

#Tuple
>>> N = (1, 3, 5, 6, 7, 8, 9)
>>> N[::-1]
(9, 8, 7, 6, 5, 3, 1)
>>> N[0] = 456
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> 6 in N
True
>>> 6 in L
True
>>> L
[0, 1, 2, 3, 4, 5, 6]
>>> N
(1, 3, 5, 6, 7, 8, 9)
>>> 7 in L
False

#Set
>>> S = {1, 2,3,4,5,6,7,8,9}
>>> S[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> 5 in S
True
>>> S = {1, 2,3,4,5,6,7,8,9, 1}
>>> S.add(20)
>>> S
{1, 2, 3, 4, 5, 6, 7, 8, 9, 20}
>>> S.pop()
1
>>> S1 = {1, 2, 3, 4, 5, 6}
>>> S2 = {4, 5, 6, 7, 8}
>>> S3 = S1.union(S2)
>>> S3
{1, 2, 3, 4, 5, 6, 7, 8}
>>> S4 = S1.intersection(S2)
>>> S4
{4, 5, 6}
>>> S5 = S1.difference(S2)
>>> S5
{1, 2, 3}
>>> S6 = S2.ddiference(S1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'ddiference'. Did you mean: 'difference'?
>>> S6 = S2.difference(S1)
>>> S6
{8, 7}

#Dictionary
>> D={1234:['Jan','Novak',22], 5678:['Jana', 'Novotna', 21]}
>>> D
{1234: ['Jan', 'Novak', 22], 5678: ['Jana', 'Novotna', 21]}
>>> 1234 in D
True
>>> D.get(5678)
['Jana', 'Novotna', 21]
