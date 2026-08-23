# Semana 10 - Contenido dinámico con Flask y Jinja2

## Proyecto
**Ferretería La Casa del Clavo**

Este proyecto continúa el trabajo desarrollado en la Semana 9 e incorpora contenido dinámico utilizando Flask y Jinja2.

## Requisitos evidenciados

- Variable simple enviada desde Flask.
- Listas de Python.
- Diccionarios.
- `render_template()`.
- Variables Jinja2 con `{{ variable }}`.
- Bucles `{% for %}`.
- Condicionales `{% if %}` y `{% else %}`.
- Filtros como `upper`, `lower` y `format`.
- Herencia mediante `{% extends "base.html" %}`.
- Componentes reutilizables:
  - `components/navbar.html`
  - `components/footer.html`
- Navegación con `url_for()`.
- Archivos CSS y JavaScript desde `static`.
- Bootstrap.
- Sin base de datos.

## Estructura

```text
Semana_10_Ferreteria_La_Casa_del_Clavo/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── productos.html
│   ├── clientes.html
│   ├── proveedores.html
│   ├── facturacion.html
│   │
│   └── components/
│       ├── navbar.html
│       └── footer.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── img/
```

## Ejecución

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar en Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecutar:

```bash
python app.py
```

6. Abrir:

```text
http://127.0.0.1:5000
```

## Rutas a comprobar

- `/`
- `/productos`
- `/clientes`
- `/proveedores`
- `/facturacion`

## Nota sobre GitHub Pages

GitHub Pages no ejecuta Flask ni Python. Debe mantenerse publicada la parte frontend estática del proyecto, mientras que el repositorio debe contener la aplicación Flask completa para su revisión.
