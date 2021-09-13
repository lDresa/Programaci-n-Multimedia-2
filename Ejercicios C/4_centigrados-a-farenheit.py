'''
funcion que convierte la temperatura en centigrados a farenheit
'''

def temperatura(c):
    f = (float(input("Cual es la temperatura en centigrados?: ")) * 9/5) + 32
    return f 

print("La temperatura en Farenheit es: ", temperatura(0))