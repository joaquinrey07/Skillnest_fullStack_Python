class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, salario_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = salario_pagar 

#Creación de instacias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 300)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 20000, 150)
daniel = Usuario("Dany", "Hernandez", "dany@codingdojo.com", 3000 ,200)

#Imprimir valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#---------------------------
#--- Tarea rápida
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes
- Imprimir el nombre y apellido concatenado + especialidad
'''