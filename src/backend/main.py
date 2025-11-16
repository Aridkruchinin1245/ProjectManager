from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.database import create_tables


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

create_tables()

