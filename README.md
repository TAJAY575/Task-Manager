# Task Manager API 📋

A clean and efficient RESTful API built with FastAPI and SQLModel for managing tasks.

## Features ✨

- CRUD operations for tasks
- SQLite database with SQLModel ORM
- Auto-generated API documentation
- Task status tracking (Pending/In Progress/Completed)

## API Testing Guide with Postman 🚀

### Prerequisites
- [Python](https://python.org) 3.8 or higher
- [Postman](https://www.postman.com/downloads/) for API testing
- Git

### Installation

bash
# Clone the repository
git clone https://github.com/yourusername/task-manager-api.git

# Navigate to project directory
cd task-manager-api

# Create virtual environment
python -m venv myenv

# Activate virtual environment
# For Windows:
myenv\Scripts\activate
# For macOS/Linux:
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the main.py


## API Endpoints 

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| POST   | `/tasks`           | Create a new task   |
| GET    | `/tasks`           | List all tasks      |
| GET    | `/tasks/{task_id}` | Get a specific task |
| PUT    | `/tasks/{task_id}` | Update a task       |
| DELETE | `/tasks/{task_id}` | Delete a task       |

## Task Model 📝

    python
class Task:
    id: int              # Auto-generated
    title: str           # Required
    description: str     # Optional
    due_date: datetime   # Required
    status: TaskStatus   # Pending/In Progress/Completed


## Project Structure 📁

task-manager/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── database.py       # Database configuration
│   ├── config.py         # Settings
│   ├── models/
│   │   └── task.py      # Task models
│   └── routers/
│       └── tasks.py      # Task endpoints
└── requirements.txt


## Dependencies 📚

fastapi>=0.68.0
sqlmodel>=0.0.8
pydantic-settings>=2.0.0
uvicorn>=0.15.0


## Development / Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

To contribute to this project:

1. Fork the repository #Creates your own copy of the repository on your GitHub account
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Documentation 📖

After running the server, access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Error Handling 🚨

The API includes comprehensive error handling:
- 404: Resource not found
- 422: Validation error
- 500: Server error

## Future Enhancements 🚀

- [ ] Task categories
- [ ] Priority levels
- [ ] Search functionality
- [ ] Task filtering
- [ ] Task sorting
- [ ] Front end

## Acknowledgments 🙏

- FastAPI documentation
- SQLModel documentation
- Python community


Remember to ⭐ this repository if you found it helpful!

