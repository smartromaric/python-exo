# generation of list one
L = [*range(10)]
L2 = [8,88,79]
# unpacking of the list
L3 = [*L,*L2,"end"]
# result is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 88, 79, 'end']
print(L3)

Dic = {'name': 'samrt', 'contact': 123}
Dic2 = {**Dic,"power":"infinity"}
print(Dic2)