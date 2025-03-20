from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class BaseTask(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    due_date: datetime
    status: TaskStatus = Field(default=TaskStatus.PENDING)

class Task(BaseTask, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class CreateTask(BaseTask):
    pass

class ReadTask(BaseTask):
    id: int