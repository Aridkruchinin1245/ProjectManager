from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.database import create_tables
from backend.api.v1.routers import router_v1

create_tables()

app = FastAPI()

app.include_router(router_v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

