class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(f"titulo '(titulo)' agregado correctamente")

    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        if titulo in self.lista_reproduccion:
            print(f"El usuario {self.nombre} esta viendo '{titulo}'")


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        susAntigua = self.suscripcion
        self.suscripcion = nueva_suscripcion
        print(f"Suscripcion cambio de {susAntigua} a {nueva_suscripcion}")

    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        

# Todos los valores que seban registrar debe ser con input

maurigamer777 = UsuarioStreaming("maurigaymer777", "maurigayymer@gmail.com")
maurigamer777.agregar_a_lista("deadpool")
maurigamer777.cambiar_suscripcion("estandar")
maurigamer777.ver_contenido("deadpool")
maurigamer777.mostrar_info_usuario()

joaquin = UsuarioStreaming("joaquin", "joaquin@gmail.com")
joaquin.agregar_a_lista("que paso ayer 1")
joaquin.cambiar_suscripcion("restanda")
joaquin.ver_contenido("que paso ayer 1")
joaquin.mostrar_info_usuario()
# Añadir un menu While para llamar a los metodos
# metodos 
