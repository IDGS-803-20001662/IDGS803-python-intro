# HERENCIA
class padre():
    x=1


class operasbas(padre):
    # Definir propiedades de clase
    num1=0
    num2=0
    res=0
    # Definir constructor de la clase
    # def __init__(self, *args):

    # Definir los metodos
    def suma(self, a, b):
        self.num1=a
        self.num2=b
        return a+b

obj = operasbas()