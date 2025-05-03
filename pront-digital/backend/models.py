from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from .database import Base


class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_paciente = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    sexo = Column(String(10), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    telefone = Column(String(15), nullable=False)
    prontuarios = relationship("Prontuario", back_populates="paciente")

class Prontuario(Base): 
    __tablename__ = 'prontuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    data_consulta = Column(Date, nullable=False)
    queixa_principal = Column(Text, nullable=False)
    historia_doenca_atual = Column(Text, nullable=False)
    historico_medico_pregressa = Column(Text, nullable=False)
    historico_familiar = Column(Text, nullable=False)
    medicamentos_em_uso = Column(Text, nullable=False)
    alergias = Column(Text, nullable=False)
    pressao_arterial = Column(Text, nullable=False)
    frequencia_cardiaca = Column(Text, nullable=False)
    temperatura = Column(Text, nullable=False)
    observacoes_exame_fisico = Column(Text, nullable=False)
    hipoteses_diagnosticas = Column(Text, nullable=False)
    diagnostico_definitivo = Column(Text, nullable=False)
    prescricao = Column(Text, nullable=False)
    orientacoes = Column(Text, nullable=False)
    
    paciente = relationship("Paciente", back_populates="prontuarios")