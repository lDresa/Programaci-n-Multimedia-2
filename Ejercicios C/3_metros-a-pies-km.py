'''
programa de conversion de metros a pies y kilometros
'''
def conversor():
    num = float(input("Escriba la distancia (m) que desea convertir: "))

    pies = num * 3.281
    km = num / 1000

    print("La distancia en pies (ft) es: ", pies, ", y en kilometros es: ", km)

conversor()