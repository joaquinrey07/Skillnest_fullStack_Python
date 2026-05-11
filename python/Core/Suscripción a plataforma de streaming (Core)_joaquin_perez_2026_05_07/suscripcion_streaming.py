class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        self.saldo_pendiente = self.saldo_pendiente - monto
        print(self.usuario, "pagó:", monto)
        print("Saldo restante:", self.saldo_pendiente)

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente = self.saldo_pendiente + self.costo_mensual
            print(self.usuario, "cambió a plan", nuevo_tipo)

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print(self.usuario, "no tiene acceso a contenido exclusivo")
        else:
            print(self.usuario, "está viendo contenido exclusivo")

    def mostrar_info_suscripcion(self):
        print("Usuario:", self.usuario)
        print("Tipo:", self.tipo_suscripcion)
        print("Costo mensual:", self.costo_mensual)
        print("Saldo pendiente:", self.saldo_pendiente)
        print("---------------------------")

user1 = SuscripcionStreaming("Ana", "Gratis")
user2 = SuscripcionStreaming("Pedro", "Estándar")
user3 = SuscripcionStreaming("Lucía", "Premium")

user1.ver_contenido_exclusivo()
user1.cambiar_suscripcion("Estándar")
user1.realizar_pago(5.99)
user1.mostrar_info_suscripcion()

user2.ver_contenido_exclusivo()
user2.cambiar_suscripcion("Premium")
user2.realizar_pago(5.00)
user2.realizar_pago(11.98)
user2.mostrar_info_suscripcion()

user3.realizar_pago(5.00)
user3.ver_contenido_exclusivo()
user3.mostrar_info_suscripcion()