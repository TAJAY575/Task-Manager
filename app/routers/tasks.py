from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from database import get_session
from models.task import PriorityLevel, Task, CreateTask, ReadTask

router = APIRouter()

@router.post("/tasks/", response_model=ReadTask,)
def create_task(task: CreateTask, session: Session = Depends(get_session)):

    db_task = Task.model_validate(task)
    # Add to database
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.get("/tasks/", response_model=List[ReadTask])
def read_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return tasks

@router.get("/tasks/{task_id}", response_model=ReadTask)
def read_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=ReadTask)
def update_task(task_id: int,task_update: CreateTask,session: Session = Depends(get_session)):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task_data = task_update.model_dump()
    for key, value in task_data.items():
        setattr(db_task, key, value)
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task)
    session.commit()
    return {"message": "Task deleted successfully"}

@router.get("/categorized")
def get_categorized_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    
    # Categorize by status
    status_categories = {
        "pending": [task for task in tasks if task.status == "Pending"],
        "in_progress": [task for task in tasks if task.status == "In Progress"],
        "completed": [task for task in tasks if task.status == "Completed"]
    }
    
    # Categorize by date
    today = date.today()
    date_categories = {
        "overdue": [task for task in tasks if task.due_date< today],
        "today": [task for task in tasks if task.due_date == today],
        "upcoming": [task for task in tasks if task.due_date > today]
        }
    
    # Categorize by Priority 
    priorityLevel_categories = {
        "High": [task for task in tasks if task.priority_level == "High"],
        "Medium": [task for task in tasks if task.priority_level == "Medium"],
        "Low": [task for task in tasks if task.priority_level == "Low"]
        }
    return {"By Status" :status_categories , 
            "By Date" : date_categories,
            "By Priority": priorityLevel_categories}