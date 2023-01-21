num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))

if(num1 > num2):
    print("{} es mayor que {}".format(num1,num2))
else:
    print("{} es mayor que {}".format(num2,num1)) # 2 es mayor que 1

print("--------------------------- DATO NUEVO ---------------------------------")
edad = int(input("Date tu edad: "))

if edad > 18: 
    print("Eres mayor de edad") # Eres mayor de edad
elif edad == 18:
    print("Tienes 18")
else:
    print("Eres menor de edad")