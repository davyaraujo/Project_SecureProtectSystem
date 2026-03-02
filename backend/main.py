from fastapi import FastAPI
from database import Base, engine
from routers import events

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "SecureVision API", 
              description = "API para o sistema de segurança inteligente", 
              version = "1.0.0")

app.include_router(events.router)


@app.get("/")



def root():
    return {"message": "SecureVision rodando!"}


