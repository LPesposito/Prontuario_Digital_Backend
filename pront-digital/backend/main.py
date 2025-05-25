from fastapi import FastAPI, HTTPException, Body
from typing import List
from crud import (
    create_paciente, get_pacientes, get_paciente_by_id, get_paciente_by_cpf,
    create_prontuario, get_prontuarios, get_prontuario_by_id, get_prontuarios_by_paciente_id,
    create_prontuario_com_paciente
)
from schemas import PacienteCreate, PacienteRead, ProntuarioCreate, ProntuarioRead
from models import Paciente, Prontuario
from database import create_db_and_tables

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

# rotas para pacientes
@app.post("/pacientes/registrar", response_model=PacienteRead)
def adicionar_paciente(paciente: PacienteCreate):
    paciente_model = Paciente(**paciente.model_dump())
    return create_paciente(paciente_model)

@app.get("/pacientes/", response_model=List[PacienteRead])
def listar_pacientes():
    return get_pacientes()

@app.get("/paciente/{paciente_id}", response_model=PacienteRead)
def buscar_paciente_por_id(paciente_id: int):
    paciente = get_paciente_by_id(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente

@app.get("/paciente/cpf/{cpf}", response_model=PacienteRead)
def buscar_paciente_por_cpf(cpf: str):
    paciente = get_paciente_by_cpf(cpf)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente

@app.post("/prontuario/registrar-auto")
def criar_prontuario_com_paciente(
    paciente: PacienteCreate = Body(...),
    prontuario: ProntuarioCreate = Body(...)
):
    print("Recebido POST /prontuario/registrar-auto")
    paciente_existente = get_paciente_by_cpf(paciente.cpf)
    print("Resultado get_paciente_by_cpf:", paciente_existente)
    if paciente_existente:
        paciente_obj = paciente_existente
    else:
        paciente_obj = Paciente(**paciente.model_dump())
        paciente_obj = create_paciente(paciente_obj)
        print("Paciente criado:", paciente_obj)

    prontuario_dict = prontuario.model_dump()
    prontuario_dict['id_paciente'] = paciente_obj.id
    prontuario_obj = Prontuario(**prontuario_dict)
    print("Prontuário pronto para criar:", prontuario_obj)
    resultado = create_prontuario(prontuario_obj)
    print("Prontuário criado:", resultado)
    return resultado

# rota para prontuário
@app.post("/prontuarios/registrar-novo", response_model=ProntuarioRead)
def adicionar_prontuario(prontuario: ProntuarioCreate):
    prontuario_model = Prontuario(**prontuario.model_dump())
    return create_prontuario(prontuario_model)

@app.get("/prontuarios/", response_model=List[ProntuarioRead])
def listar_prontuarios():
    return get_prontuarios()

@app.get("/prontuario/{prontuario_id}", response_model=ProntuarioRead)
def buscar_prontuario_por_id(prontuario_id: int):
    prontuario = get_prontuario_by_id(prontuario_id)
    if not prontuario:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    return prontuario

@app.get("/paciente/{paciente_id}/prontuarios", response_model=List[ProntuarioRead])
def buscar_prontuarios_por_paciente(paciente_id: int):
    return get_prontuarios_by_paciente_id(paciente_id)