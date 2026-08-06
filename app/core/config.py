from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "PulseForge"
    APP_DESCRIPTION: str = "Open-source API health monitoring platform"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///./pulseforge.db"

    API_V1_PREFIX: str = "/api/v1"

    # Background monitoring interval (seconds)
    MONITOR_INTERVAL: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()
