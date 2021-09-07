'''
Cuadrado de numero con float(input)
'''

print('''Este pequeño programa encontrará el cuadrado de cualquier número
que usted le asigne.''')

def cuadrado():
    numero = float(input("Escruba un número: "))
    print("el cuadrado de", numero, "es", (numero**2))

cuadrado()
