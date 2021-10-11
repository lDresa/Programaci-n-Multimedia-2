class Barcos:
    via = "mar"
    proa = 1
    pop = 1
    babor = 1
    estribor = 1
    amuras = 1
    aletas = 1
    chimenea = 1
    cubierta = 1
    ancla = 1
    propulsion = ["remo","motor","vela"]

    def __init__(self,t,m,c):
        self.tamano = t
        self.material = m
        self.color = c

b_pirata = Barcos("pequeño","madera","café")
b_petrolero = Barcos("mediano","acero","blacno y rojo")
b_draga = Barcos("mediano","acero","blanco y verde")
b_crucero = Barcos("grande","acero","blanco")
b_gaseros = Barcos("grande","acero","azul")

def imprimir_Barcos():
    print("> Barco pirata - tamaño:",b_pirata.tamano,", material:",b_pirata.material,", color:",b_pirata.color)
    print("> Barco petrolero - tamaño:",b_petrolero.tamano,", material:",b_petrolero.material,", color:",b_petrolero.color)
    print("> Barco draga - tamaño:",b_draga.tamano,", material:",b_draga.material,", color:",b_draga.color)
    print("> Crucero - tamaño:",b_crucero.tamano,", material:",b_crucero.material,", color:",b_crucero.color)
    print("> Barco gasero - tamaño:",b_gaseros.tamano,", material:",b_gaseros.material,", color:",b_gaseros.color)

imprimir_Barcos()