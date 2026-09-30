from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    gemini_api_key: str = ""

    gemini_outline_model: str = "gemini-2.5-flash"

    gemini_story_model: str = "gemini-2.5-pro"

    hf_api_key: str = ""

    hf_image_model: str = "stabilityai/stable-diffusion-xl-base-1.0"

    demo_mode: bool = True

    panels: int = 5

    app_name: str = "ComicCraft"


    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()