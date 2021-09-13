'''
funcion que regresa solo los numeros pares de una lista
'''

def pares():

    num = [1,2,4,8,9,12,14,28,42,57,91,108]

    for x in num:
        if x % 2 == 0:
            print (x)

pares()