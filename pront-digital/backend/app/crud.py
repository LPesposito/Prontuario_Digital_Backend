from sqlmodel import Session, select
from models import Paciente, Prontuario
from database import engine


# ---------------- PACIENTE ----------------

def create_paciente(paciente: Paciente) -> Paciente:
    with Session(engine) as session:
        session.add(paciente)
        session.commit()
        session.refresh(paciente)
        return paciente


def get_pacientes() -> list[Paciente]:
    with Session(engine) as session:
        return session.exec(select(Paciente)).all()


def get_paciente_by_id(paciente_id: int) -> Paciente | None:
    with Session(engine) as session:
        return session.exec(
            select(Paciente).where(Paciente.id == paciente_id)
        ).first()


def get_paciente_by_cpf(cpf: str) -> Paciente | None:
    with Session(engine) as session:
        return session.exec(
            select(Paciente).where(Paciente.cpf == cpf)
        ).first()


# ---------------- PRONTUÁRIO ----------------

def create_prontuario(prontuario: Prontuario) -> Prontuario:
    with Session(engine) as session:
        paciente = session.get(Paciente, prontuario.id_paciente)
        if not paciente:
            raise ValueError("Paciente com ID fornecido não existe.")
        session.add(prontuario)
        session.commit()
        session.refresh(prontuario)
        return prontuario


def get_prontuarios() -> list[Prontuario]:
    with Session(engine) as session:
        return session.exec(select(Prontuario)).all()


def get_prontuario_by_id(prontuario_id: int) -> Prontuario | None:
    with Session(engine) as session:
        return session.exec(
            select(Prontuario).where(Prontuario.id == prontuario_id)
        ).first()


def get_prontuarios_by_paciente_id(paciente_id: int) -> list[Prontuario]:
    with Session(engine) as session:
        return session.exec(
            select(Prontuario).where(Prontuario.id_paciente == paciente_id)
        ).all()


def create_prontuario_com_paciente(paciente_data: Paciente, prontuario_data: Prontuario):
    with Session(engine) as session:
        # Tenta buscar o paciente pelo CPF
        paciente = session.exec(
            select(Paciente).where(Paciente.cpf == paciente_data.cpf)
        ).first()

        # Se não encontrar, cria um novo
        if not paciente:
            session.add(paciente_data)
            session.commit()
            session.refresh(paciente_data)
            paciente = paciente_data

        # Agora cria o prontuário com o id do paciente
        prontuario_data.id_paciente = paciente.id
        session.add(prontuario_data)
        session.commit()
        session.refresh(prontuario_data)

        return prontuario_data
