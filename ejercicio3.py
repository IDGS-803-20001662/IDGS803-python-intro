class operaciones():
    num1=0
    num2=0

    def suma(self,x,y):
        self.num1=x
        self.num2=y
        print("LA SUMA DE {} + {} ES IGUAL A {}".format(x,y,(x+y)))

    def resta(self,x,y):
        self.num1=x
        self.num2=y
        print("LA RESTA DE {} - {} ES IGUAL A {}".format(x,y,(x-y)))

    def division(self,x,y):
        self.num1=x
        self.num2=y
        print("LA DIVISION DE {} ENTRE {} ES IGUAL A {}".format(x,y,(x/y)))

    def multiplicacion(self,x,y):
        self.num1=x
        self.num2=y
        print("LA MULTIPLICACION DE {} POR {} ES IGUAL A {}".format(x,y,(x*y)))
    
    def pedir(self):
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
        obj = operaciones()
        obj.pedir()
        operacion = int(input("Dame la operacion a realizar: "))
        if operacion == 1:
            obj.suma(numero1,numero2)
        elif operacion == 2:
            obj.resta(numero1,numero2)
        elif operacion == 3:
            obj.division(numero1,numero2)
        elif operacion == 4:
            obj.multiplicacion(numero1,numero2)
    
    print("BYE")

if __name__=="__main__":
    main()


