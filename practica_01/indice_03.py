"""3. Generar un nuevo entorno virtual (3 ptos)
Reglas:
- El nombre del entorno virtual tendrá el nombre y tiene que seguir la siguiente
estructura (apellido_nombre) (mostrar captura de pantalla del entorno virtual
vacío)
- Instalar las librerías del requirements.txt obtenido en el problema anterior en
este nuevo entorno virtual
- Mostrar las librerías instaladas en el nuevo entorno virtual (screemshot)
- Mostrar el proceso de instalación exitoso de todas las dependencias que se
verá en la terminal sobre este nuevo entorno virtual.
- Agregar un último valor a tu lista la cuál estará previamente en una variable,
este valor indicará la cantidad de hijos que tiene esta persona, si la persona no
tiene hijos indicar “No cumple para obtener el bono familiar” en caso de tener
un hijo a más se agregará un nuevo valor a la lista el cuál será el 8% del sueldo
e indicándolo en un mensaje como: “Obtiene el bono familiar el cuál es de:
{bono_familiar}” (agregar este dato a lista y mostrar toda la lista actualizada)
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

#Adicionando el bono el bono obtenido por ser menor de 30 años
pot = pow(salario, 2)
porcentaje_5 = (5 * salario) / 100
bono = pot + porcentaje_5
print("El bono a es de: {}.".format(bono))
print("_____________________________________________________________________")

#Agregando las variables a la lita vacia
lista.extend([nombre, apellido, salario, edad_int, compania, trabajando, bono])

#Mostrar la lista y  el tamaño de la lista
print("La lista actualizada es: {}".format(lista))
print("La lista tiene {} datos.".format(len(lista)))

#Verificamos si se encuentra trabajando
if trabajando:
    print("El trabajador {} {} se encuentra trabajando actualmente en la compañía.".format(nombre, apellido))
else:
    print("El trabajador {} {} ya no se encuentra trabajando actualmente en la empresa.".format(nombre, apellido))
print("_____________________________________________________________________")

#Agregando la ultima variable
cant_hijos = 0 # puede cambiar el numero de hijos para verificar que si funciona el programa

#Agregando la variable a la lista
lista.extend([cant_hijos])

#Mostrar la lista y el tamaño de la lista
print("La lista actualizada con la cantidad de hijos es: {}".format(lista))
print("La lista tiene {} datos.".format(len(lista)))

#Veremos si es apto para obetener el bono familiar
if cant_hijos > 0:
    porcentaje_8 = (8 * salario) / 100
    bono_familiar = bono + porcentaje_8

    print("Obtiene el bono familiar el cuál es de: {}.".format(bono_familiar))

else:
    print("No cumple para obtener el bono familiar.")

# Si en caso sea apto agregar el valor de bono familia a la lista
if cant_hijos > 0:
    lista.extend([bono_familiar])
    print("La lista actualizada con el bono familiar es es: {}".format(lista))
else:
    print("Debido a que no tiene hijos, no se ha actualizado la lista con el bono familiar obtenido.")