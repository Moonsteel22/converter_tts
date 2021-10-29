from fastapi import APIRouter

router = APIRouter(
    prefix="/converter",
)


@router.get("/")
async def converter_hello():
    return {"converter": "hello"}
