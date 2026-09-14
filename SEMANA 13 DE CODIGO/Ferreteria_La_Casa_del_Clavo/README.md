# Proyecto Integrador — Ferretería La Casa del Clavo

Aplicación Flask conectada a MySQL. Mantiene los formularios Flask-WTF, CSRF,
validaciones, herencia Jinja2, componentes, Bootstrap, CSS y JavaScript de las
semanas anteriores. Los cuatro módulos usan datos persistentes y el módulo de
Productos implementa el CRUD completo solicitado.

## Funcionalidades implementadas

- Base relacional MySQL con tablas `productos`, `proveedores`, `clientes` y `facturas`.
- Claves primarias en todas las tablas.
- Claves foráneas Producto–Proveedor y Factura–Cliente.
- Listado de productos mediante `SELECT`, `fetchall()` y una tabla Jinja2.
- Consulta relacionada `INNER JOIN` para mostrar el proveedor de cada producto.
- Registro mediante Flask-WTF, `validate_on_submit()`, `INSERT` y `commit()`.
- Edición que recupera un registro con `WHERE`, carga el formulario y ejecuta `UPDATE`.
- Eliminación individual con `DELETE ... WHERE`, confirmación visual y CSRF.
- Consultas parametrizadas con `%s`; no se concatenan datos del usuario.
- Cierre garantizado de cursores y conexiones; `rollback()` ante errores.
- Credenciales por variables de entorno; `.env` está excluido de Git.
- Clientes, proveedores y facturas también se consultan y registran en MySQL.

## 1. Crear la base de datos

Instale MySQL Community Server y abra MySQL Workbench. En Workbench, abra el
archivo `sql/esquema.sql` y ejecútelo completo con el icono del rayo. El script
crea la base, las tablas, relaciones y datos iniciales.

También puede hacerlo desde una terminal:

```powershell
mysql -u root -p < sql\esquema.sql
```

## 2. Configurar el proyecto en Windows

Desde la carpeta que contiene `app.py`:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edite `.env` con sus propios datos. En PowerShell cargue las variables antes de
iniciar Flask:

```powershell
$env:SECRET_KEY="una-clave-larga-y-unica"
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
$env:DB_USER="root"
$env:DB_PASSWORD="SU_CONTRASENA"
$env:DB_NAME="ferreteria_casa_clavo"
$env:FLASK_DEBUG="1"
python app.py
```

Abra <http://127.0.0.1:5000>.

## 3. Prueba obligatoria y evidencias

1. Abra Productos y capture el listado obtenido desde MySQL.
2. Cree un producto con un código nuevo y capture el formulario y el mensaje de éxito.
3. En Workbench ejecute `SELECT * FROM productos;` y capture el registro creado.
4. Pulse Editar, cambie precio o stock y guarde. Capture la interfaz.
5. Repita el `SELECT` en Workbench y capture el valor actualizado.
6. Pulse Eliminar, acepte la confirmación y capture el listado sin el registro.
7. Repita el `SELECT` para evidenciar que ya no existe.
8. Detenga Flask, vuelva a ejecutar `python app.py` y capture que los cambios permanecen.

Consultas de apoyo para Workbench:

```sql
USE ferreteria_casa_clavo;
SELECT * FROM productos ORDER BY id_producto;
SELECT p.codigo, p.nombre, pr.nombre AS proveedor
FROM productos p
INNER JOIN proveedores pr ON pr.id_proveedor = p.id_proveedor;
```

## 4. Subir al mismo repositorio de GitHub

```powershell
git status
git add .
git commit -m "Integrar Flask con MySQL y CRUD de productos"
git push
```

No suba `.env`, contraseñas ni el entorno `venv`. Entregue el enlace del
repositorio. GitHub Pages solo muestra el frontend estático; Flask y MySQL deben
demostrarse localmente, tal como indica la guía.

## Estructura principal

```text
Ferreteria_La_Casa_del_Clavo/
├── app.py
├── requirements.txt
├── .env.example
├── conexion/
│   ├── __init__.py
│   └── conexion.py
├── sql/
│   └── esquema.sql
├── forms/
├── templates/
└── static/
```
