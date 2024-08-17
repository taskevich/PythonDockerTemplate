from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.backend.routes import api_routes
from src.backend.backend.logger import logger


@asynccontextmanager
async def lifespan(_):
    logger.info("Инициализация...")
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_routes.router)
