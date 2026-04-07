'''
Actividad: Gestor de inventario

1.- Creacion: crear una lista llamada inventario que contenga los siguentes
articulos: "laptop", "raton", "monitor", "cable hdmi" '''
inventario = ["laptop", "raton", "monitor", "cable hdmi", "teclado"]
''' 2.- Expansiion: Utiliza el metodo correspondiente para agregar "impresora"
al final de la lista '''
inventario.append("impresora")
''' 3.- Conteo: Utiliza la funcion integrada para mostrar cuantos elementos 
totales hay en la lista. '''
(len(inventario))
''' 4.- Acceso y modificacion: modifca "teclado" por "teclado mecanico" '''
inventario[5] = "teclado mecanico"
''' 5.- Slicing: Crea una nueva lista llamada "promocion", debe contener
solo los 3 primeros elementos de la lista "inventario". '''
promocion = inventario[0:3]
''' 6.- Mostrar la lista de inventario ordenado alfabeticamente '''
inventario.sort()
''' 7.- Elimina el ultimo elemento de la lista inventario mostrando el elemento 
eliminado y la lista final'''
eliminado = inventario.pop()
print(inventario)
print(eliminado)





