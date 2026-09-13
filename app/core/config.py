from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "ml" / "artifacts" / "v1" / "model.pkl"
DATA_DIR = BASE_DIR / "data"


class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()
