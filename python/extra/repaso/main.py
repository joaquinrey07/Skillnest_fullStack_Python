from python.extra.repaso.usuario import Usuario

u = Usuario()

while True:
    print("========================")
    print("SISTEMA DE USUARIOS")
    print("========================")
    print("1. Iniciar sesión")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        datos = u.iniciar_sesion(usuario, password)

        if datos == None:
            print("Usuario o contraseña incorrectos.")

        else:
            if datos[3] == 1: # ADMIN

                while True:
                    print("\n========================")
                    print("Bienvenido Administrador")
                    print("========================")
                    print("1. Registrar usuario")
                    print("2. Listar usuarios")
                    print("3. Buscar usuario")
                    print("4. Modificar usuario")
                    print("5. Eliminar usuario")
                    print("6. Cerrar sesión")

                    op = input("Opción: ")

                    if op == "1":
                        usu = input("Usuario: ")
                        contra = input("Contraseña: ")
                        tipo = input("Tipo (1=ADMIN, 2=USER): ")

                        u.crear_usuario(usu, contra, tipo)
                        print("Usuario registrado.")

                    elif op == "2":
                        lista = u.listar_usuarios()

                        for x in lista:
                            print(x)

                    elif op == "3":
                        id = input("ID: ")

                        dato = u.buscar_usuario(id)

                        print(dato)

                    elif op == "4":
                        id = input("ID: ")
                        usu = input("Nuevo usuario: ")
                        contra = input("Nueva contraseña: ")
                        tipo = input("Tipo (1=ADMIN, 2=USER): ")

                        u.modificar_usuario(id, usu, contra, tipo)

                        print("Usuario modificado.")

                    elif op == "5":
                        id = input("ID: ")

                        u.eliminar_usuario(id)

                        print("Usuario eliminado.")

                    elif op == "6":
                        break

                    else:
                        print("Opción inválida.")

            elif datos[3] == 2:

                while True:
                    print("\n========================")
                    print("Bienvenido")
                    print(datos[1])
                    print("Tipo de usuario: USER")
                    print("1. Cerrar sesión")

                    op = input("Opción: ")

                    if op == "1":
                        break
                    else:
                        print("Opción inválida.")

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
