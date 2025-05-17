from fastapi import APIRouter

from .customers import router as customer_router

router = APIRouter()

router.include_router(customer_router, prefix="/customers")
