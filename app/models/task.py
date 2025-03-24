from typing import Optional
from unicodedata import category
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
    
class PriorityLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    
    
class BaseTask(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    due_date: date
    

class Task(BaseTask, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
class CreateTask(BaseTask):
    priority_level : PriorityLevel = Field (default= PriorityLevel.LOW)
    category: TaskCategory = Field(default=TaskCategory.PERSONAL)
    status: TaskStatus = Field(default=TaskStatus.PENDING)

class ReadTask(BaseTask):
    id: int
    priority_Level: PriorityLevel
    category: TaskCategory
    created_at : datetime