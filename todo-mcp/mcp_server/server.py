from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="MCP Server")


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


_tasks: List[Task] = []
_next_id = 1


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return _tasks


class CreateTask(BaseModel):
    title: str


@app.post("/tasks", response_model=Task)
def create_task(payload: CreateTask):
    global _next_id
    task = Task(id=_next_id, title=payload.title, done=False)
    _tasks.append(task)
    _next_id += 1
    return task


@app.post("/tasks/{task_id}/done", response_model=Task)
def mark_done(task_id: int):
    for t in _tasks:
        if t.id == task_id:
            t.done = True
            return t
    raise HTTPException(status_code=404, detail="Task not found")
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="MCP Server")


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


_tasks: List[Task] = []
_next_id = 1


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return _tasks


class CreateTask(BaseModel):
    title: str


@app.post("/tasks", response_model=Task)
def create_task(payload: CreateTask):
    global _next_id
    task = Task(id=_next_id, title=payload.title, done=False)
    _tasks.append(task)
    _next_id += 1
    return task


@app.post("/tasks/{task_id}/done", response_model=Task)
def mark_done(task_id: int):
    for t in _tasks:
        if t.id == task_id:
            t.done = True
            return t
    raise HTTPException(status_code=404, detail="Task not found")
