class OperacionesAritmeticas():
    def ingresoNumeros(self):
        numero1 = float(input("Ingrese sumando uno: "))
        numero2 = float(input("Ingrese sumando dos: "))
        return numero1, numero2


    def suma(self, numero1, numero2):
        return numero1 + numero2

if __name__=='__main__':
    operacion = OperacionesAritmeticas()
    num1, num2 = operacion.ingresoNumeros()
    print(f"{num1} + {num2} = {operacion.suma(num1, num2)}")
