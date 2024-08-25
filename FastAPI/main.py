from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Inputs(BaseModel):
    inp: int
    inp2: str


@app.get("/exemplo")
def example() -> str:
    return "Olá mundo!"


@app.post("/exemplo_2")
def example_2(inputs: Inputs) -> str:
    return inputs.inp2


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
