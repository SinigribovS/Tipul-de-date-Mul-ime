#PROGRAMEAZĂ! Scrieţi un program care citeşte de la tastatură elementele
#mulţimilor A şi B şi afişează pe ecran:
#a) intersecţia mulţimilor A şi B;
#b) reuniunea mulţimilor A şi B;
#c) diferenţa mulţimilor A şi B.
#Mulţimile A şi B sunt formate din numere întregi.

A=set(filter(str.isdigit,str(input('Introduceți elementele mulțimii A: '))))
B=set(filter(str.isdigit,str(input('Introduceți elementele mulțimii B: '))))
print('Intersecția: ', A.intersection(B))
print('Reuniunea: ', A.union(B))
print('Diferența (A-B): ', A.difference(B)) 
print('Diferența (B-A): ', B.difference(A))