#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from scipy.optimize import linprog
from sympy import Symbol
from sympy import Rational

# Um comerciante vende dois tipos de artigos, e B. Na venda do artigo A, tem um lucro de 20 por unidade, e na venda do artigo B, tem um lucro de 30. Em seu depósito, só cabem 100 artigos, e sabe-se que por compromissos já assumidos, ele venderá 15 artigos do tipo A e 25 do tipo B.
# O distribuidor pode entregar ao comerciante, no máximo, 60 artigos A e 50 artigos B. Quantos artigos de cada tipo o comerciante deverá encomendar do distribuidor para que supondo que venda todos, obtenha o lucro máximo?
# 

# In[ ]:

from scipy.optimize import linprog

# Coeficientes da função objetivo
c = [-20, -30]

# Coeficientes das restrições de desigualdade (escrevendo Ax <= b)
A = [
    [1, 1],    # A + B <= 100
    [-1, 0],   # -A <= -15 => A >= 15
    [0, -1],   # -B <= -25 => B >= 25
    [1, 0],    # A <= 60
    [0, 1]     # B <= 50
]

# Resultados das desigualdades
b = [100, -15, -25, 60, 50]

resultado = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')
print("Quantidade do artigo A:", resultado.x[0])
print("Quantidade do artigo B:", resultado.x[1])
print("Ganho Máximo:", -resultado.fun)


# In[ ]:


from scipy.optimize import linprog

# Coeficientes da função objetivo
c = [10, 14, 12, 15]

# Coeficientes das restrições de desigualdade
A = [
    [1, 1, 0, 0],   # D1 <= 40
    [0, 0, 1, 1]    # D2 <= 50
]

# Lados direitos das desigualdades
b = [40, 50]

# Coeficientes das restrições de igualdade
A_eq = [
    [1, 0, 1, 0],   # Cliente A = 30
    [0, 1, 0, 1]    # Cliente B = 40
]

# Lados direitos das igualdades
b_eq = [30, 40]

# Resolvendo o problema com as novas restrições
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')

# Exibindo o resultado
print("Quantidade a ser enviada do depósito D1 para o cliente A:", result.x[0])
print("Quantidade a ser enviada do depósito D1 para o cliente B:", result.x[1])
print("Quantidade a ser enviada do depósito D2 para o cliente A:", result.x[2])
print("Quantidade a ser enviada do depósito D2 para o cliente B:", result.x[3])
print("Custo total mínimo de transporte:", result.fun)


# In[ ]:


from scipy.optimize import linprog

# Coeficientes da função objetivo
c = [3, 2]  # Custo de P e Q

# Coeficientes das restrições
A = [
    [-3, -1],  # Vitamina A
    [-3, -4],  # Vitamina B
    [-2, -7]   # Vitamina C
]

# Resultados das desigualdades
b = [-12, -30, -28]

bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

print("Quantidade de produto P a ser comprada:", result.x[0])
print("Quantidade de produto Q a ser comprada:", result.x[1])
print("Custo total mínimo:", result.fun)


# In[ ]:

from scipy.optimize import linprog

# Coeficientes da função objetivo
c = [-0.1, -0.07]

# Coeficientes das restrições de desigualdade (escrevendo Ax <= b)
A = [
    [1, 1],    # A + B <= 10000
    [1, 0],    # A <= 0
    [0, -1]     # B <= 2000
]

# Resultados das desigualdades
b = [10000, 6000, -2000]

resultado = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')
print("Quantidade investida no titulo A:", resultado.x[0])
print("Quantidade investida no titulo B:", resultado.x[1])
print("Ganho Máximo:", -resultado.fun)