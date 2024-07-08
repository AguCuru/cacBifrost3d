# app/models/productos.py

import mysql.connector


class Productos:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(4))"""
        )
        self.conn.commit()

    def agregar_producto(self, descripcion, cantidad, precio, imagen, proveedor):
        sql = "INSERT INTO productos (descripcion, cantidad, precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s)"
        valores = (descripcion, cantidad, precio, imagen, proveedor)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_producto(
        self,
        codigo,
        nueva_descripcion,
        nueva_cantidad,
        nuevo_precio,
        nueva_imagen,
        nuevo_proveedor,
    ):
        sql = "UPDATE productos SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"
        valores = (
            nueva_descripcion,
            nueva_cantidad,
            nuevo_precio,
            nueva_imagen,
            nuevo_proveedor,
            codigo,
        )
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def eliminar_producto(self, codigo):
        sql = "DELETE FROM productos WHERE codigo = %s"
        self.cursor.execute(sql, (codigo,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def consultar_producto(self, codigo):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = %s", (codigo,))
        return self.cursor.fetchone()

    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


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
