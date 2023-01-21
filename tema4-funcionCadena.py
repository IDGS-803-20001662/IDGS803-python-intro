texto = "Universidad tecnologica de leon"

print(type(texto)) # <class 'str'>
print(texto.lower()) # universidad tecnologica de leon
print(texto.upper()) # UNIVERSIDAD TECNOLOGICA DE LEON
print(texto.title()) # Universidad Tecnologica De Leon
print(texto.find("de")) # 24
print(texto.count("a")) # 2
texto2 = texto.replace("e","3") 
print(texto2) # Univ3rsidad t3cnologica d3 l3on
texto3 = texto.split(" ")
print(texto3) # ['Universidad', 'tecnologica', 'de', 'leon']