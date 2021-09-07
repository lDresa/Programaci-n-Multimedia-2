'''
Ejercicio B-1: Funcion de Calculadora de IMC
'''

print("Este programa te indicará tu indice de masa corporal (IMC)")

def indice():
    peso = float(input("Escriba su peso (kg): "))
    altura = float(input("Escriba su altura (m): "))

    imc = peso / altura**2

    print("Su imc es:", imc)

    if imc<=18.5:
        print("Su IMC está por debajo de lo normal (<18.5)")
    elif imc<=24.9:
        print("Su IMC es normal (18.6-24.9)")
    elif imc<=29.9:
        print("Su IMC indica sobrepeso (25-29.9)")
    else:
        print("Su IMC indica obesidad (>30)")
        
indice()
