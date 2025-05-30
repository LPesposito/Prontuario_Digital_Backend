# :clipboard:Prontuário Digital - Backend:computer:
### Projeto Integrador 3 - UNIVESP

Este é o backend do projeto **Prontuário Digital**, desenvolvido como parte do **Projeto Integrador 3** da faculdade que estou cursando atualmente (2025), Bacharelado em Tecnologia da Informação - UNIVESP. O objetivo do projeto é criar uma aplicação para o gerenciamento de prontuários médicos digitais.

## Sobre o Projeto

O **Prontuário Digital** é uma aplicação que visa facilitar o gerenciamento de informações de pacientes e prontuários médicos. Este repositório contém o backend da aplicação, desenvolvido em Python utilizando o framework **FastAPI**.

## Contribuintes

- **Luan Eposito** - Desenvolvimento Backend  
- **Bruno Rodling** - Desenvolvimento Frontend  

## Tecnologias Utilizadas

- **Python** (FastAPI, SQLmodel)

## Repositórios do Projeto

- **Frontend**: [GitHub - Bruno Rodling](https://github.com/Obrunorodling/meus_projetos)
- **Backend**: [GitHub - Luan Eposito](https://github.com/LPesposito/prontuario-digital)

## Como Executar o Backend

1. Clone o repositório:
   ```bash
   git clone https://github.com/LPesposito/prontuario-digital.git
   cd prontuario-digital
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # No Windows
   source .venv/bin/activate     # No Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```

Rotas da API - Prontuário Digital

### Pacientes

POST   /pacientes/registrar  
- Cadastra um novo paciente  
- Body: PacienteCreate

GET    /pacientes/  
- Lista todos os pacientes  
- Response: List[PacienteRead]

GET    /paciente/{paciente_id}  
- Busca paciente pelo ID  
- Response: PacienteRead

GET    /paciente/cpf/{cpf}  
- Busca paciente pelo CPF  
- Response: PacienteRead

### Prontuários

POST   /prontuario/resgistrar-auto  
- Cria paciente e prontuário juntos  
- Body:  
  {
    "paciente": PacienteCreate,
    "prontuario": ProntuarioCreate
  }

POST   /prontuarios/registrar-novo  
- Cadastra um novo prontuário  
- Body: ProntuarioCreate  
- Response: ProntuarioRead

GET    /prontuarios/  
- Lista todos os prontuários  
- Response: List[ProntuarioRead]

GET    /prontuario/{prontuario_id}  
- Busca prontuário pelo ID  
- Response: ProntuarioRead

GET    /paciente/{paciente_id}/prontuarios  
- Lista prontuários de um paciente  
- Response: List[ProntuarioRead]