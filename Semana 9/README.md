# Semana 7 - Integración Flask

Proyecto: **Ferretería La Casa del Clavo**

## Estructura

```text
semana7/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── productos.html
│   ├── clientes.html
│   ├── proveedores.html
│   └── facturacion.html
└── static/
    ├── css/style.css
    ├── js/script.js
    └── img/ferreteria.jpg
```

## Instalación y ejecución en Visual Studio Code (Windows)

1. Abrir una terminal dentro de la carpeta `semana7`.
2. Crear el entorno virtual:
   ```powershell
   python -m venv venv
   ```
3. Activarlo:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   En CMD puede utilizar: `venv\Scripts\activate`.
4. Instalar Flask:
   ```powershell
   pip install flask
   ```
   También puede instalar las dependencias con `pip install -r requirements.txt`.
5. Ejecutar:
   ```powershell
   python app.py
   ```
6. Abrir en el navegador: `http://127.0.0.1:5000`

## Rutas que deben verificarse

- `/`
- `/productos`
- `/clientes`
- `/proveedores`
- `/facturacion`

> Nota: GitHub Pages publica archivos frontend estáticos, pero no ejecuta aplicaciones Flask/Python. El repositorio sí debe contener toda la aplicación Flask para su revisión. La publicación estática anterior puede mantenerse como frontend del proyecto.
