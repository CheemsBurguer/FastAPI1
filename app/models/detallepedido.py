from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.database import Base

class DetallePedido(Base):
    __tablename__ = "detallepedido"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedido.id"))
    producto_id = Column(Integer, ForeignKey("producto.id"))
    cantidad = Column(Integer)
    subtotal = Column(Float)
    pedido = relationship("Pedido", back_populates="detalles")
    producto = relationship("Producto")