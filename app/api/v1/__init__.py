from fastapi import APIRouter

from .endpoints import router

router_v1 = APIRouter()

router_v1.include_router(router, prefix="/v1")
