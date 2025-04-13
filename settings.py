# settings.py
from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        # Check if the value is in the allowed values
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
