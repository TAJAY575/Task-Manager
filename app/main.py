from fastapi import FastAPI
import uvicorn
from database import create_db_and_tables
from routers import tasks

app = FastAPI(title="Task Manager API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

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