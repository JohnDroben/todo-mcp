from fastapi import FastAPI
import httpx
from pydantic import BaseModel
from typing import List
import os

app = FastAPI(title="API proxy")


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


MCP_URL = os.environ.get("MCP_URL", "http://mcp-server:8000")


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    r = httpx.get(f"{MCP_URL}/tasks")
    r.raise_for_status()
    return r.json()


class CreateTask(BaseModel):
    title: str


@app.post("/tasks", response_model=Task)
def create_task(payload: CreateTask):
    r = httpx.post(f"{MCP_URL}/tasks", json=payload.dict())
    r.raise_for_status()
    return r.json()
from fastapi import FastAPI
import httpx
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API proxy")


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


MCP_URL = "http://mcp-server:8000"


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    r = httpx.get(f"{MCP_URL}/tasks")
    r.raise_for_status()
    return r.json()


class CreateTask(BaseModel):
    title: str


@app.post("/tasks", response_model=Task)
def create_task(payload: CreateTask):
    r = httpx.post(f"{MCP_URL}/tasks", json=payload.dict())
    r.raise_for_status()
    return r.json()
