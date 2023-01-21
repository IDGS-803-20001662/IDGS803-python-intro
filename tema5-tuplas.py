tupla = (1,2,3,4)

print(type(tupla)) # <class 'tuple'>
print(tupla) # (1, 2, 3, 4)

tupla2 = (7, "Roberto", True, 23.9, 12+3j)
print(tupla2) # (7, 'Roberto', True, 23.9, (12+3j))

tupla3 = tupla + tupla2
print(tupla3) # (1, 2, 3, 4, 7, 'Roberto', True, 23.9, (12+3j))

print(tupla2[1]) # Roberto

print(tupla2[:]) # (7, 'Roberto', True, 23.9, (12+3j))

print(tupla2[:4]) # (7, 'Roberto', True, 23.9)

print(tupla2[2:]) # (True, 23.9, (12+3j))

print(tupla2[-1]) # (12+3j)
