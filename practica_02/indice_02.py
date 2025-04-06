"""2. Usando el concepto de herencia y encapsulación (para el atributo saldo)
para crear el siguiente programa (3 ptos):
Reglas:
- Crear una clase llamada Persona y agregar un atributo saldo a esta clase
(ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la clase Empleado que llame al método
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
deberá ir actualizando también el saldo o monto que tiene el otro empleado
en su cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando
una transferencia y con dos personas."""

#Creando la clase
class Empleado:

    def __init__(self, nombre, edad, sueldo, nacionalidad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = nacionalidad
        self.__saldo = saldo

class Persona(Empleado):

