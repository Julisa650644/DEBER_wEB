# Semana 11 - Formularios con Flask-WTF y WTForms

## Proyecto integrador

**Ferretería La Casa del Clavo**

Este avance conserva el contenido dinámico de la Semana 10 e incorpora formularios del lado del servidor para los módulos de productos, clientes, proveedores y facturación. Los datos se guardan temporalmente en listas de Python y se pierden al reiniciar la aplicación, porque todavía no se utiliza una base de datos.

## Funciones incorporadas

- Carpeta `forms` con una clase `FlaskForm` independiente para cada módulo.
- Campos de texto, correo, fecha, números, listas de selección, área de texto y casilla de verificación.
- Validadores `DataRequired`, `InputRequired`, `Length`, `Email`, `NumberRange` y `Regexp`.
- Rutas con métodos `GET` y `POST`.
- Comprobación con `form.validate_on_submit()` antes de procesar información.
- Protección CSRF mediante `SECRET_KEY` y `form.hidden_tag()`.
- Mensajes de error debajo de cada campo.
- Mensajes de confirmación después de un registro válido.
- Estilos Bootstrap y herencia desde `base.html`.
- Componente reutilizable `campo_formulario.html` para evitar repetir código.

## Estructura

```text
Semana_11_Ferreteria_La_Casa_del_Clavo/
│
├── app.py
├── requirements.txt
├── README.md
│
├── forms/
│   ├── __init__.py
│   ├── producto_form.py
│   ├── cliente_form.py
│   ├── proveedor_form.py
│   └── facturacion_form.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── productos.html
│   ├── formulario_producto.html
│   ├── clientes.html
│   ├── formulario_cliente.html
│   ├── proveedores.html
│   ├── formulario_proveedor.html
│   ├── facturacion.html
│   ├── formulario_facturacion.html
│   └── components/
│       ├── navbar.html
│       ├── footer.html
│       └── campo_formulario.html
│
└── static/
    ├── css/style.css
    ├── js/script.js
    └── img/
```

## Ejecución paso a paso en Windows

1. Descomprima el proyecto y abra su carpeta en Visual Studio Code.
2. Abra una terminal desde `Terminal > New Terminal`.
3. Cree el entorno virtual:

```powershell
python -m venv venv
```

4. Active el entorno en PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, ejecute primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

5. Instale las dependencias:

```powershell
pip install -r requirements.txt
```

6. Ejecute la aplicación:

```powershell
python app.py
```

7. Abra en el navegador `http://127.0.0.1:5000`.

## Rutas para comprobar

- `/` - Inicio.
- `/productos` y `/productos/nuevo`.
- `/clientes` y `/clientes/nuevo`.
- `/proveedores` y `/proveedores/nuevo`.
- `/facturacion` y `/facturacion/nueva`.

## Pruebas solicitadas

1. Abra cada formulario y presione **Guardar** sin completar los campos. Deben aparecer mensajes de validación.
2. En clientes, escriba un teléfono incompleto y un correo sin formato válido. El formulario no debe procesarse.
3. En productos, escriba un precio igual a cero o un stock negativo. Deben mostrarse errores.
4. Complete correctamente todos los campos. La aplicación debe redirigir al módulo, mostrar un mensaje verde y enseñar el nuevo registro.
5. Reinicie la aplicación para comprobar que los registros agregados desaparecen. Este comportamiento es correcto en la Semana 11, ya que todavía no existe conexión a MySQL o PostgreSQL.

## Subir los cambios a GitHub

Desde la terminal, dentro del repositorio existente, ejecute:

```powershell
git status
git add .
git commit -m "Semana 11: formularios Flask-WTF y validaciones"
git push origin main
```

Después abra el repositorio en GitHub, compruebe que aparezcan `forms`, las cuatro plantillas nuevas y el `requirements.txt` actualizado, y copie la dirección del repositorio para entregarla en Moodle.

> GitHub Pages no puede ejecutar Flask ni Python. La entrega solicitada es el enlace del repositorio con todo el código; el profesor debe ejecutarlo localmente con `python app.py`.
