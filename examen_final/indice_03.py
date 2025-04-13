"""
3. (3 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con minutos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.
"""

from datetime import datetime


def deco_time_sum(funcionB):
    def funcionC(**kwargs):
        ahora = datetime.now()
        hora = ahora.strftime("%H")
        minuto = ahora.strftime("%M")
        print(
            "El decorador está siendo ejecutado a las {} con {} minutos".
            format(hora, minuto)
        )

        suma = sum(kwargs.values())
        print("Suma de los elementos: {}".format(suma))

        resultado = funcionB(**kwargs)
        return resultado
    return funcionC


@deco_time_sum
def encontrar_mayor(**kwargs):
    mayor = max(kwargs.values())
    print("El mayor número es: {}".format(mayor))
    return mayor


# Ejemplos con distintos numeros
print("Ejemplo 1:")
encontrar_mayor(a=5, b=12, c=3, d=8, e=9, f=2)

print("Ejemplo 2:")
encontrar_mayor(x=100, y=250, z=50, w=10)

print("Ejemplo 3:")
encontrar_mayor(n1=1, n2=1, n3=1, n4=1, n5=1)
