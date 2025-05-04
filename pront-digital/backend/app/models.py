from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional
from datetime import date


class Paciente(SQLModel, table=True):
    __tablename__ = 'pacientes'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome_paciente: str = Field(max_length=100, nullable=False)
    sexo: str = Field(max_length=10, nullable=False)
    data_nascimento: date = Field(nullable=False)
    cpf: str = Field(max_length=14, unique=True, nullable=False)
    telefone: str = Field(max_length=15, nullable=False)
    prontuarios: List["Prontuario"] = Relationship(back_populates="paciente")
    
    @property
    def idade(self) -> int:
        today = date.today()
        return today.year - self.data_nascimento.year - (
            (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )


class Prontuario(SQLModel, table=True):
    __tablename__ = 'prontuarios'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    id_paciente: int = Field(foreign_key="pacientes.id", nullable=False)
    data_consulta: date = Field(default_factory=date.today, nullable=False)
    queixa_principal: str = Field(nullable=False)
    historia_doenca_atual: str = Field(nullable=False)
    historico_medico_pregressa: str = Field(nullable=False)
    historico_familiar: str = Field(nullable=False)
    medicamentos_em_uso: str = Field(nullable=False)
    alergias: str = Field(nullable=False)
    pressao_arterial: str = Field(nullable=False)
    frequencia_cardiaca: str = Field(nullable=False)
    temperatura: str = Field(nullable=False)
    observacoes_exame_fisico: str = Field(nullable=False)
    hipoteses_diagnosticas: str = Field(nullable=False)
    diagnostico_definitivo: str = Field(nullable=False)
    prescricao: str = Field(nullable=False)
    orientacoes: str = Field(nullable=False)
    
    paciente: Optional[Paciente] = Relationship(back_populates="prontuarios")