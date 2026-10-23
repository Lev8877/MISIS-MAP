from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.floors import router as floors_router
from routers.rooms import router as rooms_router
from routers.routes import router as routes_router

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])

app.include_router(floors_router)
app.include_router(rooms_router)
app.include_router(routes_router)
