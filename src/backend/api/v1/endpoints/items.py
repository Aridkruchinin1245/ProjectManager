from fastapi import APIRouter

items_router = APIRouter()

@items_router.get('/items')
def get_items():
    pass