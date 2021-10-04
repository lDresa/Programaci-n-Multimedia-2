'''
programa que realiza tres acciones con un humano
'''

class Humano:
    cerebro = 1
    corazon = 1
    razonamiento = True
    organos = True
    brazos = True
    piernas = True
    cansancio = 0

    def caminar(self):
        print("La persona camina 10 pasos")
    def saltar(self):
        print("La persona salta")
    def saludar(self):
        print("La persona te saluda")

Mateo = Humano()
Daniela = Humano()
Tomas = Humano()

Mateo.caminar()
Mateo.saltar()
Mateo.saludar()