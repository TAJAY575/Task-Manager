from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from database import create_db_and_tables
from routers import tasks

# Lifespan context manager to handle lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    create_db_and_tables()
    yield
    pass
    
app = FastAPI(lifespan=lifespan, title="Task Manager API")

# Include router without prefix
app.include_router(tasks.router, tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API"}
# start the FastAPI server
def start_server():
    try:
        print('Starting Server...')
        uvicorn.run("main:app", reload=True)
    except Exception as e:
        print(f"Error starting server: {e}")

# Run the FastAPI 
if __name__ == "__main__":
    start_server()