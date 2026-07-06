from python.extra.repaso.conexion import Conexion

class Usuario:

    def crear_usuario(self, usuario, password, tipo):
        con = Conexion()
        conexion = con.conectar()
        cursor = conexion.cursor()

        sql = "INSERT INTO usuarios(usuario, password, tipo_usuario) VALUES(%s,%s,%s)"
        cursor.execute(sql, (usuario, password, tipo))

        conexion.commit()
        conexion.close()

    def listar_usuarios(self):
        con = Conexion()
        conexion = con.conectar()
        cursor = conexion.cursor()

        sql = """SELECT usuarios.id, usuario, nombre
                 FROM usuarios
                 INNER JOIN tipo_usuario
                 ON usuarios.tipo_usuario = tipo_usuario.id"""

        cursor.execute(sql)

        datos = cursor.fetchall()

        conexion.close()

        return datos

    def buscar_usuario(self, id):
        con = Conexion()
        conexion = con.conectar()
        cursor = conexion.cursor()

        sql = "SELECT * FROM usuarios WHERE id=%s"
        cursor.execute(sql, (id,))

        dato = cursor.fetchone()

        conexion.close()

        return dato

    def modificar_usuario(self, id, usuario, password, tipo):
        con = Conexion()
        conexion = con.conectar()
        cursor = conexion.cursor()

        sql = """UPDATE usuarios
                 SET usuario=%s, password=%s, tipo_usuario=%s
                 WHERE id=%s"""

        cursor.execute(sql, (usuario, password, tipo, id))

        conexion.commit()
        conexion.close()

    def eliminar_usuario(self, id):
        con = Conexion()
        conexion = con.conectar()
        cursor = conexion.cursor()

        sql = "DELETE FROM usuarios WHERE id=%s"

        cursor.execute(sql, (id,))

        conexion.commit()
        conexion.close()

    def iniciar_sesion(self, usuario, password):
        con = Conexion()
        conexion = con.conectar()
        cursor = conexion.cursor()

        sql = "SELECT * FROM usuarios WHERE usuario=%s AND password=%s"

        cursor.execute(sql, (usuario, password))

        dato = cursor.fetchone()

        conexion.close()

        return dato