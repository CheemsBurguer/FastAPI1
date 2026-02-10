from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies.deps import get_db
from crud.carrito import obtener_carrito, agregar_item, eliminar_item
from dependencies.deps_auth import get_current_user

api_router = APIRouter()

@api_router.get("/", summary="Ver contenido de carrito")
def ver_carrito(db: Session = Depends(get_db), user = Depends(get_current_user)):
    carrito = obtener_carrito(db, user.id)
    return carrito

@api_router.post("/agregar/{producto_id}")
def agregar_producto(producto_id: int, cantidad: int = 1, db: Session = Depends(get_db), user = Depends(get_current_user)):
    carrito = obtener_carrito(db, user.id)
    item_carrito = agregar_item(db, carrito.id, producto_id, cantidad)
    return {"Mensaje": "Producto agregado", "item": item_carrito}

@api_router.delete("/eliminar/{item_id}")
def eliminar_item_carrito(item_id: int, db: Session = Depends(get_db)):
    eliminar_item(item_id, db)
    return {"Mensaje": "Item eiminado del carrito con exito"}

