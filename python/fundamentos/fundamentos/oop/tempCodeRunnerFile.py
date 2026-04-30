class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(f'"{titulo}" ha sido añadido a tu lista de reproducción.')

    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        if titulo in self.lista_reproduccion:
            print(f'¡Reproduciendo: {titulo}!')
        else:
            print(f'El contenido "{titulo}" no está en tu lista de reproducción.')

    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        self.suscripcion = nueva_suscripcion
        print(f'Su suscripción ha sido cambiada a: {nueva_suscripcion}')

    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        print("Lista de Reproducción:", ", ".join(self.lista_reproduccion) if self.lista_reproduccion else "Vacía")

# Función para el menú interactivo
def menu():
    nombre = input("Ingresa tu nombre: ")
    email = input("Ingresa tu email: ")
    suscripcion = input("Ingresa el tipo de suscripción (Gratis, Premium, etc.): ")
    usuario = UsuarioStreaming(nombre, email, suscripcion)

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar a lista de reproducción")
        print("2. Ver contenido de la lista")
        print("3. Cambiar suscripción")
        print("4. Mostrar información del usuario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Ingresa el título del contenido a agregar: ")
            usuario.agregar_a_lista(titulo)
        elif opcion == "2":
            titulo = input("Ingresa el título del contenido a ver: ")
            usuario.ver_contenido(titulo)
        elif opcion == "3":
            nueva_suscripcion = input("Ingresa el nuevo tipo de suscripción: ")
            usuario.cambiar_suscripcion(nueva_suscripcion)
        elif opcion == "4":
            usuario.mostrar_info_usuario()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

# Llamar al menú
menu()