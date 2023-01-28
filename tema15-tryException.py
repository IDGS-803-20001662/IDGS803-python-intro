num1 = 2
num2 = 0

# x = num1/num2 -> ERROR: ZeroDivisionError: division by zero

try:
    x = num1/num2
except:
    print("Error en el programa")
finally:
    print("Programa de try")
