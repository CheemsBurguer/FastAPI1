from sqlalchemy.orm import Session
from models import Producto, Categoria
from schemas import ProductoCreate, CategoriaCreate

def crear_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def actualizar_producto(db: Session, producto_id: int, datos: ProductoCreate):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        return None
    for campo, valor in datos.model_dump().items():
        setattr(db_producto, campo, valor)
    
    db.commit()
    db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        return None
    db.delete(db_producto)
    db.commit()
    return db_producto


###### Categoria


def crear_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db: Session):
    return db.query(Categoria).all()


