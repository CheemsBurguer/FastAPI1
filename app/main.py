from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool

products = ["laptop", "pou", "002 plush"]

@app.get("/productos")
def listar_productos():
    return {"porductos": products}


@app.post("/productos")
def agregar_producto(producto: Producto):
    products.append(producto)
    return {"mensaje": "producto agregado con exito", "producto": producto}


@app.put("/productos/{id}")
def actualizar_producto(id: int, nombre: str):
    products[id] = nombre
    return {"mensaje": "producto actualizado con exito", "producto": nombre}

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    eliminado = products.pop(id)
    return {"mensaje": "producto eliminado con exito", "producto": eliminado}