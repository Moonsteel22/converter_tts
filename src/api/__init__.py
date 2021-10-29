from fastapi import APIRouter

from src.api.converter import router as c_router


router = APIRouter()

router.include_router(c_router)
