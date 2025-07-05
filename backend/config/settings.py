from pydantic_settings import BaseSettings, SettingsConfigDict # <--- Impor SettingsConfigDict
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str

    # config
    model_config = SettingsConfigDict(env_file=".env", extra='ignore') # <--- Perbarui baris ini

settings = Settings()