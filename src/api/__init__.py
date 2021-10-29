from fastapi import APIRouter

from src.api.converter import router as c_router
import math

router = APIRouter()

router.include_router(c_router)
