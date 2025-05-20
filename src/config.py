from pydantic_settings import SettingsConfigDict, BaseSettings
from dotenv import find_dotenv

class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEYS: set[str]

    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        extra='ignore'
    )


settings = Settings()
