'''
Ejercicio B-2: Funcion de Operaciones
'''

print('''Este programa generará cuatro operaciones aritméticas con dos numeros
que usted asigne''')

def operaciones():
    num1 = float(input("Escriba su primer numero: "))
    num2 = float(input("Escriba su segundo numero: "))

    suma = num1 + num2
    resta = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    print("Suma:", suma, "| Resta:", resta, "| Multiplicación:", mult, "| División:", div)

operaciones()
