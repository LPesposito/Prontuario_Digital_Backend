from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_create_paciente():
    response = client.post(
        "/pacientes/register",
        json={
            "nome": "João Silva",
            "idade": 30,
            "sexo": "Masculino",
            "data-nascimento": "1993-01-01",
            "cpf": "12345678901",
            "telefone": "11999999999"
        }
    )
    assert response.status_code == 200
    assert response.json()["cpf"] == "12345678901"

def test_read_paciente():
    response = client.get("/pacientes/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_register_prontuario():
    response = client.post(
        "/prontuarios/register",
        json={
            "paciente": {
                "nome": "João Silva",
                "idade": 30,
                "sexo": "Masculino",
                "data-nascimento": "1993-01-01",
                "cpf": "123.456.789-00",
                "telefone": "123456789"
            },
            "data_consulta": "2023-10-01",
            "queixa-principal": "Dor de cabeça",
            "historia-doenca-atual": "Dor persistente há 3 dias",
            "historico-medico-pregressa": "Nenhum",
            "historico-familiar": "Hipertensão",
            "medicamentos-em-uso": "Nenhum",
            "alergias": "Nenhuma",
            "pressao-arterial": "120/80",
            "frequencia-cardiaca": "70",
            "temperatura": "36.5",
            "observacoes-exame-fisico": "Sem alterações",
            "hipoteses-diagnosticas": "Cefaleia tensional",
            "diagnostico-definitivo": "Cefaleia tensional",
            "prescricao": "Analgésico",
            "orientacoes": "Repouso"
        }
    )
    assert response.status_code == 200
    assert response.json()["queixa_principal"] == "Dor de cabeça"

def test_register_prontuario_with_new_paciente():
    response = client.post(
        "/prontuarios/register",
        json={
            "nome": "Ana Paula",
            "idade": 32,
            "sexo": "Feminino",
            "data-nascimento": "1990-10-15",
            "cpf": "22233344455",
            "telefone": "11988887777",
            "data_consulta": "2023-10-01",
            "queixa-principal": "Febre alta",
            "historia-doenca-atual": "Febre persistente há 2 dias",
            "historico-medico-pregressa": "Nenhum",
            "historico-familiar": "Diabetes",
            "medicamentos-em-uso": "Nenhum",
            "alergias": "Nenhuma",
            "pressao-arterial": "110/70",
            "frequencia-cardiaca": "80",
            "temperatura": "39.0",
            "observacoes-exame-fisico": "Sem alterações",
            "hipoteses-diagnosticas": "Infecção viral",
            "diagnostico-definitivo": "Infecção viral",
            "prescricao": "Antitérmico",
            "orientacoes": "Repouso e hidratação"
        }
    )
    assert response.status_code == 200
    assert response.json()["queixa_principal"] == "Febre alta"
