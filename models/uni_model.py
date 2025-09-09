from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Universidad(Base):
    __tablename__ = 'universidades'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    codigo = Column(String(50), nullable=False, unique=True)

    carreras = relationship('Carrera', back_populates='universidad', cascade='all, delete-orphan')

class Carrera(Base):
    __tablename__ = 'carreras'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    universidad_id = Column(Integer, ForeignKey('universidades.id'))

    universidad = relationship('Universidad', back_populates='carreras')

