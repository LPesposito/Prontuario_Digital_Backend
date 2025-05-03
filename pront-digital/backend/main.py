from . import crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import models
from .schemas import schemas
from .database.database import SessionLocal, engine

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rotas para Paciente
@app.post("/pacientes/", response_model=schemas.Paciente)
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente_by_cpf(db, cpf=paciente.cpf)
    if db_paciente:
        raise HTTPException(status_code=400, detail="Paciente com este CPF já existe")
    return crud.create_paciente(db=db, paciente=paciente)


@app.get("/pacientes/{paciente_id}", response_model=schemas.Paciente)
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente(db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return db_paciente


@app.get("/pacientes/", response_model=list[schemas.Paciente])
def read_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_pacientes(db, skip=skip, limit=limit)


# Rotas para Prontuário
@app.post("/prontuarios/", response_model=schemas.Prontuario)
def create_prontuario(prontuario: schemas.ProntuarioCreate, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente(db, paciente_id=prontuario.id_paciente)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return crud.create_prontuario(db=db, prontuario=prontuario)


@app.get("/prontuarios/{prontuario_id}", response_model=schemas.Prontuario)
def read_prontuario(prontuario_id: int, db: Session = Depends(get_db)):
    db_prontuario = crud.get_prontuario(db, prontuario_id=prontuario_id)
    if db_prontuario is None:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    return db_prontuario


@app.get("/prontuarios/", response_model=list[schemas.Prontuario])
def read_prontuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_prontuarios(db, skip=skip, limit=limit)


@app.get("/pacientes/{paciente_id}/prontuarios/", response_model=list[schemas.Prontuario])
def read_prontuarios_by_paciente(paciente_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente(db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return crud.get_prontuarios_by_paciente(db, paciente_id=paciente_id, skip=skip, limit=limit)

