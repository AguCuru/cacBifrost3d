# app/models/usuarios.py

import mysql.connector


class Usuarios:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.conn.cursor()

        # Puedes crear la tabla de usuarios si es necesario
        # Ejemplo:
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            contraseña VARCHAR(255) NOT NULL
        )"""
        )
        self.conn.commit()

    def agregar_usuario(self, nombre, email, contraseña):
        # Implementa la lógica para agregar un usuario
        pass

    def modificar_usuario(self, id, nuevo_nombre, nuevo_email, nueva_contraseña):
        # Implementa la lógica para modificar un usuario
        pass

    def eliminar_usuario(self, id):
        # Implementa la lógica para eliminar un usuario
        pass

    def consultar_usuario(self, id):
        # Implementa la lógica para consultar un usuario
        pass

    def listar_usuarios(self):
        # Implementa la lógica para listar todos los usuarios
        pass

    def __del__(self):
        self.cursor.close()
        self.conn.close()
