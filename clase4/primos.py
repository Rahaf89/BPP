"""

    Funcion que determina si un numero es primo

    Tiene que recibir el numero entero

    

    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:

    #   1 - divisible entre 1

    #   2 - divisible entre el mismo

    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo

    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es

    # primo """

import math


lista = [2, 3, 4, 8, 5, 5, 22, 13, 17, 37, 24, 25]

def es_primo(numero):

    if (numero<=1):

        return False

    for i in range(2, math.ceil(math.sqrt(numero))+1):

        if(numero%i==0 and i!=numero):
            return False
    return True


nuevaLista=list(filter(lambda x : es_primo(x), lista))

print(nuevaLista) # [2, 3, 5, 5, 13, 17, 37]