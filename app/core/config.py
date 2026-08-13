from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "PulseForge"
    APP_DESCRIPTION: str = (
        "Open-source API and Stellar network health monitoring platform"
    )
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///./pulseforge.db"

    API_V1_PREFIX: str = "/api/v1"

    # Background monitoring interval (seconds)
    MONITOR_INTERVAL: int = 60

    # Stellar network configuration
    STELLAR_NETWORK: str = "testnet"
    STELLAR_RPC_URL: str = "https://soroban-testnet.stellar.org"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()
