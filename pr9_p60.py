#PROGRAMEAZĂ! Scrieţi un program care citeşte de la tastatură elementele
#mulţimilor A şi B şi afişează pe ecran:
#a) intersecţia mulţimilor A şi B;
#b) reuniunea mulţimilor A şi B;
#c) diferenţa mulţimilor A şi B;
#Mulţimile A şi B sunt formate din literele mari ale alfabetului latin.

A=set(filter(str.isupper, filter(lambda x: x not in ['',' ',',',';','1','2','3','4','5','6','7','8','9'],str(input('Introduceti elementele multimii A: ')))))
B=set(filter(str.isupper, filter(lambda x: x not in ['',' ',',',';','1','2','3','4','5','6','7','8','9'],str(input('Introduceti elementele multimii B: ')))))
print(f'Intersectia: ',A.intersection(B))
print('Reuniunea: ',A.union(B))
print('Diferenta (A-B): ',A.difference(B))
print('Diferenta (B-A): 'B.difference(A))