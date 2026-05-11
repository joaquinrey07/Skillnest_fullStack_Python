#Atributos, metodos de clase, 

#DEFINCION DE LA CLASE
class Estudiante:
    #Atributo de Clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes
    estudiantes = []

    #Metodo CONSTRUCTOR
    def __init__(self, nombre, nota):
        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota

        #Agregar elementos a lista Estudiante
        Estudiante.estudiantes.append(self)

        #Metodo de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

        #metodo de CLASE
        # Usa "CLS" porque trabaja con la informacion de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
         cls.colegio = nuevo_nombre

    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)

        #Metodo estatico
        #Este no usa CLS ni SELF, solo parametro.
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
            
#Creacion de objetos(Instancias)
e1 = Estudiante("Donovan", 4.0)
e2 = Estudiante("Randy", 6.7)
# Uso de metodos de instancias 
print("== METODO DE INSTANCIAS ==")
#mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info()
print()

#Uso de metodos de clase
print("=== METODO DE CLASE ===")
Estudiante.cambiar_colegio("Purkuyen")
print(e1.colegio)
print(e2.colegio)
print()

#Contar Estudiantes
print("=== CONTAR ESTUDIANTES ===")
print(f"")

#




##Funcion repaso.
## Crear una funcion que valide usuario y contraseña

def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user} a tu cuenta")
        return True
    else:
        print("Datos incorrentos")
        return False

def enviarDatos():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña:")
    validador(username, password)

enviarDatos()