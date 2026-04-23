import os
#Funciones basicas practica 2

#Ejercicio 1
# Calcula experiencia
def multiplica_por_2(num):
    resultado = []
    for i in range(num + 1):
        resultado.append(i * 2)
    return resultado
def ejercicio1():
    resultado1 = multiplica_por_2(5)
    print(resultado1)   
# Debe retornar: [0, 2, 4, 6, 8, 10]

#Ejercicio 2
# Analiza publicaciones
def suma_y_resta(num):
    suma = num[0] + num[1]
    print(suma)
    resta = num[0] - num[1]
    return resta
def ejercicio2():
    resultado2 = suma_y_resta([120, 115])
    print(resultado2)

# Imprime: 235 y retorna: 5

#Ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(num):
    suma = sum(num)
    print(f"Suma total: {suma}")
    long = len(num)
    print(f"Longitud: {long}")
    return suma - long
def ejercicio3():
    resultado3 = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"Retorno: {resultado3}")
# Suma total = 25, longitud = 4, debe retornar: 21

#Ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    else:
        segEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i * segEle)
        long = len(nuevaLista)
        print(long)
        return nuevaLista 
def ejercicio4():
    resultado4 = valores_multiplicados_segundo([100, 3, 50, 20])
    print(resultado4)
    print()
    resultado5 = print(valores_multiplicados_segundo([100]))
    print(resultado5)

#Ejercicio 5
# Genera precio fijo
def valor_multiplicado_longitud(valor, longitud):
    lista = []
    for i in range(longitud):
        lista.append(valor * longitud)
    return lista

def ejercicio5():
    print(valor_multiplicado_longitud(5, 2))
# Debe retornar: [10, 10]
    print(valor_multiplicado_longitud(7, 5))
# Debe retornar: [35, 35, 35, 35, 35]

def limpiarconsola():
    os.system('cls')

continuar = True
while continuar:
    print("\n ejercicio python: ")
    print("--- 1.- Ejercicio  1 ---:")
    print("--- 2.- Ejercicio  2 ---:")
    print("--- 3.- Ejercicio  3 ---:")
    print("--- 4.- Ejercicio  4 ---:")
    print("--- 5.- Ejercicio  5 ---:")
    opcion = input("\n--- Elige una opción: (1:5) (0 para salir)")
    if opcion == "1":
        limpiarconsola()
        print("\nEjecutando ejercicio 1: ")
        ejercicio1()
    elif opcion == "2":
        limpiarconsola()
        print("\nEjecutando ejercicio 2: ")
        ejercicio2()
    elif opcion == "3":
        limpiarconsola()
        print("\nEjecutando ejercicio 3: ")
        ejercicio3()
    elif opcion == "4":
        limpiarconsola()
        print("\nEjecutando ejercicio 4: ")
        ejercicio4()
    elif opcion == "5":
        limpiarconsola()
        print("\nEjecutando ejercicio 5: ")
        ejercicio5()