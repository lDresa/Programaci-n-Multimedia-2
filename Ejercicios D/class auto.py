class Auto:
    marca = "Subaru"
    modelo = "BRZ"
    tipo = "Sedan"
    llantas = 4
    puertas = 2
    volante = True
    transimison_auto = False
    traccion = "trasera"
    stock = True
    color = "blanco"

    def abrirPiloto(self):
        print("La puerta del piloto se abre y se cierra")
    def abrirPasajero(self):
        print("La puerta del pasajero se abre y se cierra")
    def encender(self):
        print("El auto se enciende")
    def avanzar(self):
        print("El auto avanza a su destino")
    def estacionar(self):
        print("El auto se estaciona")

brz = Auto()

brz.abrirPiloto()
brz.abrirPasajero()
brz.encender()
brz.avanzar()
brz.estacionar()