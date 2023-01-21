miDiccionario = {
    "Matricula": 1234,
    "Nombre": "Roberto",
    "Apellidos": "Cardiel"
}

print(type(miDiccionario)) # <class 'dict'>
print(miDiccionario) # {'Matricula': 1234, 'Nombre': 'Roberto', 'Apellidos': 'Cardiel'}

print(miDiccionario["Nombre"]) # Roberto

miDiccionario["Email"] = "rcardiel@gmail.com" 
print(miDiccionario["Email"]) # rcardiel@gmail.com