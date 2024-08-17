from fastapi import APIRouter

from src.backend.backend.schemas import DefaultResponse

router = APIRouter(prefix="/api")


@router.get("/", response_model=DefaultResponse, tags=["API"])
async def root():
    return DefaultResponse(error=False, message="OK", payload=None)
