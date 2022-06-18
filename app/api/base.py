from fastapi import APIRouter
from app.api.routes import route_account
from app.api.routes import route_file


api_router = APIRouter()
api_router.include_router(route_account.router, prefix="/account", tags=["account"])
api_router.include_router(route_file.router, prefix="/file", tags=["file"])
