from pydantic import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_DRIVER: str

    API_TITLE: str = "Temple API"
    API_VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    # model_config = SettingsConfigDict(env_file=".env")


settings = Settings()