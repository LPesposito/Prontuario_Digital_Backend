from typing import Optional
from datetime import date
from sqlmodel import SQLModel


# Paciente
class PacienteBase(SQLModel):
    nome_paciente: str
    sexo: str
    data_nascimento: date
    cpf: str
    telefone: str

class PacienteCreate(PacienteBase):
    pass

class PacienteRead(PacienteBase):
    id: int


# Prontuário
class ProntuarioBase(SQLModel):
    id_paciente: int
    data_consulta: Optional[date] = None
    queixa_principal: str
    historia_doenca_atual: str
    historico_medico_pregressa: str
    historico_familiar: str
    medicamentos_em_uso: str
    alergias: str
    pressao_arterial: str
    frequencia_cardiaca: str
    temperatura: str
    observacoes_exame_fisico: str
    hipoteses_diagnosticas: str
    diagnostico_definitivo: str
    prescricao: str
    orientacoes: str

class ProntuarioCreate(ProntuarioBase):
    pass

class ProntuarioRead(ProntuarioBase):
    id: int
