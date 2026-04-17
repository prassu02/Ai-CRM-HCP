from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Base, engine
from agent import build_graph

app = FastAPI()
graph = build_graph()

Base.metadata.create_all(bind=engine)

@app.post("/log")
def log(data: dict):
    result = graph.invoke(data)
    return result

@app.get("/interactions")
def get():
    from tools import get_interactions
    return get_interactions({})
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)