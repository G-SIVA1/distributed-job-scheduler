from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import models
import app.models.user
import app.models.project
import app.models.queue
import app.models.job
import app.models.worker

# Database
from app.database.database import engine
from app.models.base import Base

# Routers
from app.routers.auth_router import router as auth_router
from app.routers.project_router import router as project_router
from app.routers.queue_router import router as queue_router
from app.routers.job_router import router as job_router
from app.routers.worker_router import router as worker_router
from app.routers.metrics_router import router as metrics_router

# Scheduler
from app.scheduler.scheduler import start_scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Distributed Job Scheduler",
    version="1.0.0"
)

# 👇 ADD THIS HERE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(queue_router)
app.include_router(job_router)
app.include_router(worker_router)
app.include_router(metrics_router)


@app.on_event("startup")
def startup():
    start_scheduler()


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Distributed Job Scheduler API",
        "version": "1.0.0"
    }