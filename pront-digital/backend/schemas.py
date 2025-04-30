from pydantic import BaseModel

class ProntuarioBase(BaseModel):
    nome: str
    
class ProntarioCreate(ProntuarioBase):
    pass

class Prontuario(ProntuarioBase):
    id: int
    nome: str

    class Config:
        orm_mode = True