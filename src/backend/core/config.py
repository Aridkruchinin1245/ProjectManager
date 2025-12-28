from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = 'ProjectManager'
    VERSION: str = '0.0.1'
    API_V1_STR: str = 'api/v1'

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_HOST: str

    @property
    def async_db_url(self) -> str:
        url = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return url
    
    @property
    def sync_db_url(self) -> str:
        url = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return url


    model_config = SettingsConfigDict(env_file='backend/core/.env')

settings = Settings()
