from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies.deps import get_db
from dependencies.deps_auth import get_current_user, require_admin
from schemas.usuario import UsuarioCreate, UsuarioResponse
from schemas.token import Token
from crud.usuario import obtener_usuario_por_email, crear_usuario
from fastapi.security import OAuth2PasswordRequestForm
from core.security import verify_password
from core.security import crear_token

api_router = APIRouter()

@api_router.post("/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crear_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = obtener_usuario_por_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    token = crear_token(sub=user.email, es_admin=user.es_admin)
    return {"access_token": token, "token_type": "bearer"}


@api_router.get("/usuarios/me", response_model=UsuarioResponse)
def leer_perfil(current_user = Depends(get_current_user)):
    return current_user

@api_router.get("/admin/ping")
def admin_ping(_admin = Depends(require_admin)):
    return {"ok": True, "role": "admin"}