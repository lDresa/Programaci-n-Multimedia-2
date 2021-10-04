'''
programa que realiza tres acciones con un animal
'''

class Animal:
    cerebro = 1
    corazon = 1
    razonamiento = False
    organos = True
    patas = 4
    cansancio = 0

    def correr(self):
        print("El animal corre 20 metros")
    def buscar(self):
        print("El animal busca alimento")
    def acostar(self):
        print("El animal se acuesta a dormir")

oso = Animal()

oso.correr()
oso.buscar()
oso.acostar()