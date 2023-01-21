dato1 = "Hola"
dato2 = "Mundo"

datoFinal = dato1 + " " + dato2
print(datoFinal)

# PORCENTAJES
print("El saludo es: %s %s" %(dato1,dato2))

#FORMAT POR INDEX
saludo = "Saludo2 {0} {1}".format(dato1, dato2)
print(saludo)

#FORMAT POR VARIABLES
saludo = "Saludo3 {a} {b}".format(a=dato1, b=dato2)
print(saludo)