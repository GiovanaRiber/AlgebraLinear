#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from sympy import symbols, Matrix, Rational

# In[ ]:

x, y, z = symbols ("x:z")
A = Matrix([[1, 2, -3], [2, 3, 4], [4, 7, -1]])
B = Matrix([x, y, z])
C = Matrix([4, 5, 13])
A

# In[ ]:

B

# In[ ]:

C

# In[ ]:

A*B #Matriz B pode ser interpretada domo um vetor (Multiplicação de matrizes)

# In[ ]:

B*A #dá errado por conta da regra. A quantidade de colunas da matriz A, precisa ser igual ao número de linhas da segunda Matriz

# In[ ]:

A1 = A.inv() #calcula a inversa da mratriz A
A1

# In[ ]:

A * A1 #matriz indentidade

# In[ ]:

A1*C #O produto da inversa por um vetor coluna é uma das soluções do sistema

# In[ ]:

A.det() #calcula o determinante da matriz (número vinculado a matriz). Se o determinante for diferente de 0, a matriz tem inversa

# In[ ]:
a, b = symbols ("a, b")

# In[ ]:
a

# In[ ]:

b

# In[ ]:

A2 = Matrix([[1, 2], [5, 8], [3, 7]])
A2

# In[ ]:

A3 = Matrix([a, b])
A3

# In[ ]:

A2*A3

# In[ ]:

E = Matrix([[1, -1, -3, 0], [4, 3, 2, 0], [4, 6, 8, 0]]) #Matriz homogenia
E

# In[ ]:

#Processo de escalonamento
E[1,:] = -4*E[0,:] + E[1,:]
E

# In[ ]:

E[2,:] = -4*E[0,:] + E[2,:]
E

# In[ ]:

E[1,:] = 1/7*E[1,:]
E

# In[ ]:

E[2,:] = -10*E[1,:] + E[2,:] #Sistema possível e Inderterminado
E

# In[ ]:

c = symbols("c")

# In[ ]:

F = Matrix([[-3, 5, 1, a], [0, -1, 1, b], [4, 2, 3, c]])
F

# In[ ]:

F[0,:] = -Rational(1,3)*F[0,:]
F

# In[ ]:

F[2,:] = -4*F[0,:] + F[2,:]
F

# In[ ]:

F[1,:] = -1*F[1,:]
F

# In[ ]:

F[2,:] = -Rational(26,3)*F[1,:] + F[2,:]
F

# In[ ]:

# In[ ]:

D = Matrix([[1, x],[y,2]])
D, D**2

# In[ ]:

D

# In[ ]:

D**2

# In[ ]:

D.inv() #Forma de mostrar a inversa

# In[ ]:

D**-1 #Forma de mostrar a inversa

# In[ ]:

G = Matrix([[1, 2, 3],[4, 5, 6]])
G

# In[ ]:

G1 = G.applyfunc(lambda x: x+2) #Modificar cada elemento da matriz, qualquer que seja a operação
G1

# In[ ]:

from sympy import pi, cos, Symbol, Integer

# In[ ]:

H = Matrix([[pi/2, pi/3, 0]])
H

# In[ ]:

H1 = H.applyfunc(cos)
H1
