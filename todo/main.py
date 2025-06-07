from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允許 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開發環境可以用 "*"，生產環境要指定具體域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TODO_FILE = "todos.json"

class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return load_todos()

@app.post("/todo", response_model=Todo)
def create_todo(todo: Todo):
    todos = load_todos()
    new_id = max([t.get('id', 0) for t in todos], default=0) + 1
    new_todo = {"id": new_id, "title": todo.title, "completed": todo.completed}
    todos.append(new_todo)
    save_todos(todos)
    return new_todo

@app.put("/todo/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: Todo):
    todos = load_todos()
    for i, t in enumerate(todos):
        if t['id'] == todo_id:
            todos[i] = {"id": todo_id, "title": todo.title, "completed": todo.completed}
            save_todos(todos)
            return todos[i]
    return {"error": "Todo not found"}

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    todos = load_todos()
    todos = [t for t in todos if t['id'] != todo_id]
    save_todos(todos)
    return {"message": "Todo deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 