"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)

Reglas:

- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda."""

#Asignando variables
nombre = "Mathius"
salario = 1000
edad = "20"
compania = "Universidad Nacional Mayor de San Marcos"

#Identificando el tipo de variable
print("El tipo de dato de la variable nombre es: {}.".format(type(nombre)))
print("El tipo de dato de la variable salario es: {}.".format(type(salario)))
print("El tipo de dato de la variable edad es: {}.".format(type(edad)))
print("El tipo de dato de la variable compañia es: {}.".format(type(compania)))

print("_____________________________________________________________________")

#Convirtiendo edad en entero
edad_int = int(edad)

#identificamos si es mayor a 30 años
if edad_int > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
else:
    print("Usted tiene un bono del 5% en el mes diciembre")

#Varianles a utilizar
pot = pow(salario, 2)
porcentaje_5 = (5 * salario) / 100 #si el usuario es menor a 30 años
porcentaje_10 = (10 * salario) / 100 #si el usuario es mayor a 30 años

#Bono final
if edad_int > 30:
    bono_total_10 = pot + porcentaje_10
    print("Su bono total es: {}".format(bono_total_10))
else:
    bono_total_5 = pot + porcentaje_5
    print("Su bono total es: {}".format(bono_total_5))


