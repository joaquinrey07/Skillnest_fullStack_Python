datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

datos[2]["puntaje"] = 75


def mostrar_calificacion(datos):
   print(f"{datos[0]["nombre"]} obtuvo {datos[0]["puntaje"]} puntos")

mostrar_calificacion(datos)


def obtener_valores(clave, lista):
    for diccionario in datos:
        print(diccionario[clave])
obtener_valores("nombre" ,datos)

def obtener_valores(clave, lista):
    for diccionario in datos:
        print(diccionario[clave])
obtener_valores("puntaje" ,datos)



# 1. Cambiar el puntaje de Pedro a 75
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
