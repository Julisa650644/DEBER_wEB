from flask import Flask, render_template

app = Flask(__name__)

# ==========================================================
# DATOS TEMPORALES
# Esta semana no se utiliza base de datos.
# Se emplean variables, listas y diccionarios de Python.
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

# Lista de diccionarios: productos
PRODUCTOS = [
    {
        "codigo": "P001",
        "nombre": "Taladro eléctrico",
        "categoria": "Herramientas",
        "precio": 85.50,
        "stock": 12,
        "descripcion": "Taladro de uso doméstico y profesional."
    },
    {
        "codigo": "P002",
        "nombre": "Martillo profesional",
        "categoria": "Herramientas",
        "precio": 18.75,
        "stock": 25,
        "descripcion": "Martillo resistente con mango ergonómico."
    },
    {
        "codigo": "P003",
        "nombre": "Caja de tornillos",
        "categoria": "Fijaciones",
        "precio": 9.90,
        "stock": 40,
        "descripcion": "Caja surtida de tornillos para diferentes trabajos."
    },
    {
        "codigo": "P004",
        "nombre": "Tubo PVC 1/2 pulgada",
        "categoria": "Materiales",
        "precio": 6.25,
        "stock": 30,
        "descripcion": "Tubo PVC para instalaciones de agua."
    },
    {
        "codigo": "P005",
        "nombre": "Sierra manual",
        "categoria": "Herramientas",
        "precio": 14.50,
        "stock": 0,
        "descripcion": "Sierra manual para corte de madera."
    }
]

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
    total_productos = len(PRODUCTOS)
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
        productos=PRODUCTOS
    )


@app.route("/clientes")
def clientes():
    return render_template(
        "clientes.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        clientes=CLIENTES
    )


@app.route("/proveedores")
def proveedores():
    return render_template(
        "proveedores.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        proveedores=PROVEEDORES
    )


@app.route("/facturacion")
def facturacion():
    total_ventas = sum(factura["total"] for factura in FACTURAS)

    return render_template(
        "facturacion.html",
        nombre_negocio=NOMBRE_NEGOCIO,
        facturas=FACTURAS,
        total_ventas=total_ventas
    )


if __name__ == "__main__":
    app.run(debug=True)
