"""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Empleado donde sus atributos deben ser nombre,
edad, sueldo y de nacionalidad peruana, tendrá un método para solicitar su
nombre y otro para solicitar su edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Empleado y usar su nuevo método
aumentoSueldo para incrementar su sueldo en un 30% (mínimo instanciar
la clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
- Crear un siguiente método que retorne un mensaje donde indique que: “En
el año XXXX tendrá XX años”, el año se ingresará por parámetro y la
edad también, realizar una validación si la edad ingresada por parámetro
es menor a la del constructor indicar que no es posible realizar la
operación (Mostrar por pantalla este valor)
"""

#Creando la clase
class Empleado:

    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.sueldo = 0.0
        self.nacionalidad = "Peruana"

    #Metodo para solicitar nombre
    def solicita_nombre(self):
        self.nombre = input("Ingrese el nombre: ")

    #Metodo para solicitar edad
    def solicitar_edad(self):
        self.edad = int(input("Ingrese el edad: "))

    #Metodo que aumenta +1 en la edad
    def cumpleaños(self):
        self.edad = self.edad + 1

    def aumento_sueldo(self):
        self.sueldo= (self.sueldo + (self.sueldo * 0.3))
        return self.sueldo

    def edad_en(self, año_futuro, edad_ingresada):
        if edad_ingresada < self.edad:
            return "No es posible realizar la operación: la edad ingresada ({}) es menor a la edad actual ({}).".format(edad_ingresada, self.edad)
        elif edad_ingresada > self.edad:
            return "Su edad es mayor a la ingresada con anteorioridad"
        else:
            años_que_pasan = año_futuro - 2025
            edad_futura = self.edad + años_que_pasan
            return "En el año {} tendrá {} años.".format(año_futuro, edad_futura)
#Creando instancias
empleado1 = Empleado()
empleado1.solicita_nombre()
empleado1.solicitar_edad()
empleado1.sueldo = float(input("Ingrese el sueldo actual del empleado 1: "))
nuevo_sueldo1 = empleado1.aumento_sueldo()

print("El empleado {} cuenta con un con aumento: S/. {} ".format(empleado1.nombre,nuevo_sueldo1))
print(empleado1.edad_en(2026,int(input("Ingrese edad para verificar (Empleado 1): "))))
#ingresando 2025 por parametro

print("______________________________________________________________")
empleado2 = Empleado()
empleado2.solicita_nombre()
empleado2.solicitar_edad()
empleado2.sueldo = float(input("Ingrese el sueldo actual del empleado 2: "))
nuevo_sueldo2 = empleado2.aumento_sueldo()

print("El empleado {} cuenta con un con aumento: S/. {} ".format(empleado2.nombre,nuevo_sueldo2))
print(empleado1.edad_en(2025,int(input("Ingrese edad para verificar (Empleado 2): "))))