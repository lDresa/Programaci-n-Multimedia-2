'''
programa con clase Felinos e inicializador para listar sus caracteristicas
'''
print("Ejemplos de felinos")
#clase Felinos como plantilla para caracteristicas de animales felinos
class Felinos:
    def __init__(self,sf,tm,p,r,dm):
        self.subfamilia = sf #Felinae / Pantherinae
        self.tamaño = tm
        self.peso = p
        self.rugir = r #si / no
        self.domestico = dm #si o no

#objetos con la clase Felinos
tigre = Felinos("Pantherinae,","70-120 cm,","65-310kg,","puede rugir","no es domestico")
leopardo = Felinos("Pantherinae,","57-70 cm,","50-90kg,","puede rugir","no es domestico")
puma = Felinos("Pantherinae,","60-90 cm,","29-100kg,","puede rugir","no es domestico")
leon = Felinos("Pantherinae,","90-120 cm,","130-190kg,","puede rugir","no es domestico")
gato = Felinos("Felinae,","23-25 cm,","3.6-4.5kg,","no puede rugir","es domestico")

#funcion para imprimir los objetos utilizando los parametros de la clase
def imprimir_Felinos():
    print("> El tigre es",tigre.subfamilia, "mide entre",tigre.tamaño, "pesa entre",tigre.peso, tigre.rugir,"y", tigre.domestico)
    print("> El leopardo es",leopardo.subfamilia, "mide entre",leopardo.tamaño, "pesa entre",leopardo.peso, leopardo.rugir,"y", leopardo.domestico)
    print("> El puma es",puma.subfamilia, "mide entre",puma.tamaño, "pesa entre",puma.peso, puma.rugir,"y", puma.domestico)
    print("> El leon es",leon.subfamilia, "mide entre",leon.tamaño, "pesa entre",leon.peso, leon.rugir,"y", leon.domestico)
    print("> El gato es",gato.subfamilia, "mide entre",gato.tamaño, "pesa entre",gato.peso, gato.rugir,"y", gato.domestico)

imprimir_Felinos()