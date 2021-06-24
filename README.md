# Prueba Técnica Listo

Instrucciones para preparar, instalar y levantar el proyecto

1. Ubicarse desde la terminal en la raiz de la carpeta del proyecto.
2. Verificar tener instalado python 3 y pip
3. Instalar PIPENV con: `pip install pipenv` que una herramienta que crea y maneja un entorno virtual para tus proyectos.
4. Ejecutar `pipenv install` para instalar las dependencias necesarias del proyecto.
5. Ejecutar `pipenv shell` para entrar al entorno virtual
6. Ejecutar `python3 script_db.py` para poblar la base de datos desde el archivo mydb.txt.
7. Ejecutar `python3 app.py` para levantar el proyecto
8. Ir a la url: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) para abrir el proyecto en el navegador.


## Información sobre el proyecto

En este proyecto esta creado en python con el Framework Flask, como base de datos se uso SQLite y SQLAlchemy como manejador de Base de datos para el Backend.

Para el desarrollo Frontend se utilzo el Bootstrap para aprovechar su estructura y estilos para no escribir demasiado CSS, se utiliza una fuente de google fonts y el javascript que se utiliza es Vanilla JS.