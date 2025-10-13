📘 Proyecto de Gestión de Inscripción de Materias Universitarias

Este proyecto es una aplicación para la gestión de inscripción de materias, implementado siguiendo el patrón arquitectónico por capas. Utiliza Python, Flask como framework web y SQLAlchemy como ORM con SQLite para la interacción con bases de datos relacionales.

📝 Descripción General

El sistema permite registrar, consultar, actualizar y eliminar sus respectivas inscripciones de materias. La arquitectura por capas facilita la separación de responsabilidades, mejorando la mantenibilidad, escalabilidad y flexibilidad del código.



📂 Estructura del Proyecto

DEV/

│

├── config/                    → Configuración de la base de datos

│   └── (archivos de configuración)

│

├── controllers/               → Controladores (lógica de endpoints)

│   ├── \_\_pycache\_\_/

│   ├── \_\_init\_\_.py

│   ├── uni\_controller.py      → Controlador de universidades

│   └── user\_controller.py     → Controlador de usuarios

│

├── instance/                  → Instancia de la aplicación

│   ├── app.db                 → Base de datos SQLite principal

│   ├── Universiada.db         → Base de datos de universidades

│   └── Universida.db          → Base de datos auxiliar

│

├── models/                    → Modelos de datos (entidades del dominio)

│   ├── \_\_pycache\_\_/

│   ├── \_\_init\_\_.py

│   ├── db.py                  → Configuración de la base de datos

│   ├── uni\_model.py           → Modelo de Universidad

│   └── user\_model.py          → Modelo de Usuario

│

├── repositories/              → Capa de acceso a datos (patrón Repository)

│   ├── \_\_pycache\_\_/

│   ├── \_\_init\_\_.py

│   ├── uni\_repositories.py    → Repositorio de universidades

│   └── user\_repositories.py   → Repositorio de usuarios

│

├── scripts/                   → Scripts de utilidad

│   └── add\_user.py            → Script para agregar usuarios

│

├── services/                  → Capa de servicios (lógica de negocio)

│   ├── \_\_pycache\_\_/

│   ├── \_\_init\_\_.py

│   ├── uni\_services.py        → Servicios de universidades

│   └── user\_services.py       → Servicios de usuarios

│

├── main.py                    → Punto de entrada de la aplicación

├── README.md                  → Documentación del proyecto

└── Universiada.db             → Base de datos de respaldo







🚀 Ejecución del proyecto

Una vez instaladas las dependencias y configurado el entorno, ejecuta la aplicación:



-> python main.py



La aplicación estará disponible en http://localhost:5000



🗄️ Base de Datos

El proyecto utiliza SQLite como sistema de gestión de base de datos, lo que ofrece:



Portabilidad: La base de datos es un único archivo fácil de mover y respaldar.

Ligereza: No requiere servidor de base de datos separado.

Simplicidad: Ideal para desarrollo y aplicaciones de tamaño pequeño a mediano.

Sin configuración: Funciona sin necesidad de instalación o configuración adicional.



Las bases de datos se almacenan en la carpeta instance/, que es ignorada por el control de versiones para proteger datos sensibles.



📄 Licencia

Este proyecto es de uso libre para fines educativos y de aprendizaje. Se proporciona "tal cual" sin garantías de ningún tipo.

👨‍💻 Autor

Desarrollado por Brayan Franco



Configuración de postman 

https://drive.google.com/file/d/1KImT4W8lLjblNk-9cxVERBGl-zJrR2\_0/view?usp=sharing







python -m pip install flask
python -m pip install flask-sqlalchemy
pip install python-dotenv

