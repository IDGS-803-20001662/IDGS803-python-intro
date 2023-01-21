numero = int(input("Dame el numero: "))

def generarTabla(numero):
    for x in range(1,11):
        print ("{} x {} = {}".format(numero,x,(numero*x)))

generarTabla(numero)