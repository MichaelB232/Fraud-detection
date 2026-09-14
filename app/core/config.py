from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # otomatis nemu root project

MODEL_PATH = BASE_DIR / "ml" / "artifacts" / "v1" / "model.pkl"
DATA_DIR = BASE_DIR / "data"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_USER: str
    DB_PASSWORD: str
    db_host: str = "localhost"
    db_port: int = 5436
    DB_NAME: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.db_host}:{self.db_port}/{self.DB_NAME}"
        )

    secret_key: str


settings = Settings()
