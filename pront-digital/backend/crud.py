from sqlalchemy.orm import Session
from .models import models
from .schemas import schemas


# Funções CRUD para Paciente
def get_paciente(db: Session, paciente_id: int):
    return db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()


def get_paciente_by_cpf(db: Session, cpf: str):
    return db.query(models.Paciente).filter(models.Paciente.cpf == cpf).first()


def get_pacientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Paciente).offset(skip).limit(limit).all()

# função auxiliar para criar um paciente
def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_paciente = models.Paciente(
        nome_paciente=paciente.nome_paciente,
        idade=paciente.idade,
        sexo=paciente.sexo,
        data_nascimento=paciente.data_nascimento,
        cpf=paciente.cpf,
        telefone=paciente.telefone,
    )
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente


# Funções CRUD para Prontuario
def get_prontuario(db: Session, prontuario_id: int):
    return db.query(models.Prontuario).filter(models.Prontuario.id == prontuario_id).first()


def get_prontuarios_by_paciente(db: Session, paciente_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Prontuario).filter(models.Prontuario.id_paciente == paciente_id).offset(skip).limit(limit).all()


def get_prontuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Prontuario).offset(skip).limit(limit).all()


def create_prontuario(db: Session, prontuario: schemas.ProntuarioCreate):
    db_prontuario = models.Prontuario(
        id_paciente=prontuario.id_paciente,
        data_consulta=prontuario.data_consulta,
        queixa_principal=prontuario.queixa_principal,
        historia_doenca_atual=prontuario.historia_doenca_atual,
        historico_medico_pregressa=prontuario.historico_medico_pregressa,
        historico_familiar=prontuario.historico_familiar,
        medicamentos_em_uso=prontuario.medicamentos_em_uso,
        alergias=prontuario.alergias,
        pressao_arterial=prontuario.pressao_arterial,
        frequencia_cardiaca=prontuario.frequencia_cardiaca,
        temperatura=prontuario.temperatura,
        observacoes_exame_fisico=prontuario.observacoes_exame_fisico,
        hipoteses_diagnosticas=prontuario.hipoteses_diagnosticas,
        diagnostico_definitivo=prontuario.diagnostico_definitivo,
        prescricao=prontuario.prescricao,
        orientacoes=prontuario.orientacoes,
    )
    db.add(db_prontuario)
    db.commit()
    db.refresh(db_prontuario)
    return db_prontuario

def register_prontuario(db: Session, prontuario_data: schemas.ProntuarioCreate, paciente_data: schemas.PacienteCreate):
    paciente = get_paciente_by_cpf(db, paciente_data.cpf)
    if not paciente:
        paciente = create_paciente(db, paciente_data)
    prontuario = models.Prontuario(
        id_paciente=paciente.id,
        **prontuario_data.dict(by_alias=True)
    )
    db.add(prontuario)
    db.commit()
    db.refresh(prontuario)
    return prontuario