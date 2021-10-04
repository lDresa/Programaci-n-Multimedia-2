class Television:
    canales = 42
    control = True
    volumen = 100
    señal = "buena"
    smarttv = False

    def encender(self):
        print("La television se enciende")
    def cambiar(self):
        print("La television se ha cambiado 1 canal")
    def subirVol(self):
        print("Se ha subido el volumen 2 unidades")
    def bajarVol(self):
        print("Se ha bjado el volumen 2 unidades")
    def apagar(self):
        print("Se ha apagado la television")

LG = Television()

LG.encender()
LG.cambiar()
LG.subirVol()
LG.bajarVol()
LG.apagar()