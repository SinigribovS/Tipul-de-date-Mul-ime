#Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii {’A’, ’B’, ’C’, ’D’}.

x=set({'A', 'B', 'C', 'D'})
from itertools import combinations
x1=combinations(x, 1)
x2=combinations(x, 2)
x3=combinations(x, 3)
x4=combinations(x, 4)
subset1=set(x1)
subset2=set(x2)
subset3=set(x3)
subset4=set(x4)
print(subset1, subset2, subset3, subset4)