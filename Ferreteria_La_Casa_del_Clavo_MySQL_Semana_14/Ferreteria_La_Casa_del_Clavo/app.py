import os

from flask import Flask, flash, redirect, render_template, url_for
from flask_wtf import FlaskForm
from mysql.connector import Error, IntegrityError
from dotenv import load_dotenv
from wtforms import SubmitField

from conexion.conexion import obtener_conexion
from forms.cliente_form import ClienteForm
from forms.facturacion_form import FacturacionForm
from forms.producto_form import ProductoForm
from forms.proveedor_form import ProveedorForm

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "cambie-esta-clave-en-produccion")

NOMBRE_NEGOCIO = "Ferretería La Casa del Clavo"
INFO_NEGOCIO = {
    "nombre": NOMBRE_NEGOCIO, "ciudad": "Puyo", "provincia": "Pastaza",
    "telefono": "099 555 1234", "correo": "contacto@casadelclavo.com",
    "horario": "Lunes a sábado de 08:00 a 18:00",
}


class EliminarForm(FlaskForm):
    submit = SubmitField("Eliminar")


def consultar(sql, parametros=(), uno=False):
    """Ejecuta SELECT parametrizados y garantiza el cierre de recursos."""
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute(sql, parametros)
        return cursor.fetchone() if uno else cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()


def ejecutar(sql, parametros=()):
    """Ejecuta INSERT, UPDATE o DELETE con transacción segura."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(sql, parametros)
        conexion.commit()
        return cursor.lastrowid
    except Exception:
        conexion.rollback()
        raise
    finally:
        cursor.close()
        conexion.close()


def opciones_proveedores():
    filas = consultar(
        "SELECT id_proveedor, nombre FROM proveedores WHERE activo = %s ORDER BY nombre",
        (True,),
    )
    return [(fila["id_proveedor"], fila["nombre"]) for fila in filas]


@app.errorhandler(Error)
def error_base_datos(error):
    app.logger.exception("Error de MySQL: %s", error)
    return render_template("error_db.html", nombre_negocio=NOMBRE_NEGOCIO), 503


@app.route("/")
def inicio():
    conteos = consultar(
        """SELECT
        (SELECT COUNT(*) FROM productos) AS productos,
        (SELECT COUNT(*) FROM clientes) AS clientes,
        (SELECT COUNT(*) FROM proveedores) AS proveedores,
        (SELECT COUNT(*) FROM facturas) AS facturas""",
        uno=True,
    )
    return render_template(
        "index.html", nombre_negocio=NOMBRE_NEGOCIO,
        mensaje="Bienvenidos a nuestro sistema de gestión comercial.", info=INFO_NEGOCIO,
        total_productos=conteos["productos"], total_clientes=conteos["clientes"],
        total_proveedores=conteos["proveedores"], total_facturas=conteos["facturas"],
    )


@app.route("/productos")
def productos():
    filas = consultar(
        """SELECT p.id_producto, p.codigo, p.nombre, p.categoria, p.precio,
                  p.stock, p.descripcion, pr.nombre AS proveedor
           FROM productos AS p
           INNER JOIN proveedores AS pr ON pr.id_proveedor = p.id_proveedor
           ORDER BY p.id_producto"""
    )
    return render_template("productos.html", nombre_negocio=NOMBRE_NEGOCIO,
                           productos=filas, eliminar_form=EliminarForm())


@app.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo_producto():
    form = ProductoForm()
    form.id_proveedor.choices = opciones_proveedores()
    if form.validate_on_submit():
        try:
            ejecutar(
                """INSERT INTO productos
                (codigo, nombre, categoria, precio, stock, descripcion, id_proveedor)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (form.codigo.data.strip().upper(), form.nombre.data.strip(),
                 form.categoria.data, form.precio.data, form.stock.data,
                 form.descripcion.data.strip(), form.id_proveedor.data),
            )
        except IntegrityError:
            form.codigo.errors.append("Ya existe un producto con este código.")
        else:
            flash("Producto registrado correctamente en MySQL.", "success")
            return redirect(url_for("productos"))
    return render_template("formulario_producto.html", form=form,
                           nombre_negocio=NOMBRE_NEGOCIO, modo="nuevo")


