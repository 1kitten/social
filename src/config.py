from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Configuration settings"""

    db_url: str = (
        "postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
            DB_USER=os.getenv("DB_USER"),
            DB_PASS=os.getenv("DB_PASS"),
            DB_HOST=os.getenv("DB_HOST"),
            DB_PORT=os.getenv("DB_PORT"),
            DB_NAME=os.getenv("DB_NAME"),
        )
    )
    db_echo: bool = False


settings = Settings()
