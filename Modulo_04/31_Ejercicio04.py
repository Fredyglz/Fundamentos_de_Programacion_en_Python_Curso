d1 = {'Adam Smith': 'A', 'Judy':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}
d4 = {}

for elemento in (d1, d2):
    d4.update(elemento)
    for item in elemento:
        d3[item] = elemento[item]
    
print(d3)
print(d4)