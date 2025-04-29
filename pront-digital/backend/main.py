from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/prontuario/id={prontuario_id}")
async def read_prontuario(prontuario_id: int):
    return {"prontuario_id": prontuario_id, "message": "Prontuário encontrado!"}