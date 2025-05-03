from datetime import date
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
@app.post("/pacientes/register", response_model=schemas.Paciente)
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
@app.get("/prontuarios/{prontuario_id}", response_model=schemas.Prontuario)
def read_prontuario(prontuario_id: int, db: Session = Depends(get_db)):
    db_prontuario = crud.get_prontuario(db, prontuario_id=prontuario_id)
    if db_prontuario is None:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    return db_prontuario


@app.get("/prontuarios/", response_model=list[schemas.Prontuario])
def read_prontuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_prontuarios(db, skip=skip, limit=limit)


@app.post("/prontuarios/register", response_model=schemas.Prontuario)
def register_prontuario_endpoint(
    data: dict,  # Recebe o JSON completo do front-end
    db: Session = Depends(get_db)
):
    paciente_data = schemas.PacienteCreate(
        nome=data["nome"],
        idade=data["idade"],
        sexo=data["sexo"],
        data_nascimento=data["data-nascimento"],
        cpf=data["cpf"],
        telefone=data["telefone"]
    )
    prontuario_data = schemas.ProntuarioCreate(
        data_consulta=data["data_consulta"],
        queixa_principal=data["queixa-principal"],
        historia_doenca_atual=data["historia-doenca-atual"],
        historico_medico_pregressa=data["historico-medico-pregressa"],
        historico_familiar=data["historico-familiar"],
        medicamentos_em_uso=data["medicamentos-em-uso"],
        alergias=data["alergias"],
        pressao_arterial=data["pressao-arterial"],
        frequencia_cardiaca=data["frequencia-cardiaca"],
        temperatura=data["temperatura"],
        observacoes_exame_fisico=data["observacoes-exame-fisico"],
        hipoteses_diagnosticas=data["hipoteses-diagnosticas"],
        diagnostico_definitivo=data["diagnostico-definitivo"],
        prescricao=data["prescricao"],
        orientacoes=data["orientacoes"]
    )
    return crud.register_prontuario(db, prontuario_data=prontuario_data, paciente_data=paciente_data)