@app.route("/productos/<int:id_producto>/editar", methods=["GET", "POST"])
def editar_producto(id_producto):
    producto = consultar("SELECT * FROM productos WHERE id_producto = %s", (id_producto,), uno=True)
    if producto is None:
        flash("El producto solicitado no existe.", "warning")
        return redirect(url_for("productos"))
    form = ProductoForm(data=producto)
    form.id_proveedor.choices = opciones_proveedores()
    if form.validate_on_submit():
        try:
            ejecutar(
                """UPDATE productos SET codigo = %s, nombre = %s, categoria = %s,
                   precio = %s, stock = %s, descripcion = %s, id_proveedor = %s
                   WHERE id_producto = %s""",
                (form.codigo.data.strip().upper(), form.nombre.data.strip(), form.categoria.data,
                 form.precio.data, form.stock.data, form.descripcion.data.strip(),
                 form.id_proveedor.data, id_producto),
            )
        except IntegrityError:
            form.codigo.errors.append("Ya existe otro producto con este código.")
        else:
            flash("Producto modificado correctamente.", "success")
            return redirect(url_for("productos"))
    return render_template("formulario_producto.html", form=form,
                           nombre_negocio=NOMBRE_NEGOCIO, modo="editar", producto=producto)


@app.post("/productos/<int:id_producto>/eliminar")
def eliminar_producto(id_producto):
    form = EliminarForm()
    if form.validate_on_submit():
        ejecutar("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        flash("Producto eliminado correctamente.", "success")
    else:
        flash("No se pudo validar la solicitud de eliminación.", "danger")
    return redirect(url_for("productos"))


@app.route("/clientes")
def clientes():
    return render_template("clientes.html", nombre_negocio=NOMBRE_NEGOCIO,
                           clientes=consultar("SELECT * FROM clientes ORDER BY id_cliente"))


@app.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        ejecutar(
            "INSERT INTO clientes (nombre, cedula, telefono, correo, activo) VALUES (%s, %s, %s, %s, %s)",
            (form.nombre.data.strip(), form.cedula.data.strip(), form.telefono.data.strip(),
             form.correo.data.strip().lower(), form.activo.data),
        )
        flash("Cliente registrado correctamente en MySQL.", "success")
        return redirect(url_for("clientes"))
    return render_template("formulario_cliente.html", form=form, nombre_negocio=NOMBRE_NEGOCIO)


@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html", nombre_negocio=NOMBRE_NEGOCIO,
                           proveedores=consultar("SELECT * FROM proveedores ORDER BY id_proveedor"))


@app.route("/proveedores/nuevo", methods=["GET", "POST"])
def nuevo_proveedor():
    form = ProveedorForm()
    if form.validate_on_submit():
        ejecutar(
            "INSERT INTO proveedores (nombre, contacto, telefono, correo, producto, activo) VALUES (%s, %s, %s, %s, %s, %s)",
            (form.empresa.data.strip(), form.contacto.data.strip(), form.telefono.data.strip(),
             form.correo.data.strip().lower(), form.producto.data.strip(), form.estado.data == "Activo"),
        )
        flash("Proveedor registrado correctamente en MySQL.", "success")
        return redirect(url_for("proveedores"))
    return render_template("formulario_proveedor.html", form=form, nombre_negocio=NOMBRE_NEGOCIO)


@app.route("/facturacion")
def facturacion():
    filas = consultar(
        """SELECT f.id_factura, f.numero, c.nombre AS cliente, f.fecha, f.total, f.estado
           FROM facturas AS f INNER JOIN clientes AS c ON c.id_cliente = f.id_cliente
           ORDER BY f.id_factura"""
    )
    return render_template("facturacion.html", nombre_negocio=NOMBRE_NEGOCIO,
                           facturas=filas, total_ventas=sum(float(f["total"]) for f in filas))


@app.route("/facturacion/nueva", methods=["GET", "POST"])
def nueva_factura():
    form = FacturacionForm()
    activos = consultar("SELECT id_cliente, nombre FROM clientes WHERE activo = %s ORDER BY nombre", (True,))
    form.cliente.choices = [(fila["id_cliente"], fila["nombre"]) for fila in activos]
    if form.validate_on_submit():
        ejecutar(
            "INSERT INTO facturas (numero, id_cliente, fecha, total, estado) VALUES (%s, %s, %s, %s, %s)",
            (form.numero.data.strip().upper(), form.cliente.data, form.fecha.data,
             form.total.data, form.estado.data),
        )
        flash("Factura registrada correctamente en MySQL.", "success")
        return redirect(url_for("facturacion"))
    return render_template("formulario_facturacion.html", form=form, nombre_negocio=NOMBRE_NEGOCIO)


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")
