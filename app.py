from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import os
import time
import mysql.connector
from models.enums import Category, Rol
from dotenv import load_dotenv

# from config import Config
# Instalar con pip install flask-cors
from flask_cors import CORS

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos utilizando variables de entorno
app.config["MYSQL_HOST"] = os.getenv("DB_HOST")
app.config["MYSQL_USER"] = os.getenv("DB_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("DB_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("DB_DATABASE")

mysql = MySQL(app)
CORS(app)  # Esto habilitará CORS para todas las rutas

# --------------------------------------------------------------------
import mysql.connector
from mysql.connector import errorcode


class User:
    # ----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión inicial
        self.conn = mysql.connector.connect(
            host=app.config["MYSQL_HOST"],
            user=app.config["MYSQL_USER"],
            password=app.config["MYSQL_PASSWORD"],
            database=app.config["MYSQL_DB"],
        )

        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
                self.cursor.execute(f"USE {database}")
                print("Base de datos creada")
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos las tablas si no existen
        self.create_user_table()
        self.create_product_table()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    # ----------------------------------------------------------------
    # Crear tabla User
    def create_user_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS User (
                user_id INT NOT NULL AUTO_INCREMENT,
                firstname VARCHAR(45) NOT NULL,
                lastname VARCHAR(100) NOT NULL,
                email VARCHAR(45) NOT NULL,
                profile_image VARCHAR(255) DEFAULT NULL,
                password VARCHAR(45) NOT NULL,
                birthdate DATE NOT NULL,
                country VARCHAR(45) DEFAULT NULL,
                accepted_terms TINYINT NOT NULL DEFAULT '0',
                rol enum('ADMIN','USER') DEFAULT 'USER',
                PRIMARY KEY (user_id),
                UNIQUE KEY email_UNIQUE (email)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
        )
        self.conn.commit()

    # ----------------------------------------------------------------
    # Crear tabla Product
    def create_product_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Product (
                product_id INT NOT NULL AUTO_INCREMENT,
                producto VARCHAR(100) NOT NULL,
                descripcion TEXT NOT NULL,
                precio DECIMAL(10, 2) NOT NULL,
                product_image VARCHAR(255) DEFAULT NULL,
                video VARCHAR(255) DEFAULT NULL,
                stock INT NOT NULL,
                categoria VARCHAR(100) NOT NULL,
                PRIMARY KEY (product_id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
        )
        self.conn.commit()

    # ----------------------------------------------------------------
    def userRegister(
        self,
        firstname,
        lastname,
        email,
        profile_image,
        password,
        birthdate,
        country,
        accepted_terms,
    ):

        sql = "INSERT INTO user ( firstname, lastname, email, profile_image, password, birthdate, country, accepted_terms ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (
            firstname,
            lastname,
            email,
            profile_image,
            password,
            birthdate,
            country,
            accepted_terms,
        )

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

    # ----------------------------------------------------------------
    # Método para registrar un nuevo producto
    def productRegister(
        self,
        producto,
        descripcion,
        precio,
        product_image,
        video,
        stock,
        categoria,
    ):
        sql = """INSERT INTO Product (
            producto, descripcion, precio, product_image, video, stock, categoria
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (
            producto,
            descripcion,
            precio,
            product_image,
            video,
            stock,
            categoria,
        )
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid


# Ejemplo de uso
if __name__ == "__main__":
    user = User(host="localhost", user="root", password="root", database="cacbifrost3d")
    print("Tablas creadas o verificadas correctamente")
# ----------------------------------------------------------------


# Carpeta para guardar las imagenes.
# RUTA_DESTINO = './static/imagenes/'

# Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
RUTA_DESTINO = "C:\Agu\Proyectos\cacBifrost3d\images"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/registro")
def registro():
    return render_template("registro.html")


@app.route("/add_contact", methods=["POST"])
def addContact():
    if request.method == "POST":
        nombre = request.form["nombre"]
        print(nombre)
    return "ingresado"


@app.route("/registrado", methods=["POST"])
def userRegister():
    if request.method == "POST":
        # user_id = request.form["user_id"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        profile_image = request.files["profile_image"]
        password = request.form["password"]
        birthdate = request.form["birthdate"]
        country = request.form["country"]
        # accepted_terms = request.form["accepted_terms"]

        # Convertir el valor de 'terms' a 1 o 0
        accepted_terms = 1 if "accepted_terms" in request.form else 0

        # Genero el nombre de la imagen
        imageName = secure_filename(profile_image.filename)
        nombre_base, extension = os.path.splitext(imageName)
        imageName = f"{nombre_base}_{int(time.time())}{extension}"

        try:
            # Llama al método userRegister de la clase User
            nuevo_codigo = user.userRegister(
                # user_id,
                firstname,
                lastname,
                email,
                imageName,
                password,
                birthdate,
                country,
                accepted_terms,
            )

            # Guarda la imagen en el sistema de archivos
            profile_image.save(os.path.join(RUTA_DESTINO, imageName))

            # Si el producto se agrega con éxito, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 201 (Creado).
            return (
                jsonify(
                    {
                        "mensaje": "Producto agregado correctamente.",
                        "codigo": nuevo_codigo,
                        "imagen": imageName,
                    }
                ),
                201,
            )
        except Exception as e:
            # Si hay un error, se devuelve una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Internal Server Error).
            return jsonify({"mensaje": f"Error al agregar el producto: {str(e)}"}), 500


# -------------------ADMIN---------------------------------------------


@app.route("/ingresar-producto")
def ingresar_producto():
    categories = [category.value for category in Category]
    return render_template("ingresar_producto.html", categories=categories)


@app.route("/producto-ingresado", methods=["POST"])
def productRegister():
    if request.method == "POST":

        producto = request.form["producto"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        product_image = request.files["product_image"]
        video = request.form["video"]
        stock = request.form["stock"]
        categoria = request.form["categoria"]

        # Genero el nombre de la imagen
        imageName = secure_filename(product_image.filename)
        nombre_base, extension = os.path.splitext(imageName)
        imageName = f"{nombre_base}_{int(time.time())}{extension}"

        try:
            # Llama al método userRegister de la clase User
            nuevo_codigo = user.productRegister(
                # user_id,
                producto,
                descripcion,
                precio,
                imageName,
                video,
                stock,
                categoria,
            )

            # Guarda la imagen en el sistema de archivos
            product_image.save(os.path.join(RUTA_DESTINO, imageName))

            # Si el producto se agrega con éxito, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 201 (Creado).
            return (
                jsonify(
                    {
                        "mensaje": "Producto agregado correctamente.",
                        "codigo": nuevo_codigo,
                        "imagen": imageName,
                    }
                ),
                201,
            )
        except Exception as e:
            # Si hay un error, se devuelve una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Internal Server Error).
            return jsonify({"mensaje": f"Error al agregar el producto: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=8080, debug=True)
