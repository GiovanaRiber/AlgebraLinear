#!/usr/bin/env python
# coding: utf-8

# In[3]:

from sympy import symbols, Matrix, Rational, diag

# In[4]:

A = Matrix ([[1, 2], [3, 0], [-1, 4]])
A

# In[5]:

B = Matrix(2, 3, [1, 2, -1, 3, 0, 4]) #2, 3 = indicação das linhas colunas
B

# In[6]:

C = Matrix ([[1, 2, 3]]) #Matriz linha
C

# In[7]:

D = Matrix([1, 2, 3]) #Matriz coluna
D

# In[8]:

E = Matrix(3, 3, [1, 2, 3, 1, 2, 3, 1, 2, 3]) #Matriz quadrada
E

# In[9]:

E1 = Matrix([[3, 2, 1],[3, 2, 1], [3, 2, 1]]) #Matriz quadrada
E1

# In[10]:

diag (1, 2, 3) #Elemntos da diagonal da matriz; O restantes dos elementos são 0

# In[11]:

A [2, 1] #se for necessário encontrar um elemento específico de acordo com os índices

# In[12]:

a = list(A) #Transforma a matriz em uma lista, tal qual uma lista
a

# In[13]:

B.shape #Dimensões/tamanho da matriz

# In[14]:

E.shape

# In[15]:

x, y, z = symbols("x:z")

# Operações

# In[16]:

G = Matrix([[x, y, z],[x+1, y+1, z+1]])
G

# In[17]:

F = Matrix([x, y, z])
F

# In[18]:

G + B #Só se pode somar matrizes de mesma ordem -> comutativa
      #G+F não dará certo

# In[19]:

G - B #Só se pode subtrair matrizes de mesma ordem -> diferente

# In[20]:

B - G

# In[21]:

from sympy import zeros, ones, eye

# In[22]:

zeros(2) #Matiz nula

# In[23]:

ones(3) #Todos os elementos são 1

# In[24]:

eye(4) #Matriz quadrada com diagonal com elemento 1, o restante é zero -> Matriz identidade

# In[32]:

from sympy import symbols, Matrix, Rational
Z = Matrix([[x-1, -1, 3],[-2, x, -6], [-1, 1, x-5]])
Z

# In[35]:

Z.det()

# In[49]:

b = symbols("b")
a = symbols("a")
N = Matrix([[x-3, -2],[-a, x-b]])
N

# In[50]:

N.det()

# In[ ]: