import os
import sqlite3
from pathlib import Path

from flask import Flask, flash, redirect, render_template, url_for

from forms.cliente_form import ClienteForm
from forms.facturacion_form import FacturacionForm
from forms.producto_form import ProductoForm
from forms.proveedor_form import ProveedorForm

app = Flask(__name__)

# Flask-WTF utiliza esta clave para generar y comprobar el token CSRF.
# En producción se debe definir SECRET_KEY como variable de entorno.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "clave-segura-semana-11-casa-del-clavo")

# Ruta absoluta: la base se conserva aunque cambie la carpeta de ejecución.
app.config["DATABASE"] = Path(__file__).resolve().parent / "data" / "ferreteria.db"


def conectar_db():
    ruta = Path(app.config["DATABASE"])
    ruta.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(ruta))
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_db():
    conn = conectar_db()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL UNIQUE,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                precio REAL NOT NULL CHECK (precio > 0),
                stock INTEGER NOT NULL CHECK (stock >= 0),
                descripcion TEXT NOT NULL
            )
        """)
        conn.commit()
    finally:
        conn.close()


def consultar_productos():
    conn = conectar_db()
    try:
        return conn.execute("SELECT * FROM productos ORDER BY id").fetchall()
    finally:
        conn.close()


inicializar_db()

# ==========================================================
# DATOS TEMPORALES
# Clientes, proveedores y facturación conservan su almacenamiento temporal.
# Productos utiliza SQLite desde la Semana 12.
# ==========================================================

# Variable simple
NOMBRE_NEGOCIO = "Ferretería La Casa del Clavo"

# Diccionario con información general del sistema
INFO_NEGOCIO = {
    "nombre": "Ferretería La Casa del Clavo",
    "ciudad": "Puyo",
    "provincia": "Pastaza",
    "telefono": "099 555 1234",
    "correo": "contacto@casadelclavo.com",
    "horario": "Lunes a sábado de 08:00 a 18:00"
}

# Lista de diccionarios: clientes
CLIENTES = [
    {
        "id": 1,
        "nombre": "María López",
        "telefono": "0987654321",
        "correo": "maria@example.com",
        "activo": True
    },
    {
        "id": 2,
        "nombre": "Carlos Pérez",
        "telefono": "0991234567",
        "correo": "carlos@example.com",
        "activo": True
    },
    {
        "id": 3,
        "nombre": "Ana Torres",
        "telefono": "0974567890",
        "correo": "ana@example.com",
        "activo": False
    },
    {
        "id": 4,
        "nombre": "Luis Mendoza",
        "telefono": "0963344556",
        "correo": "luis@example.com",
        "activo": True
    }
]

# Lista de diccionarios: proveedores
PROVEEDORES = [
    {
        "id": "PR01",
        "empresa": "Distribuidora Andina",
        "contacto": "Luis Andrade",
        "telefono": "032888100",
        "producto": "Herramientas",
        "estado": "Activo"
    },
    {
        "id": "PR02",
        "empresa": "Materiales Oriente",
        "contacto": "Paola Silva",
        "telefono": "032889200",
        "producto": "Materiales de construcción",
        "estado": "Activo"
    },
    {
        "id": "PR03",
        "empresa": "Fijaciones Ecuador",
        "contacto": "José Molina",
        "telefono": "022334455",
        "producto": "Tornillos y pernos",
        "estado": "Inactivo"
    }
]

# Lista de diccionarios: facturas
FACTURAS = [
    {
        "numero": "F-001",
        "cliente": "María López",
        "fecha": "2026-08-10",
        "total": 104.25,
        "estado": "Pagada"
    },
    {
        "numero": "F-002",
        "cliente": "Carlos Pérez",
        "fecha": "2026-08-12",
        "total": 31.05,
        "estado": "Pendiente"
    },
    {
        "numero": "F-003",
        "cliente": "Ana Torres",
        "fecha": "2026-08-14",
        "total": 85.50,
        "estado": "Pagada"
    },
    {
        "numero": "F-004",
        "cliente": "Luis Mendoza",
        "fecha": "2026-08-18",
        "total": 42.75,
        "estado": "Pendiente"
    }
]


@app.route("/")
def inicio():
    # Variables simples y diccionario enviados a index.html
    mensaje = "Bienvenidos a nuestro sistema de gestión comercial."
    total_productos = len(consultar_productos())
    total_clientes = len(CLIENTES)
    total_proveedores = len(PROVEEDORES)
    total_facturas = len(FACTURAS)

    return render_template(
        "index.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        mensaje=mensaje,
        info=INFO_NEGOCIO,
        total_productos=total_productos,
        total_clientes=total_clientes,
        total_proveedores=total_proveedores,
        total_facturas=total_facturas
    )


@app.route("/productos")
def productos():
    return render_template(
        "productos.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        productos=consultar_productos()
    )


@app.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        conn = conectar_db()
        try:
            conn.execute(
                """INSERT INTO productos
                   (codigo, nombre, categoria, precio, stock, descripcion)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (form.codigo.data.strip().upper(), form.nombre.data.strip(),
                 form.categoria.data, float(form.precio.data), form.stock.data,
                 form.descripcion.data.strip()),
            )
            conn.commit()
        except sqlite3.IntegrityError:
            conn.rollback()
            form.codigo.errors.append("Ya existe un producto con este código.")
        else:
            flash("Producto registrado correctamente en SQLite.", "success")
            return redirect(url_for("productos"))
        finally:
            conn.close()
    return render_template("formulario_producto.html", form=form, nombre_negocio=NOMBRE_NEGOCIO)


