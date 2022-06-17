from fastapi import APIRouter
from app.api.routes import route_account


api_router = APIRouter()
api_router.include_router(route_account.router, prefix="/account", tags=["account"])
