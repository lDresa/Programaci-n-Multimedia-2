'''
funcion que regresara el numero mayor
'''

def num_mayor():
    num1 = float(input("Escriba su primer numero: "))
    num2 = float(input("Escriba su segundo numero: "))

    if num1 > num2:
        print("El numero mayor es el primer numero: ", num1)
    else:
        print("El numero mayor es el segundo numero: ", num2)

num_mayor()
