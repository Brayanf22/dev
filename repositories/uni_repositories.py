from models.uni_model import Universidad
from sqlalchemy.orm import Session

class UniRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_uni(self):
        return self.db.query(Universidad).all()
        
    def get_uni_by_id(self, uni_id: int):
        return self.db.query(Universidad).filter(Universidad.id == uni_id).first()

    def create_uni(self, nombre: str, codigo: str, carrera: str):
        new_uni = Universidad(nombre=nombre, codigo=codigo, carrera=carrera)
        self.db.add(new_uni)
        self.db.commit()
        self.db.refresh(new_uni)
        return new_uni
    
    def update_uni(self, uni_id: int, nombre: str = None, codigo: str = None, carrera: str = None):
        uni = self.get_uni_by_id(uni_id)
        if uni:
            if nombre:
                uni.nombre = nombre
            if codigo:
                uni.codigo = codigo
            if codigo:
                uni.carrera = carrera
            self.db.commit()
            self.db.refresh(uni)
        return uni

    def delete_uni(self, uni_id: int):
        uni = self.get_uni_by_id(uni_id)
        if uni:
            self.db.delete(uni)
            self.db.commit()
        return uni
