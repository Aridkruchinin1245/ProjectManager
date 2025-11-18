from fastapi import APIRouter
from backend.api.v1.endpoints.auth_reg import auth_reg_router
from backend.api.v1.endpoints.utils import utils_router

router_v1 = APIRouter()

router_v1.include_router(auth_reg_router)
router_v1.include_router(utils_router)