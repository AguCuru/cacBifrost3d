from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import os
import time
import mysql.connector
from models.enums import Category, Rol

# from config import Config
# Instalar con pip install flask-cors
from flask_cors import CORS

app = Flask(__name__)

mysql = MySQL(app)
CORS(app)  # Esto habilitará CORS para todas las rutas

RUTA_DESTINO = r"C:\Agu\Proyectos\cacBifrost3d\img"

# --------------------------------------------------------------------
import mysql.connector
from mysql.connector import errorcode


class User:
    # ----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión inicial
        self.conn = mysql.connector.connect(host=host, user=user, password=password)
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
    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM User")
        user = self.cursor.fetchall()
        return user

    # ----------------------------------------------------------------

    # ----------------------------------------------------------------


class Producto:
    # ----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión inicial
        self.conn = mysql.connector.connect(host=host, user=user, password=password)
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
        self.create_product_table()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

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
    # Método para registrar un nuevo producto
    def productRegisterRepo(
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

    # ----------------------------------------------------------------
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM Product")
        productos = self.cursor.fetchall()
        return productos

    # -----------------Eliminar Producto-----------------------------------------------

    def eliminar_producto(self, product_id):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM Product WHERE product_id = {product_id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    # ----------------Consultar Producto-----------------------------------------------
    def consultar_producto(self, product_id):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM Product WHERE product_id = {product_id}")
        return self.cursor.fetchone()

    # ----------------------------------------------------------------

    # ------------------Modificar Producto----------------------------------------------
    def modificar_producto(
        self,
        product_id,
        nuevo_producto,
        nueva_descripcion,
        nuevo_precio,
        nuevo_video,
        nuevo_stock,
        nueva_categoria,
        nombre_imagen,
    ):
        sql = "UPDATE Product SET producto = %s, descripcion = %s, precio = %s, video = %s, stock = %s, categoria = %s, product_image = %s WHERE product_id = %s"
        valores = (
            nuevo_producto,
            nueva_descripcion,
            nuevo_precio,
            nuevo_video,
            nuevo_stock,
            nueva_categoria,
            nombre_imagen,
            product_id,
        )
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    # ----------------------------------------------------------------

    # -------------------Controller-User---------------------------------------------

    # Carpeta para guardar las imagenes.
    # RUTA_DESTINO = './static/imagenes/'


user_instance = User(
    host="localhost", user="root", password="root", database="cacbifrost3d"
)


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
            nuevo_codigo = user_instance.userRegister(
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
                        "mensaje": "Usuario agregado correctamente.",
                        "codigo": nuevo_codigo,
                        "imagen": imageName,
                    }
                ),
                201,
            )
        except Exception as e:
            # Si hay un error, se devuelve una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Internal Server Error).
            return jsonify({"mensaje": f"Error al agregar el usuario: {str(e)}"}), 500


# -------------------Listar Usuarios-------------------------------------------------
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    user = user_instance.listar_usuarios()
    return jsonify(user)

    # -----------------Controller-Product---------------------------------------------


