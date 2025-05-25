from typing import Optional
from datetime import date
from sqlmodel import SQLModel


# Paciente
class PacienteBase(SQLModel):
    nome_paciente: str
    data_nascimento: date
    cpf: str
    sexo: Optional[str] = None
    telefone: Optional[str] = None

class PacienteCreate(PacienteBase):
    pass

class PacienteRead(PacienteBase):
    id: int


# Prontuário
class ProntuarioBase(SQLModel):
    id_paciente: Optional[int] = None
    data_consulta: Optional[date] = None
    queixa_principal: str
    historia_doenca_atual: Optional[str] = None
    historico_medico_pregressa: Optional[str] = None
    historico_familiar: Optional[str] = None
    medicamentos_em_uso: Optional[str] = None
    alergias: Optional[str] = None
    pressao_arterial: Optional[str] = None
    frequencia_cardiaca: Optional[str] = None
    temperatura: Optional[str] = None
    observacoes_exame_fisico: Optional[str] = None
    hipoteses_diagnosticas: Optional[str] = None
    diagnostico_definitivo: Optional[str] = None
    prescricao: Optional[str] = None
    orientacoes: Optional[str] = None

class ProntuarioCreate(ProntuarioBase):
    pass

class ProntuarioRead(ProntuarioBase):
    id: int
