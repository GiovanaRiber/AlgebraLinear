#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from sympy import symbols, Matrix, Rational, diag

# In[ ]:

A = Matrix ([[2, 1, 2, 1], [3, 2, 2, 10], [5, 5, 3, 7]])
A

# In[ ]:


A[0,:] = Rational(1,2)* A[0,:]
A


# In[ ]:

A[1,:] = -3*A[0,:] + A[1,:]
A

# In[ ]:

A[2,:] = -5*A[0,:] + A[2,:]
A

# In[ ]:

A[1,:] = Rational(2) * A[1,:]
A

# In[ ]:

B = Matrix ([[1, -3, 2], [4, 0, -5]])
B

# In[ ]:

C = Matrix ([3, 1, 2])
C

# In[ ]:

B*C

# In[ ]:

B1 = Matrix ([[3, 0], [-1, 2], [4, 1]])
B1

# In[ ]:

C1 = Matrix ([2, -5])
C1

# In[ ]:

B1*C1

# In[ ]:

# O traço de uma matriz é a soma dos elementos da diagonal principal

# In[ ]:

AA = Matrix([[2, -5], [-1, 3]])
AA

# In[ ]:

BB = Matrix ([[3, 5], [1, 2]])
BB

# In[ ]:

AA*BB

# In[ ]:

CC = Matrix([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
CC

# In[ ]:

CC.inv()

# In[ ]:

#Se o determinante da matriz for 0, então os vetores que a compõem são linearmente dependentes
#Se o determinante da matriz for diferente de 0, então os vetores que a compõem são linearmente independentes
CC.det()

# In[ ]:

#Uma matriz quadrada é singular se possui uma coluna ou linha de zeros
#Se o determinante de uma matriz for diferente de zer0, então há matriz inversa
