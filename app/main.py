from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool


@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)


@app.post("/productos", response_model=schemas.ProductoCreate)
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)


@app.put("/productos/{id}", response_model=schemas.ProductoCreate)
def actualizar_producto(id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="No se encontro el producto indicado")
    return producto

@app.delete("/productos/{id}")
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="No se encontro el producto indicado")
    return {"mensaje": "Producto eliminado"}

###### Categoria

@app.get("/categorias", response_model=list[schemas.CategoriaResponse])
def obtener_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)

@app.post("/categoria", response_model=schemas.CategoriaCreate)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)
