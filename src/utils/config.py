from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    APP_NAME: str
    APP_VERSION: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int

def get_settings() -> Settings:
    return Settings()





if __name__ == "__main__":
    settings = get_settings()
    print(settings.model_dump())