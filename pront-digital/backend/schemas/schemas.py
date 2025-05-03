from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional


class PacienteBase(BaseModel):
    nome: str = Field(alias="nome")
    idade: int
    sexo: str
    data_nascimento: date = Field(alias="data-nascimento")
    cpf: str
    telefone: str = Field(alias="telefone")


class PacienteCreate(PacienteBase):
    pass


class Paciente(PacienteBase):
    id: int
    prontuarios: Optional[List["Prontuario"]] = []  # Relacionamento com prontuários

    class Config:
        from_attributes = True
        validate_by_name = True  # Permite usar os nomes dos campos do modelo no backend


class ProntuarioBase(BaseModel):
    data_consulta: date
    queixa_principal: str = Field(alias="queixa-principal")
    historia_doenca_atual: str = Field(alias="historia-doenca-atual")
    historico_medico_pregressa: str = Field(alias="historico-medico-pregressa")
    historico_familiar: str = Field(alias="historico-familiar")
    medicamentos_em_uso: str = Field(alias="medicamentos-em-uso")
    alergias: str
    pressao_arterial: str = Field(alias="pressao-arterial")
    frequencia_cardiaca: str = Field(alias="frequencia-cardiaca")
    temperatura: str
    observacoes_exame_fisico: str = Field(alias="observacoes-exame-fisico")
    hipoteses_diagnosticas: str = Field(alias="hipoteses-diagnosticas")
    diagnostico_definitivo: str = Field(alias="diagnostico-definitivo")
    prescricao: str
    orientacoes: str


# Schema para criação de Prontuário
class ProntuarioCreate(ProntuarioBase):
    pass


class Prontuario(ProntuarioBase):
    id: int

    class Config:
        from_attributes = True
        validate_by_name = True  # Permite usar os nomes dos campos do modelo no backend