'''
funcion que imprime todas las vocales dentro de una oracion
'''

def contar_vocales():
    oracion = input("Escriba una oracion: ")
    print("El numero de vocales (en orden de a,e,i,o,u) es:")
    print(*map(oracion.lower().count, "aeiou"))

contar_vocales()