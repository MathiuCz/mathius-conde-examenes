import random


def lista_aleatoria():
    lista = []
    for _ in range(10):
        # puede variar el rango en este caso elegimos 100
        numero = random.randint(1, 100)
        lista.append(numero)
    print("Lista aleatoria: {}".format(lista))
    return lista


def no_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    print("Lista sin repetidos: {}".format(lista_sin_repetidos))
    return lista_sin_repetidos


def ordenar(lista):
    descendente = sorted(lista, reverse=True)
    ascendente = sorted(lista)
    print("Orden mayor a menor: {}".format(descendente))
    print("Orden menor a mayor: {}".format(ascendente))
    return descendente, ascendente


def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        mayor_par = max(pares)
        print("El mayor número par es: {}".format(mayor_par))
        return mayor_par
    else:
        print("No hay números pares en la lista.")
        return None
