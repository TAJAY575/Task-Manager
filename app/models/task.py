from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone, date
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class TaskCategory(str, Enum):
    WORK = "Work"
    PERSONAL = "Personal"
    SHOPPING = "Shopping"
    HEALTH = "Health"
    HOME = "Home"
    MEETING = "Meeting"
    OTHER = Optional[str]
    
class BaseTask(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    due_date: date
    category: TaskCategory = Field(default=TaskCategory.PERSONAL)
    status: TaskStatus = Field(default=TaskStatus.PENDING)

class Task(BaseTask, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))
class CreateTask(BaseTask):
    pass

class ReadTask(BaseTask):
    id: int
    created_at: datetime