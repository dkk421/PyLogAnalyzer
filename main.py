from fastapi import FastAPI
from app.api.routers import Logs
from app.db.base import Base
from app.db.session import engine
from app.models import log_entry

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(Logs.router, prefix="/logs")

@app.get("/")
def root():
    return {"message": "hello"}