@app.route("/clientes")
def clientes():
    return render_template(
        "clientes.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        clientes=CLIENTES
    )


@app.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        siguiente_id = max((cliente["id"] for cliente in CLIENTES), default=0) + 1
        CLIENTES.append({
            "id": siguiente_id,
            "nombre": form.nombre.data.strip(),
            "telefono": form.telefono.data.strip(),
            "correo": form.correo.data.strip().lower(),
            "activo": form.activo.data,
        })
        flash("Cliente registrado correctamente.", "success")
        return redirect(url_for("clientes"))
    return render_template("formulario_cliente.html", form=form, nombre_negocio=NOMBRE_NEGOCIO)


@app.route("/proveedores")
def proveedores():
    return render_template(
        "proveedores.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        proveedores=PROVEEDORES
    )


@app.route("/proveedores/nuevo", methods=["GET", "POST"])
def nuevo_proveedor():
    form = ProveedorForm()
    if form.validate_on_submit():
        PROVEEDORES.append({
            "id": form.identificador.data.strip().upper(),
            "empresa": form.empresa.data.strip(),
            "contacto": form.contacto.data.strip(),
            "telefono": form.telefono.data.strip(),
            "producto": form.producto.data.strip(),
            "estado": form.estado.data,
        })
        flash("Proveedor registrado correctamente.", "success")
        return redirect(url_for("proveedores"))
    return render_template("formulario_proveedor.html", form=form, nombre_negocio=NOMBRE_NEGOCIO)


@app.route("/facturacion")
def facturacion():
    total_ventas = sum(factura["total"] for factura in FACTURAS)

    return render_template(
        "facturacion.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        facturas=FACTURAS,
        total_ventas=total_ventas
    )


@app.route("/facturacion/nueva", methods=["GET", "POST"])
def nueva_factura():
    form = FacturacionForm()
    form.cliente.choices = [(cliente["nombre"], cliente["nombre"]) for cliente in CLIENTES if cliente["activo"]]
    if form.validate_on_submit():
        FACTURAS.append({
            "numero": form.numero.data.strip().upper(),
            "cliente": form.cliente.data,
            "fecha": form.fecha.data.isoformat(),
            "total": float(form.total.data),
            "estado": form.estado.data,
        })
        flash("Factura registrada correctamente.", "success")
        return redirect(url_for("facturacion"))
    return render_template("formulario_facturacion.html", form=form, nombre_negocio=NOMBRE_NEGOCIO)


if __name__ == "__main__":
    app.run(debug=True)
