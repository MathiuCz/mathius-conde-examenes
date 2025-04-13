"""
2. (3 ptos) Crear un decorador conteo.
Reglas:

- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.

- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.

- La función que vas a crear va a capturar, la edad, nombre de un alumnos y la
hora y el minuto en que fue registrado (usar la librería correspondiente)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”

- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.

"""

from datetime import datetime


def conteo(funB):
    def funC(*args, **kwargs):
        total_para = len(args) + len(kwargs)
        print("Cantidad de parámetros recibidos: {}".format(total_para))

        if total_para > 1:
            resultado = funB(*args, **kwargs)
            print("La función fue ejecutada.")
            return resultado
        else:
            print("Requerimos más de un parametro para ejecutar la funcion")
    return funC


@conteo
def registrar_estudiante(nombre, edad, n1, n2, n3, n4):
    ahora = datetime.now()
    hora = ahora.hour
    minuto = ahora.minute

    print(
        "{} de {} años ha sido registrado a las {} horas con {} minutos.".
        format(nombre, edad, hora, minuto)
    )

    promedio = (n1 + n2 + n3 + n4) / 4
    print("La media de las notas es: {}".format(promedio))
    return promedio


registrar_estudiante("Pedro", 30, 13, 20, 11, 15)
