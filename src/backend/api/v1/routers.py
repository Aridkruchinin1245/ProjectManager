from fastapi import APIRouter
from backend.api.v1.endpoints.auth_reg import auth_reg_router
from backend.api.v1.endpoints.user_data import user_data_router
from backend.api.v1.endpoints.projects_working import project_router
from backend.api.v1.endpoints.admin_handlers import admin_router
from backend.api.v1.endpoints.command_handler import command_router
from backend.api.v1.endpoints.tasks_handle import task_router


router_v1 = APIRouter()

router_v1.include_router(auth_reg_router)
router_v1.include_router(user_data_router)
router_v1.include_router(project_router)
router_v1.include_router(admin_router)
router_v1.include_router(command_router)
router_v1.include_router(task_router)