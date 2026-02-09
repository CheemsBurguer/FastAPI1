from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime, timezone


class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    fecha = Column(DateTime, default=datetime.now(timezone.utc))
    total = Column(Float)
    detalles = relationship("DetallePedido", back_populates="pedido")