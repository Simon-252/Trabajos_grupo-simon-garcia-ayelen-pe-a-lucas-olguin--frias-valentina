TP 2 de programacion
####Sistema de Gestión de Ventas####

Integrantes: Simón García, Ayelén Peña, Lucas Olguín, Valentina Frías. Ies 0923

API RESTful para la gestión completa de un sistema de ventas, con módulos para:
- Proveedores
- Clientes (con múltiples teléfonos)
- Productos (organizados por categorías)
- Ventas (con detalles y cálculos automáticos)

# Tecnologías 
- **Backend**: Python + Flask
- **Base de datos**: SQLite (para desarrollo) / PostgreSQL (producción)
- **ORM**: SQLAlchemy
- **Formato de datos**: JSON

#Requisitos
- Python 3.8+
- pip
- Entorno virtual (recomendado)

Para iniciar, iniciar el archivo load_data.py para cargar o reiniciar la base de datos y despues ya puede
iniciar el archivo app.py y las opciones en el local host son

                                                                        Metodos
--Lista de productos	    http://localhost:5000/api/productos         GET, POST
--Detalles de ventas	    http://localhost:5000/api/ventas            GET, POST
--Información de clientes	http://localhost:5000/api/clientes          GET, POST
--Proveedores registrados	http://localhost:5000/api/proveedores       GET, POST

...crear producto esta el archivo api_client.py en la carpeta tests



