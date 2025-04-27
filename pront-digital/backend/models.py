from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_paciente = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    sexo = Column(String(10), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    telefone = Column(String(15), nullable=False)

class Prontuario(Base): 
    __tablename__ = 'prontuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)    