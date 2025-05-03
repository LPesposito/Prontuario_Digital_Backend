from sqlalchemy.orm import Session
from . import models    
from . import schemas
from .database import SessionLocal, engine

# dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

