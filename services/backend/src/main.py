from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.constants import Algorithms
import src.algorithms.uninformed_breadth_search as uninformed_breadth_search
import src.algorithms.uninformed_uniform_cost as uninformed_uniform_cost

class Data(BaseModel):
    matrix: str
    operators: list

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/" + str(Algorithms.UNINFORMED_BREADTH_SEARCH))
async def ubs(data: Data):
    return uninformed_breadth_search.evaluate(data.matrix, data.operators)

@app.post("/" + str(Algorithms.UNINFORMED_UNIFORM_COST))
async def ubs(data: Data):
    return uninformed_uniform_cost.evaluate(data.matrix, data.operators)