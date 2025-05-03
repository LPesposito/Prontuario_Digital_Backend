import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

# Testes para Pacientes
def test_create_paciente():
    response = client.post(
        "/pacientes/",
        json={
            "id":1,
            "nome_paciente": "João Silva",
            "idade": 30,
            "sexo": "Masculino",
            "data_nascimento": "1995-05-15",
            "cpf": "12345678901",
            "telefone": "11999999999"
        },
    )
    assert response.status_code == 200
    assert response.json()["nome_paciente"] == "João Silva"
    assert response.json()["cpf"] == "12345678901"


def test_get_paciente():
    # Primeiro, cria um paciente
    client.post(
        "/pacientes/",
        json={
            "nome_paciente": "Maria Oliveira",
            "idade": 25,
            "sexo": "Feminino",
            "data_nascimento": "1998-03-10",
            "cpf": "98765432100",
            "telefone": "11988888888"
        },
    )
    # Em seguida, busca o paciente pelo ID
    response = client.get("/pacientes/2")
    assert response.status_code == 200
    assert response.json()["nome_paciente"] == "Maria Oliveira"


# Testes para Prontuários
def test_create_prontuario():
    # Primeiro, cria um paciente para associar ao prontuário
    client.post(
        "/pacientes/",
        json={
            "nome_paciente": "Carlos Souza",
            "idade": 40,
            "sexo": "Masculino",
            "data_nascimento": "1983-07-20",
            "cpf": "11122233344",
            "telefone": "11977777777"
        },
    )
    # Cria um prontuário associado ao paciente
    response = client.post(
        "/prontuarios/",
        json={
            "data_consulta": "2023-05-01",
            "queixa_principal": "Dor de cabeça",
            "historia_doenca_atual": "Dor persistente há 3 dias",
            "historico_medico_pregressa": "Nenhum",
            "historico_familiar": "Hipertensão",
            "medicamentos_em_uso": "Nenhum",
            "alergias": "Nenhuma",
            "pressao_arterial": "120/80",
            "frequencia_cardiaca": "72",
            "temperatura": "36.5",
            "observacoes_exame_fisico": "Sem alterações",
            "hipoteses_diagnosticas": "Cefaleia tensional",
            "diagnostico_definitivo": "Cefaleia tensional",
            "prescricao": "Analgésico",
            "orientacoes": "Repouso e hidratação"
        },
    )
    assert response.status_code == 200
    assert response.json()["queixa_principal"] == "Dor de cabeça"


def test_get_prontuario():
    # Busca o prontuário pelo ID
    response = client.get("/prontuarios/1")
    assert response.status_code == 200
    assert response.json()["queixa_principal"] == "Dor de cabeça"