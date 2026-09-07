# Semana 12 — Ferretería La Casa del Clavo

Continuación del proyecto entregado en Semana 11. Conserva los cuatro módulos,
formularios Flask-WTF, validadores, SECRET_KEY, CSRF, Bootstrap, componentes y
herencia de plantillas. Productos ahora se almacena en SQLite.

## Ejecutar en Windows

Abra esta carpeta (la que contiene app.py) en Visual Studio Code y ejecute:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe app.py
```

Abra http://127.0.0.1:5000. Si ya activó su entorno virtual, puede ejecutar
`python app.py`. SQLite pertenece a Python y no se instala con pip.

## Cambios de esta semana

- `data/ferreteria.db`: base real, con los cinco productos originales conservados.
- `app.py`: conexión sqlite3.connect, CREATE TABLE IF NOT EXISTS, clave primaria
  id, código único, INSERT con seis parámetros ?, commit y cierre en finally.
- El INSERT ocurre únicamente después de form.validate_on_submit().
- SELECT y fetchall recuperan filas sqlite3.Row para render_template.
- `templates/productos.html`: tabla Bootstrap con ciclo for de Jinja2.
  Se conserva también el catálogo de tarjetas y sus botones de consulta.
- El contador de inicio consulta los productos de SQLite.
- Los códigos duplicados muestran un error en el formulario sin duplicar filas.
- Se actualizó requirements.txt con las dependencias directas.

La inicialización crea la tabla si falta y nunca borra ni vuelve a insertar el
catálogo al arrancar. La ruta de la base se calcula desde app.py.
Clientes, proveedores y facturación mantienen las funcionalidades anteriores y
su almacenamiento temporal. Su persistencia queda pendiente para otro avance;
el requisito mínimo de esta semana se implementa en productos.

## Comprobar la persistencia

1. Abra Productos → Nuevo producto.
2. Ingrese un código nuevo, nombre, categoría, precio mayor que cero,
   stock igual o mayor que cero y descripción. Guarde.
3. Compruebe que aparezca en la tabla y en las tarjetas.
4. Detenga Flask con Ctrl+C y ejecute nuevamente python app.py.
5. Vuelva a Productos: el registro debe seguir allí.
6. Pruebe un precio cero, stock negativo y un código ya registrado: no deben
   guardarse. Los formularios mantienen su token CSRF.

## Verificación realizada

Se comprobaron las nueve rutas GET, el registro válido con stock cero,
la recuperación en HTML, el rechazo de duplicados, el rechazo de stock negativo,
el rechazo sin token CSRF y la lectura del registro desde un proceso Python
nuevo. Se utilizó una copia temporal de la base para no incluir productos de
prueba en la entrega.

## Actualizar el mismo repositorio GitHub

Copie el contenido de esta carpeta dentro de su repositorio existente,
actualizando los archivos correspondientes y agregando data/ferreteria.db.
Conserve cualquier archivo adicional de avances anteriores.
No suba únicamente el ZIP: deben verse app.py, forms, templates, static y data.

Desde la carpeta del repositorio:

```powershell
git status
git add app.py requirements.txt README.md .gitignore forms templates static data/ferreteria.db
git commit -m "Semana 12: persistencia de productos con Flask y SQLite"
git push
```

Entregue en Moodle el enlace de ese repositorio. GitHub Pages conserva su función
como evidencia estática; este backend se comprueba localmente.
