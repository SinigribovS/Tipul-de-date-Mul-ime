#Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii {1, 2, 3, 4}.

A=set({1, 2, 3, 4})
from itertools import combinations
A1=combinations(A, 1)
A2=combinations(A, 2)
A3=combinations(A, 3)
A4=combinations(A, 4)
subset1=set(A1)
subset2=set(A2)
subset3=set(A3)
subset4=set(A4)
print(subset1, subset2, subset3,subset4)