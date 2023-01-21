def suma(x,y):
    print("LA SUMA DE {} + {} ES IGUAL A {}".format(x,y,(x+y)))

def resta(x,y):
    print("LA RESTA DE {} - {} ES IGUAL A {}".format(x,y,(x-y)))

def division(x,y):
    print("LA DIVISION DE {} ENTRE {} ES IGUAL A {}".format(x,y,(x/y)))

def multiplicacion(x,y):
    print("LA MULTIPLICACION DE {} POR {} ES IGUAL A {}".format(x,y,(x*y)))

def pedir():
    print('''
    MENU DE OPERACIONES:
    1. SUMA
    2. RESTA
    3. DIVISION
    4. MULTIPLICACION
    5. SALIR
    ''')


def main():
    operacion = 0
    numero1 = int(input("Dame el numero 1: "))
    numero2 = int(input("Dame el numero 2: "))

    while operacion != 5:
        pedir()
        operacion = int(input("Dame la operacion a realizar: "))
        if operacion == 1:
            suma(numero1,numero2)
        elif operacion == 2:
            resta(numero1,numero2)
        elif operacion == 3:
            division(numero1,numero2)
        elif operacion == 4:
            multiplicacion(numero1,numero2)
    
    print("BYE")

main()
