from sqlalchemy.orm import Session
from models.carrito import Carrito
from models.itemcarrito import ItemCarrito
from sqlalchemy import and_

def obtener_carrito(db: Session, usuario_id: int):
    carrito = db.query(Carrito).filter(Carrito.usuario_id == usuario_id).first()
    if not carrito:
        carrito = Carrito(usuario_id=usuario_id)
        db.add(carrito)
        db.commit()
        db.refresh(carrito)
    return carrito

def agregar_item(db: Session, carrito_id: int, producto_id: int, cantidad: int = 1):
    item_carrito = db.query(ItemCarrito).filter(ItemCarrito.id == carrito_id, ItemCarrito.producto_id == producto_id).first()

    if not item_carrito:
        item_carrito = ItemCarrito(carrito_id=carrito_id, producto_id=producto_id, cantidad=cantidad)
        db.add(item_carrito)
    else:
        item_carrito.cantidad += cantidad

    db.commit()
    db.refresh(item_carrito)
    return item_carrito

def eliminar_item(db: Session, item_id: int):
    item_carrito = db.query(ItemCarrito).get(item_id)

    if item_carrito:
        db.delete(item_carrito)
        db.commit()

