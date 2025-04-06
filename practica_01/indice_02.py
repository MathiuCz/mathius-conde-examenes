"""
2.Crear un entorno virtual y aplicar lo siguiente (4 ptos):

Reglas:

- El nombre del entorno virtual tendrá el nombre con la siguiente estructura
(apellido_nombre_edad)
- Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y
aws (última versión)
- Generar el archivo de requirements.txt (mostrar las librerías instaladas)
- Crear un segundo archivo en el cual se creará una lista vacía, para luego
agregar los datos de nombre, salario, edad, compañía y bono a esta lista vacía
(todos estos datos ya fueron obtenidos en el problema anterior)
- Adicional agregar el valor de “true” o “false” en una variable si está trabajando
o no en la empresa y luego agregarla a la lista para mostrar en consola esta
misma lista
- Mostrar el tamaño de la lista, en el caso que el valor de si está laborando aún
en la empresa, diciendo: “El trabajador {nombre} {apellido} se encuentra
trabajando actualmente en la compañía” sino mostrar un mensaje indicando
“El trabajador {nombre} {apellido} ya no se encuentra trabajando
actualmente en la empresa”

"""
#Lista vacia
lista = []
print("La lista tiene {} datos.".format(len(lista)))
print("_____________________________________________________________________")

#Asignando variables ya utilizadas
nombre = "Mathius"
apellido = "Condde"
salario = 1000
edad = "20"
compania = "Universidad Nacional Mayor de San Marcos"
trabajando = True

#convirtiendo la edad a entero
edad_int = int(edad)

#Adicionando el bono obtenido por ser menor de 30 años
pot = pow(salario, 2)
porcentaje_5 = (5 * salario) / 100
bono = pot + porcentaje_5
print("El bono a es de: {}.".format(bono))
print("_____________________________________________________________________")

#Agregando las variables a la lista vacia
lista.extend([nombre, apellido, salario, edad_int, compania, trabajando, bono])

#Mostrar el tamaño de la lista
print("La lista actualizada es: {}".format(lista))
print("La lista tiene {} datos.".format(len(lista)))

#Verificamos si se encuentra trabajando
if trabajando:
    print("El trabajador {} {} se encuentra trabajando actualmente en la compañía.".format(nombre, apellido))
else:
    print("El trabajador {} {} ya no se encuentra trabajando actualmente en la empresa.".format(nombre, apellido))





