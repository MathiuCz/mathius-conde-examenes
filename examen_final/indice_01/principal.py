"""
1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.

- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.

- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.

- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.

- Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo

"""
from modulo import lista_aleatoria, no_repetidos, ordenar, mayor_par


lista_aleatoria = lista_aleatoria()
no_repetidos = no_repetidos(lista_aleatoria)
ordenar(no_repetidos)
mayor_par(no_repetidos)
