from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class PacienteBase(BaseModel):
    nome_paciente: str
    idade: int
    sexo: str
    data_nascimento: date
    cpf: str
    telefone: str


class PacienteCreate(PacienteBase):
    pass


class Paciente(PacienteBase):
    id: int
    prontuarios: Optional[List["Prontuario"]] = []  # Relacionamento com prontuários

    class Config:
        from_attributes = True


class ProntuarioBase(BaseModel):
    id_paciente: int
    data_consulta: date
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


# Schema para criação de Prontuário
class ProntuarioCreate(ProntuarioBase):
    pass


class Prontuario(ProntuarioBase):
    id: int

    class Config:
        from_attributes = True