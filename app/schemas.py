from pydantic import BaseModel, ConfigDict, EmailStr

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


#### Usuarios


class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    es_admin: bool = False

class UsuarioResponse(UsuarioBase):
    id: int
    es_admin: bool