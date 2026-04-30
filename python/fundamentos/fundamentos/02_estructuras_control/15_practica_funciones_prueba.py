# Instrucciones generales
# Deberá desarrollar un programa en Python que contenga un menú interactivo utilizando la estructura while, permitiendo al usuario seleccionar distintas opciones para ejecutar funciones previamente definidas.
# Cada opción del menú deberá llamar a una función diferente, la cual resolverá una situación específica utilizando distintos tipos de datos como enteros, decimales, cadenas de texto, listas y diccionarios.
# En aquellos casos donde sea necesario, deberá solicitar información al usuario mediante input(). Además, se deberá trabajar con arreglos (listas) para recorrer información utilizando ciclos for, junto con estructuras condicionales como if, elif y else.

# 1. Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def calcular_mayor_menor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número menor es: {menor}")
    print(f"El número mayor es: {mayor}")
    
def ejercicio_calcular_mayor_menor():
    limit = int(input("Ingrese la cantidad de números que desea ingresar: "))
    numeros = []
    i = 1
    while i <= limit:
        numero = int(input(f"Ingrese el número {i}: "))
        numeros.append(numero)
        i += 1
    calcular_mayor_menor(numeros)
     


# 2. Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales


def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1

    print(f"La cadena contiene {contador} vocales.")


def ejercicio_contar_vocales():
    texto = input("Ingrese una cadena de texto: ")
    contar_vocales(texto)
    


# 3. Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def mostrar():
    nombres = []
    nombresLargos = []
    cantidad = int(input("¿Cuantos nonbres quieres ingresar?"))

    for i in range(cantidad):
        nombre = input("Ingrese un nombre: ")
        print(f"{nombre} agregado con extio a la lista.")
        nombres.append(nombre)

    listaNombre = filtrar(nombres)
    print(f"Los nombre scon mas de 5 letras son: \n {("\n- ").join(listaNombre)} ")



# 4. Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def listaNotas(notas):
    lista = 0
    promedio = 0
    for i in range(len(notas)):
        lista += notas[i]
        promedio = lista / (len(notas))

    if promedio >= 4.0 and promedio <= 7.0:
        return f"El estudiante aprueba con {promedio}"
    elif promedio >= 1.0 and promedio <= 3.9:
        return f"El estudiante no pasa con un {promedio}"
    else:
        return "Error"

def ejercicio4():
    largo = int(input("Cuantos notas va a ingresar: "))
    nota = []
    for i in range(largo):
        inp = float(input(f"Ingrese nota {i + 1}: "))
        if inp != "":
            nota.append(inp)
    print(listaNotas(nota))
ejercicio4()

# 5. Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * 0.1
    precioFinal = precioInicial = descuento
    print(f"El precio inicial del procucto es: \n{precioInicial}ny con descuento \n{precioFinal}")

def valores():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quiere:\n"))
    listasPrecio = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor del producto:\n"))


def aplicar_descuento(precios):
    pass
    

# 6. Crear una función que reciba un número entero y determine si es par o impar.
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par. ")
    elif numero % 3 == 0:
        print(f"El numero {numero} es impar")
    else:
        print("Error")

def recibirNum(numero):
    num = int(input("Ingrese un numero: "))
    parImpar(num)
recibirNum()

# 7. Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 10:
            num += 1
    return num

def personas():
    edad = []
    inp = int(input("Cuantos personas vas a ingresar hoy?"))
    for i in range(inp):
        var = int(input(">> "))
        if var != "":
            edad.append()
        else:
            print("Por favor ingresar valor valido")
    resultado = edades(edad)
    print(f"Hay {resultado} personas mayores de edad")
personas()


# 8. Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def palabra_coincide(palabra):
    buscar = input("Ingrese la palabra que desea buscar: ")
    vecesqAparece = 0
    for i in range(len(palabra)):
        if buscar == palabra[i]:
            vecesAparece += 1
    print(f"La palabra {buscar} aparece {vecesqAparece} en la lista. ")

def recibirpalabras():
    cantidad = int(input("Ingrese la cantidad de palabra: "))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}. ")
        listaPalabras.append(palabra)
    palabra_coincide(listaPalabras)

def contar_palabra(palabras, palabra_buscar):
    pass

# 9. Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
def es_positivo(numero):
    pass


def filtrar_positivos(numeros):
    pass

# 10. Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
def tiene_bajo_stock(producto):
    pass


def productos_bajo_stock(productos):
    pass

#Menu while