from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import events
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "SecureVision API", 
              description = "API para o sistema de segurança inteligente", 
              version = "1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    async def connect(self,websocket:WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    def disconnect(self,websocket:WebSocket):
        self.active_connections.remove(websocket)
    async def broadcast(self,message: str):
        for connections in self.active_connections:
            await connections.send_text(message)
    
manager = ConnectionManager()

app.state.manager = manager

app.include_router(events.router)


@app.get("/")

def root():
    return {"message": "SecureVision rodando!"}

@app.websocket("/ws/live")

async def websocket_endpoint(websocket:WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)


