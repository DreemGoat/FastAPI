from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 

app = FastAPI()

#Endpoint: domain/tasks/1  
#GET
#POST
#PUT
#DELETE

tasks ={
    1:{
        "name":"Daniel",
        "description":"L4AC"
    },
    2:{
        "name":"Eric",
        "description":"L4BC"
    }
}

class Task(BaseModel):
    name: str
    descritpion:str

class UpdateTask(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

@app.get("/")
def index():
    return{"First Data": "Hello World"}

#/get-task/1
@app.get("/get-task/{task_id}")
def get_task(task_id: int):
    return tasks[task_id]

#query parameter
# google.com/menu?search="bagus"
@app.get("/get-task_by_name")
def get_task(name: str):
    for task_id in tasks:
        if tasks[task_id] ["name"] == name:
            return tasks[task_id]
    return {"Error": "Task name not found"}

#post method
@app.post("/create-task/{task_id}")
def add_task(task_id: int, task:Task):
    if task_id in tasks:
        return {"Error": "Task ID already exists"}
    tasks[task_id] = task
    return tasks[task_id]

#PUT method
@app.put("/update-task/{task_id}")
def update_task(task_id: int, task:UpdateTask):
    if task_id not in tasks: 
        return {"Error:" "Tasks ID does not exist"}
    
    if tasks[task_id].name != None:
        tasks[task_id].name = task.name

    if tasks[task_id].name != None:
        tasks[task_id].name = task.classes

#delete method
@app.delete("/delete-task/{task_id}")
def delete_task(task_id: int):
    del tasks[task_id]
    return{"data": "has been deleted successfully"}