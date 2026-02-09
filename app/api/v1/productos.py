from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.deps import get_db
from dependencies.deps_auth import require_admin
from schemas.producto import ProductoCreate, ProductoResponse
from crud.producto import crear_producto, obtener_productos

api_router = APIRouter()

@api_router.get("/productos", response_model=list[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return obtener_productos(db)


@api_router.post("/productos", response_model=ProductoResponse, dependencies=[Depends(require_admin)])
def agregar_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crear_producto(db, producto)


@api_router.put("/productos/{id}", response_model=ProductoCreate)
def actualizar_producto(id: int, datos: ProductoCreate, db: Session = Depends(get_db)):
    producto = actualizar_producto(db, id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="No se encontro el producto indicado")
    return producto

@api_router.delete("/productos/{id}")
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    producto = eliminar_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="No se encontro el producto indicado")
    return {"mensaje": "Producto eliminado"}