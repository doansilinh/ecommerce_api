from fastapi import APIRouter

from .customers import router as customer_router
from .employees import router as employee_router
from .products import router as product_router
from .suppliers import router as supplier_router

router = APIRouter()

router.include_router(customer_router, prefix="/customers")
router.include_router(employee_router, prefix="/employees")
router.include_router(product_router, prefix="/products")
router.include_router(supplier_router, prefix="/suppliers")
