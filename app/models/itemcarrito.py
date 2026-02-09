from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class ItemCarrito(Base):
    __tablename__ = "itemcarrito"
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    carrito_id = Column(Integer, ForeignKey("carrito.id"))
    cantidad = Column(Integer, default=1)
    producto = relationship("Producto")
    carrito = relationship("Carrito", back_populates="items")