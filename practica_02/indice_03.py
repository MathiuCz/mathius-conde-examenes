"""3. Escribir un programa para gestionar una billetera electrónica (3 ptos):
Reglas:
- El programa deberá considerar 2 cuentas bancarias para el
constructor: 1 en soles y otra en dólares. Considerar el nombre y
apellido del titular
- Deberá tener un método para transferir entre sus cuentas, pero
para realizar esto debe hacer una conversión de monedas.
- Tendrá otro método para retirar dinero, esto debe actualizar ambas
cuentas y mostrar en pantalla los montos actualizados, a su vez
validar si tiene fondos suficientes o no para el retiro, mostrar un
mensaje que indique no tiene suficientes en caso fuera el caso.
- Instanciar 3 veces los casos de transferencias para ver reflejado el
uso de tus métodos creados."""

class Billetera:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.soles = saldo_soles
        self.dolares = saldo_dolares

    def mostrar_saldos(self):
        print("Saldo de {} {}:".format(self.nombre, self.apellido))
        print("   - Soles: S/.{}".format(self.soles))
        print("   - Dólares: ${}".format(self.dolares))

    def transferir(self, origen, destino, monto, tipo_cambio=3.80): #Considerando un tipo de cambio de 3.8
        if origen == "soles" and destino == "dolares":
            if self.soles >= monto:
                self.soles = self.soles - monto
                self.dolares = self.dolares + (monto / tipo_cambio)
                print("Transferido S/.{} a ${}".format(monto, monto / tipo_cambio))
            else:
                print("Saldo insuficiente en soles.")
        elif origen == "dolares" and destino == "soles":
            if self.dolares >= monto:
                self.dolares = self.dolares - monto
                self.soles = self.soles + (monto * tipo_cambio)
                print("Transferido ${} a S/.{}".format(monto, monto * tipo_cambio))
            else:
                print("Saldo insuficiente en dólares.")
        else:
            print("Transferencia inválida (origen y destino deben ser diferentes).")

    def retirar(self, moneda, monto):
        if moneda == "soles":
            if self.soles >= monto:
                self.soles = self.soles - monto
                print(" Retirado S/.{} con éxito.".format(monto))
            else:
                print("No tiene suficiente saldo en soles.")
        elif moneda == "dolares":
            if self.dolares >= monto:
                self.dolares = self.dolares - monto
                print("Retirado ${} con éxito.".format(monto))
            else:
                print("No tiene suficiente saldo en dólares.")
        else:
            print("Moneda no válida (elige 'soles' o 'dolares').")

        self.mostrar_saldos()


# Instanciar
billetera1 = Billetera("Lucía", "Ramírez", 1000, 200)
billetera2 = Billetera("Maria", "Quispe", 10000, 460)
billetera3 = Billetera("Ronald", "Andrade", 5000, 300)
#Puede elegir la billetera que quiera en este caso elegí la 1

# Piden usar el metodo de transferencia tres veces)
print("Transferencia 1:")
billetera1.transferir("soles", "dolares", 380)
billetera1.mostrar_saldos()
print("___________________________________________")

print("Transferencia 2:")
billetera1.transferir("dolares", "soles", 50)
billetera1.mostrar_saldos()
print("___________________________________________")

print("Transferencia 3 (fallida):")
billetera1.transferir("soles", "dolares", 5000)  # No tiene suficiente saldo
billetera1.mostrar_saldos()
print("___________________________________________")

print("Retiro:")
billetera1.retirar("soles", 200)  # Retiro exitoso
billetera1.mostrar_saldos()
print("___________________________________________")

# Retiro fallido en dólares
print("Retiro fallido:")
billetera1.retirar("dolares", 1000)  # No tiene suficiente saldo
