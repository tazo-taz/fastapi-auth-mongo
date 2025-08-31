from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  MONGODB_URL: str
  DATABASE_NAME: str

  JWT_SECRET: str

  AUTH_COOKIE_EXP: int = 30
  AUTH_COOKIE_NAME: str = "auth_cookie"

  class Config:
    env_file = ".env"

settings = Settings()