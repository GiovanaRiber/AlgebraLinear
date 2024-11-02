#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from sympy import symbols, Matrix, Rational, diag

# In[ ]:

A = Matrix ([[3, 0], [-1, 2], [1, 1]])
A

# In[ ]:

B = Matrix ([[4, -1], [0, 2]])
B

# In[ ]:

C = Matrix ([[1, 4, 2], [3, 1, 5]])
C

# In[ ]:

D = Matrix ([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
D

# In[ ]:

E = Matrix ([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])
E

# In[ ]:

D + E

# In[ ]:

D - E

# In[ ]:

At = Matrix([[3, -1, 1], [0, 2, 1]])
At

# In[ ]:

(At * 2) + C

# In[ ]:

x, y, z = symbols ("x:z")

# In[ ]:

a = Matrix ([[x, y, z], [x, y, -4*z], [-4*x, y, z]])
a

# In[ ]:

a.det()

# In[ ]:

aa = Matrix ([[1, 1, 1], [1, 1, -4], [-4, 1, 1]])
aa

# In[ ]:

aa.det()

# In[ ]:

aaa = a.inv()
aaa

# In[ ]:

aa.inv()

# In[ ]:

aa1 = Matrix ([[5, 1, 1], [10, 1, -4], [0, 1, 1]])
aa1

# In[ ]:

aa2 = Matrix([[1, 5, 1], [1, 10, -4], [-4, 0, 1]])
aa2

# In[ ]:

aa3 = Matrix([[1, 1, 5], [1, 1, 10], [-4, 1, 0]])
aa3

# In[ ]:

aa1.det()

# In[ ]:

aa2.det()

# In[ ]:

aa3.det()

# In[ ]:

bb = Matrix([[1, 1, 3], [2, 5, 5], [3, 5, 8]])
bb

# In[ ]:

bb.det()

# In[ ]:

bb.inv()

# In[ ]:

a, b, c = symbols ("a:c")

# In[ ]:

bb1 = Matrix([[a, 1, 3], [b, 5, 5], [c, 5, 8]])
bb1

# In[ ]:

bb2 = Matrix ([[1, a, 3], [2, b, 5], [5, c, 8]])
bb2

# In[ ]:

bb3 = Matrix([[1, 1, a], [2, 5, b], [3, 5, c]])
bb3

# In[ ]:

bbb = bb1.det()
bbb

# In[ ]:

bb2.det()

# In[ ]:

bb3.det()

# In[ ]:

bbb * -1

# In[ ]:

v = Matrix ([[x, -1], [3, 1-x]])
v

# In[ ]:

v.det()

# In[ ]:

m = Matrix ([[2, 4, 8], [-1, 1, -1], [3, 2, 8]])
m

# In[ ]:

m[0,:] = Rational(1,2) * m[0,:]
m

# In[ ]:

m[1,:] = 1*m[0,:] + m[1,:]
m

# In[ ]:

m[2,:] = -3*m[0,:] + m[2,:]
m

# In[ ]:

m[1,:] = Rational(1,3) * m[1,:]
m

# In[ ]:

m[2,:] = 4*m[1,:] + m[2,:]
m

# In[ ]:

c = Matrix([[-1, 1, 1], [3, -1, 0], [2, -4, -5]])
c

# In[ ]:

c.det()

# In[ ]:

h = Matrix([[1, -2, 3], [-3, 6, 9], [-2, 4, -6]])
h

# In[ ]:

h.det()
