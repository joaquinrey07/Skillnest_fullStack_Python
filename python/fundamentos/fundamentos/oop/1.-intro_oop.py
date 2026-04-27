#Creacion de la clase usuario
class Usuario:
   def __init__(self):
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0

#Instancias de una clase
miyagi = Usuario()
daniel = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Nariyoshi
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"


