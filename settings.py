# settings.py
import os
import yaml
from typing import Any, Dict
from pydantic_settings import BaseSettings
from pydantic import validator

def _yaml_secret_settings(settings: BaseSettings) -> Dict[str, Any]:
    """
    Po zrobieniu sops --decrypt --in-place secrets.yaml
    """
    path = "secrets.yaml"
    if os.path.exists(path):
        with open(path, "r") as f:
            data = yaml.safe_load(f) or {}
            return {k.upper(): v for k, v in data.items()}
    return {}
        
class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    DATABASE_PASSWORD: str
    API_KEY: str
    
    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        valid_environments = {"dev", "test", "prod"}
        if value not in valid_environments:
            raise ValueError(
                f"""Invalid environment: {value}.
                Must be one of {", ".join(valid_environments)}."""
            )
        return value

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return (
                init_settings,
                env_settings,
                _yaml_secret_settings,
                file_secret_settings,
            )
