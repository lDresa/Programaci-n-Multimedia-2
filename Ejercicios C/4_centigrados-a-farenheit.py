'''
funcion que convierte la temperatura en centigrados a farenheit
'''

def convertir_temp():
    c = (float(input("Cual es la temperatura en centigrados?: ")) * 9/5) + 32
    return c 

print("La temperatura en Farenheit es: ", convertir_temp())