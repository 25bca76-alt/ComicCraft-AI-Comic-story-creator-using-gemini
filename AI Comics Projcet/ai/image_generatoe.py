from datetime import datetime
from pathlib import Path
import hashlib

from PIL import Image, ImageDraw

from app.config import get_settings


BASE_DIR = Path(__file__).resolve().parent.parent.parent

PANELS_DIR = BASE_DIR / "static" / "panels"

PANELS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def create_placeholder(
    prompt: str,
    panel_number: int
) -> Path:

    filename = (
        f"panel_{panel_number}_"
        f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png"
    )

    path = PANELS_DIR / filename


    image = Image.new(
        "RGB",
        (1024, 768),
        "white"
    )


    draw = ImageDraw.Draw(image)


    draw.rectangle(
        (20, 20, 1004, 748),
        outline="black",
        width=8
    )


    draw.text(
        (55, 55),
        f"ComicCraft - Panel {panel_number}",
        fill="black"
    )


    draw.text(
        (55, 130),
        prompt[:300],
        fill="black"
    )


    image.save(path)

    return path


def generate_image(
    prompt: str,
    panel_number: int
) -> Path:

    settings = get_settings()


    if not settings.hf_api_key:

        return create_placeholder(
            prompt,
            panel_number
        )


    try:

        from huggingface_hub import InferenceClient


        client = InferenceClient(
            provider="hf-inference",
            api_key=settings.hf_api_key
        )


        image = client.text_to_image(
            prompt=prompt,
            model=settings.hf_image_model
        )


        filename = (
            f"panel_{panel_number}_"
            f"{hashlib.sha256(prompt.encode()).hexdigest()[:12]}.png"
        )


        path = PANELS_DIR / filename


        image.save(path)


        return path


    except Exception:

        if settings.demo_mode:

            return create_placeholder(
                prompt,
                panel_number
            )

        raise