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

    def __init__(self, nombre, edad, sueldo, nacionalidad , saldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = nacionalidad
        self.__saldo = saldo

    def mostrar_saldo(self):
        print("Saldo de {} es de S/.{}".format(self.nombre, self.__saldo))

    def obtener_saldo(self):
        return self.__saldo

    def dejar_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo


#Persona hereda de empleado
class Persona(Empleado):
    def __init__(self, nombre, edad, sueldo, nacionalidad, saldo):
        super().__init__(nombre, edad, sueldo, nacionalidad, saldo)
        self.sueldo = sueldo

    def transferencia(self, receptor, monto):
        if self.obtener_saldo() >= monto:
            self.dejar_saldo(self.obtener_saldo() - monto)
            receptor.dejar_saldo(receptor.obtener_saldo() + monto)
            print(" Transferencia de S/.{} realizada de {} a {}".format(monto, self.nombre, receptor.nombre))
        else:
            print("Saldo insuficiente")
#Instancias
persona1 = Persona("Lucía", 27, 800, "Peruana", 3000)
persona2 = Persona("Jorge", 35, 300, "Peruana",2000)

#Cuentas
cuentas = {
    "1": persona1,
    "2": persona2
}

print("Cuentas disponibles:")
for key, persona in cuentas.items():
    print(f"{key}. {persona.nombre}")

#Pidiendo los datos
origen = input("\nIngrese el número de la cuenta DE ORIGEN: ")
destino = input("Ingrese el número de la cuenta DESTINO: ")
monto = float(input("Ingrese el monto a transferir: "))

if origen in cuentas and destino in cuentas and origen != destino:
    cuentas[origen].transferencia(cuentas[destino], monto)
else:
    print("Opción inválida (cuentas iguales o inexistentes)")

print("\n--- Saldos finales ---")
persona1.mostrar_saldo()
persona2.mostrar_saldo()