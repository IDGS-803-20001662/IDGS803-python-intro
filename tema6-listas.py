lista1 = [1,2,3,4,5]
# DIFERENCIA ENTRE LISTAS Y ARREGLOS:
# EN LAS LISTAS PUEDES ALMACENAR DATOS DE DIFERENTES TIPOS, EN LOS ARREGLOS NO

lista2 = [1,3,5, "Roberto", True]

print(lista1[-1]) # 5
print(lista1[:2]) # [1, 2]
print(lista1[3:]) # [4, 5]
print(lista1[1:3]) # [2, 3]

lista2.append("Laura")
print(lista2) # [1, 3, 5, 'Roberto', True, 'Laura']

lista2.insert(3, "Juan")
print(lista2) # [1, 3, 5, 'Juan', 'Roberto', True, 'Laura']

lista2.remove("Roberto")
print(lista2) # [1, 3, 5, 'Juan', True, 'Laura']

lista2.pop()
print(lista2) # [1, 3, 5, 'Juan', True]

del lista2[2]
print(lista2) # [1, 3, 'Juan', True]