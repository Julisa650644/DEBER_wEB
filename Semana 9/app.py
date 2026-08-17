from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo. Esta semana no se utiliza base de datos.
PRODUCTOS = [
    {"codigo": "P001", "nombre": "Taladro eléctrico", "categoria": "Herramientas", "precio": 85.50, "stock": 12},
    {"codigo": "P002", "nombre": "Martillo profesional", "categoria": "Herramientas", "precio": 18.75, "stock": 25},
    {"codigo": "P003", "nombre": "Caja de tornillos", "categoria": "Fijaciones", "precio": 9.90, "stock": 40},
    {"codigo": "P004", "nombre": "Tubo PVC 1/2 pulgada", "categoria": "Materiales", "precio": 6.25, "stock": 30},
]

CLIENTES = [
    {"id": 1, "nombre": "María López", "telefono": "0987654321", "correo": "maria@example.com"},
    {"id": 2, "nombre": "Carlos Pérez", "telefono": "0991234567", "correo": "carlos@example.com"},
    {"id": 3, "nombre": "Ana Torres", "telefono": "0974567890", "correo": "ana@example.com"},
]

PROVEEDORES = [
    {"id": "PR01", "empresa": "Distribuidora Andina", "contacto": "Luis Andrade", "telefono": "032888100", "producto": "Herramientas"},
    {"id": "PR02", "empresa": "Materiales Oriente", "contacto": "Paola Silva", "telefono": "032889200", "producto": "Materiales de construcción"},
    {"id": "PR03", "empresa": "Fijaciones Ecuador", "contacto": "José Molina", "telefono": "022334455", "producto": "Tornillos y pernos"},
]

FACTURAS = [
    {"numero": "F-001", "cliente": "María López", "fecha": "2026-08-10", "total": 104.25, "estado": "Pagada"},
    {"numero": "F-002", "cliente": "Carlos Pérez", "fecha": "2026-08-12", "total": 31.05, "estado": "Pendiente"},
    {"numero": "F-003", "cliente": "Ana Torres", "fecha": "2026-08-14", "total": 85.50, "estado": "Pagada"},
]


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/productos")
def productos():
    return render_template("productos.html", productos=PRODUCTOS)


@app.route("/clientes")
def clientes():
    return render_template("clientes.html", clientes=CLIENTES)


@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html", proveedores=PROVEEDORES)


@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html", facturas=FACTURAS)


if __name__ == "__main__":
    app.run(debug=True)
