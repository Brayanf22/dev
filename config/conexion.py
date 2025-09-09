import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.uni_model import Base
logging.basicConfig(level=logging.INFO)

# Ruta de la base de datos SQLite (archivo local en tu proyecto Codespaces)
SQLITE_URI = "sqlite:///Universiada.db"

# Crear motor de conexión a SQLite
engine = create_engine(SQLITE_URI, echo=True)

# Crear la clase Session para abrir sesiones con la BD
Session = sessionmaker(bind=engine)

# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(engine)

def get_db_session():
    """
    Retorna una nueva sesión de base de datos para ser utilizada en los servicios o controladores.
    """
    return Session()
