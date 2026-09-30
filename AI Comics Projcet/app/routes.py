from pathlib import Path

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "ComicCraft"
        }
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    panels = [
        {
            "number": 1,
            "title": "The Beginning",
            "scene_description":
                f"{character_name} begins an adventure in {setting}.",
            "caption":
                "Every great adventure begins with a single step."
        },
        {
            "number": 2,
            "title": "The Discovery",
            "scene_description":
                f"{character_name} discovers something mysterious in {setting}.",
            "caption":
                "Something unexpected has appeared..."
        },
        {
            "number": 3,
            "title": "The Challenge",
            "scene_description":
                f"{character_name} faces a difficult challenge.",
            "caption":
                "There is no turning back now."
        },
        {
            "number": 4,
            "title": "The Turning Point",
            "scene_description":
                f"{character_name} discovers an important clue.",
            "caption":
                "The answer was closer than expected."
        },
        {
            "number": 5,
            "title": "The Ending",
            "scene_description":
                f"{character_name} completes the adventure in {setting}.",
            "caption":
                "And so, a new story begins..."
        }
    ]

    comic = {
        "story_prompt": story_prompt,
        "character_name": character_name,
        "setting": setting,
        "tone": tone,
        "art_style": art_style,
        "panels": panels
    }

    return templates.TemplateResponse(
        request=request,
        name="comic_preview.html",
        context={
            "title": "Comic Preview",
            "comic": comic,
            "panels": panels
        }
    )


@router.post("/generate-comic/json")
async def generate_comic_json(data: dict):

    return JSONResponse(
        content={
            "status": "success",
            "message": "Comic generation request received.",
            "data": data
        }
    )


@router.get("/export-success", response_class=HTMLResponse)
async def export_success(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="export_success.html",
        context={
            "title": "Export Successful",
            "message": "Your comic has been exported successfully!"
        }
    )


@router.get("/test-image")
async def test_image():

    return {
        "status": "success",
        "message": "Image generation test endpoint is working."
    }