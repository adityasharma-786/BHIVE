from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    rapidapi_key: str
    dummy_username: str
    dummy_password: str
    secret_key: str = "your_secret_key_here"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
