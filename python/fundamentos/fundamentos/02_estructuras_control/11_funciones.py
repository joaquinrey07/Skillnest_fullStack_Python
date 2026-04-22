def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado

def buenos_dias(nombre):
   print("Buenos días "+nombre)
   
buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")

def buenos_dias2(nombre):
   return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python",
#por lo que el valor de mi variable frase será ese

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python

#Ejercicio de retorno de valor.
#Crear una funcion que recioba una frase en un parametro
#Devolver el valor de la frase completa e imprimir

def contruirfrase(frase, palabra):
   return f"{frase} {palabra}"

def recibirFrases():
   frase = input("Ingrese una frase: ")
   palabra = input("Ingrese una palabra: ")
   resutladoFrase = contruirfrase(frase, palabra)
   print(resutladoFrase)
