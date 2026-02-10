from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.deps import get_db
from dependencies.deps_auth import get_current_user
from crud.pedido import crear_pedido
from models.usuario import Usuario

api_router = APIRouter()

@api_router.post("/confirmar")
def confirmar_pedido(db: Session = Depends(get_db), user: Usuario = Depends(get_current_user)):
    try:
        pedido = crear_pedido(db, user.id)
        return {
            "mensaje": "Pedido generado",
            "pedido_id": pedido.id,
            "total": pedido.total
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

