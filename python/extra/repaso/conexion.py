import mysql.connector

class Conexion:

    @staticmethod
    def conectar():

        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="usuarios_db"
        )

        return conexion