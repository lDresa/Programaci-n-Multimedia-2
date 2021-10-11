'''
programa con clase Autos e inicializador para listar sus caracteristicas
'''

print("Vehiculos importados disponibles")
#clase Autos como plantilla para caracteristicas de vehiculos
class Autos:
    def __init__(self,m,mm,a,p,t,c):
        self.marca = m
        self.modelo = mm
        self.año = a
        self.pasajeros = p
        self.traccion = t
        self.color = c

#inventario (propiedades asignadas a cada vehiculo)
#marca, modelo, año, pasajeros, traccion, color
su_brz = Autos("Subaru","BRZ,","2019,","4 pasajeros,","RWD,","Blanco")
to_supra = Autos("Toyota","Supra,","2021,","2 pasajeros,","RWD,","Rojo")
ni_skyline = Autos("Nissan","Skyline R34,","1999,","4 pasajeros,","AWD,","Azul")
to_gt = Autos("Toyota","GT86,","2016,","4 pasajeros,","RWD,","Gris")
ni_370z = Autos("Nissan","370z,","2009,","2 pasajeros,","RWD,","Negro")

#funcion para imprimir los objetos utilizando los parametros de la clase
def imprimir_Autos():
    print(">",su_brz.marca, su_brz.modelo, su_brz.año, su_brz.pasajeros, su_brz.traccion, su_brz.color)
    print(">",to_supra.marca, to_supra.modelo, to_supra.año, to_supra.pasajeros, to_supra.traccion, to_supra.color)
    print(">",ni_skyline.marca, ni_skyline.modelo, ni_skyline.año, ni_skyline.pasajeros, ni_skyline.traccion, ni_skyline.color)
    print(">",to_gt.marca, to_gt.modelo, to_gt.año, to_gt.pasajeros, to_gt.traccion, to_gt.color)
    print(">",ni_370z.marca, ni_370z.modelo, ni_370z.año, ni_370z.pasajeros, ni_370z.traccion, ni_370z.color)
    
imprimir_Autos()