product_instance = Producto(
    host="localhost", user="root", password="root", database="cacbifrost3d"
)


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
        image_name = ""

        # Genero el nombre de la imagen
        imageName = secure_filename(product_image.filename)
        nombre_base, extension = os.path.splitext(imageName)
        imageName = f"{nombre_base}_{int(time.time())}{extension}"

        try:
            # Llama al método userRegister de la clase User
            nuevo_codigo = product_instance.productRegisterRepo(
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


# --------------------------------------------------------------------
# Listar todos los productos
# --------------------------------------------------------------------
# La ruta Flask /productos con el método HTTP GET está diseñada para proporcionar los detalles de todos los productos almacenados en la base de datos.
# El método devuelve una lista con todos los productos en formato JSON.
@app.route("/productos", methods=["GET"])
def listar_productos():
    productos = product_instance.listar_productos()
    return jsonify(productos)


# --------------------------------------------------------------------
# Eliminar un producto según su código
# --------------------------------------------------------------------
@app.route("/eliminar-producto/<int:product_id>", methods=["DELETE"])
# La ruta Flask /productos/<int:codigo> con el método HTTP DELETE está diseñada para eliminar un producto específico de la base de datos, utilizando su código como identificador.
# La función eliminar_producto se asocia con esta URL y es llamada cuando se realiza una solicitud DELETE a /productos/ seguido de un número (el código del producto).
def eliminar_producto(product_id):
    # Busco el producto en la base de datos
    producto = product_instance.consultar_producto(product_id)
    if (
        producto
    ):  # Si el producto existe, verifica si hay una imagen asociada en el servidor.
        imagen_vieja = producto["product_image"]
        # Armo la ruta a la imagen
        ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

        # Y si existe, la elimina del sistema de archivos.
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Luego, elimina el producto del catálogo
        if product_instance.eliminar_producto(product_id):
            # Si el producto se elimina correctamente, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
            return jsonify({"mensaje": "Producto eliminado"}), 200
        else:
            # Si ocurre un error durante la eliminación (por ejemplo, si el producto no se puede eliminar de la base de datos por alguna razón), se devuelve un mensaje de error con un código de estado HTTP 500 (Error Interno del Servidor).
            return jsonify({"mensaje": "Error al eliminar el producto"}), 500
    else:
        # Si el producto no se encuentra (por ejemplo, si no existe un producto con el codigo proporcionado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado).
        return jsonify({"mensaje": "Producto no encontrado"}), 404


# Mostrar un sólo producto según su código
# --------------------------------------------------------------------
# La ruta Flask /productos/<int:codigo> con el método HTTP GET está diseñada para proporcionar los detalles de un producto específico basado en su código.
# El método busca en la base de datos el producto con el código especificado y devuelve un JSON con los detalles del producto si lo encuentra, o None si no lo encuentra.
@app.route("/productos/<int:product_id>", methods=["GET"])
def mostrar_producto(product_id):
    producto = product_instance.consultar_producto(product_id)
    if producto:
        return jsonify(producto), 201
    else:
        return "Producto no encontrado", 404


# --------------------------------------------------------------------
# Modificar un producto según su código
# --------------------------------------------------------------------
@app.route("/modificar-producto/<int:product_id>", methods=["PUT"])
# La ruta Flask /productos/<int:product_id> con el método HTTP PUT está diseñada para actualizar la información de un producto existente en la base de datos, identificado por su código.
# La función modificar_producto se asocia con esta URL y es invocada cuando se realiza una solicitud PUT a /productos/ seguido de un número (el código del producto).
def modificar_producto(product_id):
    # Se recuperan los nuevos datos del formulario
    nuevo_producto = request.form.get("producto")
    nueva_descripcion = request.form.get("descripcion")
    nuevo_precio = request.form.get("precio")
    nuevo_video = request.form.get("video")
    nuevo_stock = request.form.get("stock")
    nueva_categoria = request.form.get("categoria")

    # Verifica si se proporcionó una nueva imagen
    if "image" in request.files:
        imagen = request.files["image"]
        # Procesamiento de la imagen
        nombre_imagen = secure_filename(
            imagen.filename
        )  # Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de archivos
        nombre_base, extension = os.path.splitext(
            nombre_imagen
        )  # Separa el nombre del archivo de su extensión.
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"  # Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

        # Guardar la imagen en el servidor
        imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))

        # Busco el producto guardado
        producto = product_instance.consultar_producto(product_id)
        if producto:  # Si existe el producto...
            imagen_vieja = producto["product_image"]
            # Armo la ruta a la imagen
            ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

            # Y si existe la borro.
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)

    else:
        # Si no se proporciona una nueva imagen, simplemente usa la imagen existente del producto
        producto = product_instance.consultar_producto(product_id)
        if producto:
            nombre_imagen = producto["product_image"]

    # Se llama al método modificar_producto pasando el codigo del producto y los nuevos datos.
    if product_instance.modificar_producto(
        product_id,
        nuevo_producto,
        nueva_descripcion,
        nuevo_precio,
        nuevo_video,
        nuevo_stock,
        nueva_categoria,
        nombre_imagen,
    ):

        # Si la actualización es exitosa, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
        return jsonify({"mensaje": "Producto modificado"}), 200
    else:
        # Si el producto no se encuentra (por ejemplo, si no hay ningún producto con el código dado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado).
        return jsonify({"mensaje": "Producto no encontrado"}), 403


# --------------------------------------------------------------------

if __name__ == "__main__":
    print("Tablas creadas o verificadas correctamente")

    # Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
app.run(port=8080, debug=True)
