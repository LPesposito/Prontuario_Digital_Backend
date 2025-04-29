from sqlalchemy import Column, ForeignKey, Integer, String, Date
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
    id_paciente = Column(ForeignKey('pacientes.id'), Integer, nullable=False)
    data_consulta = Column(Date, nullable=False)
    queixa_principal = Column(String, nullable=False)
    historia_doenca_atual = Column(String, nullable=False)
    historico_medico_pregressa = Column(String, nullable=False)
    historico_familiar = Column(String, nullable=False)
    medicamentos_em_uso = Column(String, nullable=False)
    alergias = Column(String, nullable=False)
    pressao_arterial = Column(String, nullable=False)
    frequencia_cardiaca = Column(String, nullable=False)
    temperatura = Column(String, nullable=False)
    observacoes_exame_fisico = Column(String, nullable=False)
    hipoteses_diagnosticas = Column(String, nullable=False)
    diagnostico_definitivo = Column(String, nullable=False)
    prescricao = Column(String, nullable=False)
    orientacoes = Column(String, nullable=False)