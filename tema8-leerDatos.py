print("Pedir unos numeros")

# CONVERSION DE DATOS NECESARIA -> INT()
num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))

print("La suma de {} + {} = {}".format(num1, num2, (num1 + num2)))
# La suma de 1 + 2 = 3

# INT - numeros sin punto decimal
# FLOAT - numeros con punto decimal
# STR - cadenas

dato1 = 100
dato2 = "23.7"

print(len(str(dato1))) # 3
print(float(dato2)) # 23.7