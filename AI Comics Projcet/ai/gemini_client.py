import json
import re
from typing import Any

from app.config import get_settings


try:
    from google import genai
except ImportError:
    genai = None


def extract_json(text: str) -> Any:

    text = text.strip()

    text = re.sub(
        r"^```(?:json)?\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    try:
        return json.loads(text)

    except json.JSONDecodeError:

        match = re.search(
            r"(\[.*\]|\{.*\})",
            text,
            flags=re.DOTALL
        )

        if not match:
            raise ValueError(
                "Gemini did not return valid JSON."
            )

        return json.loads(match.group(1))


def get_client():

    settings = get_settings()

    if not settings.gemini_api_key:
        return None

    if genai is None:
        return None

    return genai.Client(
        api_key=settings.gemini_api_key
    )


def generate_outline(
    story_prompt: str,
    character_name: str,
    setting: str,
    tone: str,
    art_style: str
):

    settings = get_settings()

    client = get_client()


    fallback = []

    for number in range(1, settings.panels + 1):

        fallback.append({

            "panel_number": number,

            "title": f"Panel {number}",

            "scene_description":
                f"{character_name} continues the adventure in {setting}.",

            "image_prompt":
                (
                    f"{character_name} in {setting}, "
                    f"{art_style}, {tone}, "
                    f"cinematic comic panel"
                )
        })


    if client is None:

        return fallback


    prompt = f"""
Create exactly {settings.panels} connected comic panels.

Return ONLY valid JSON.

Each object must contain:

panel_number
title
scene_description
image_prompt

Story:
{story_prompt}

Main character:
{character_name}

Setting:
{setting}

Tone:
{tone}

Art style:
{art_style}

The panels must form a complete story with:

1. Beginning
2. Development
3. Conflict
4. Climax
5. Resolution

Make the image prompts visually detailed.

Do not include dialogue inside image_prompt.
"""


    response = client.models.generate_content(

        model=settings.gemini_outline_model,

        contents=prompt,

        config={
            "temperature": 0.9
        }
    )


    data = extract_json(response.text)


    if not isinstance(data, list):

        raise ValueError(
            "Gemini returned an invalid panel structure."
        )


    if len(data) != settings.panels:

        raise ValueError(
            "Gemini returned an unexpected number of panels."
        )


    return data


def generate_story(
    outline,
    character_name: str,
    tone: str
):

    client = get_client()


    fallback = []


    for panel in outline:

        fallback.append({

            **panel,

            "caption":
                f"{panel['title']} — {tone.title()} mood",

            "narration":
                (
                    f"{character_name} faces the moment "
                    f"with courage and keeps moving forward."
                )
        })


    if client is None:

        return fallback


    prompt = f"""
Expand this comic outline into a complete comic story.

Return ONLY valid JSON.

Return the same number of panels.

Every object must contain:

panel_number
title
scene_description
image_prompt
caption
narration

Character:
{character_name}

Tone:
{tone}

Outline:
{json.dumps(outline, ensure_ascii=False)}

Make the narration engaging.

Each panel should contain approximately
1 to 3 sentences.

Short character dialogue is allowed.
"""


    response = client.models.generate_content(

        model=get_settings().gemini_story_model,

        contents=prompt,

        config={
            "temperature": 0.85
        }
    )


    data = extract_json(response.text)


    if not isinstance(data, list):

        raise ValueError(
            "Gemini returned an invalid story."
        )


    if len(data) != len(outline):

        raise ValueError(
            "Gemini returned an unexpected story structure."
        )


    return data