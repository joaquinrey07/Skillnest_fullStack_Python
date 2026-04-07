"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # Importacion de librerias para procesos aleatorios


nombre = "Frida Kahlo" # Creacion de variable tipo string y se asigna valor "valor"
print(type(nombre)) #Type() = metodo de python para mostrar el tipo de una variable
print(len(nombre)) #len() = devuelve el largo de una variable.


edad = 25 # Creacion de variable tipo numerico(INT)


if edad < 18: #Se establece condicion if
   print("Eres menor de edad.") #Imprime un mensaje
elif edad == 18: #Se establece subcondicion elif(else if)
   print("Tienes 18 años.") #Imprime un mensaje
else: #Cierra de condicion
   print("Eres mayor de edad.") #Imprime un mensaje


frutas = ["manzana", "pera", "fresa"] # Creacion de array con valores ya asignados
print(frutas[0]) # Mostramos la primara posicion del arreglo
frutas[0] = "banana" # A la posicion 0 del arreglo se le asigna el valor de "banana"
frutas.append("uva") # Se le agrega "uva" al final de un arreglo
frutas.remove("pera") # Se remueve la palabra "para" del arreglo


dimensiones = (200, 50) # Creamos una variable tipo tupla (variable inmutable)
print(dimensiones[0]) # Imprime la posicion 0 de la variable creada


persona = { # Variable tipo object (objeto)
   "nombre": "Carlos",
   "edad": 30
}
print(persona["nombre"]) # Imprime el valor del item(ej: "carlos")
persona["edad"] = 31 #Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago" #Se agrega un nuevo item con un valor
del persona["ciudad"]#Se elimina el item completo


for i in range(5): #for rango: Se crea bucle en rango S
   if i == 2: #Se establece condicion if == 2
       continue #Continue ignora el proceso y continuo
   if i == 4: # Se establece condicion if i == 4
       break #Si i - 4 se rompe el bucle
   print(i)


contador = 0 # Se crea una variable contador tipo numerica(INT)
while contador < 3: #Se crea bucle while con una condicion
   print(f"while contador es: {contador}") #Imprime el contador en un mensaje concatenado con f"" string
   contador += 1 # Incrementa el valor en 1 en cada iteracion


def saludar_usuario(nombre):
   return f"Hola, {nombre}"


print(saludar_usuario("Francisca"))