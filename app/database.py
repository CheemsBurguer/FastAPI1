from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:crismo3012@localhost:5432//ecommerce"

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

