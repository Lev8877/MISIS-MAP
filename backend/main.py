from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.floors import router as floors_router
from routers.rooms import router as rooms_router
from routers.routes import router as routes_router

from models.room_types import RoomType
from models.floors import Floor
from models.rooms import Room
from models.graph_nodes import GraphNode
from models.graph_edges import GraphEdge

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])

app.include_router(floors_router)
app.include_router(rooms_router)
app.include_router(routes_router)
