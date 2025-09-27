from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Universidad(Base):
    __tablename__ = 'universidades'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    codigo = Column(String(50), nullable=False, unique=True)
    carrera = Column(String(255), nullable=False)


