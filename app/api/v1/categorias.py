from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies.deps import get_db
from schemas.categoria import CategoriaCreate, CategoriaResponse
from crud.categoria import crear_categoria, obtener_categorias

api_router = APIRouter()

@api_router.get("/categorias", response_model=list[CategoriaResponse])
def obtener_categorias(db: Session = Depends(get_db)):
    return obtener_categorias(db)

@api_router.post("/categoria", response_model=CategoriaCreate)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return crear_categoria(db, categoria)



