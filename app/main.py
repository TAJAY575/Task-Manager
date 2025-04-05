from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from database import create_db_and_tables
from routers import tasks
from fastapi.templating import Jinja2Templates

# Lifespan context manager to handle lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    create_db_and_tables()
    yield
    pass
    
    
app = FastAPI(lifespan=lifespan, title="Task Manager API")
app.include_router(tasks.router, tags=["tasks"])
app.mount("/static", StaticFiles(directory="app/static"), name="static")

BASE_DIR = "app/templates"
templates = Jinja2Templates(BASE_DIR)


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

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