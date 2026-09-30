from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Create FastAPI application
app = FastAPI(
    title="ComicCraft",
    description="AI Comic Story Creator",
    version="1.0.0",
)

# Static files
STATIC_DIR = BASE_DIR / "static"

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)

# Application routes
app.include_router(router)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "project": "ComicCraft"
    }