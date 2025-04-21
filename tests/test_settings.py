import pytest
from pydantic import ValidationError
from settings import Settings

def test_settings_loads_all_vars_from_env():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyTestApp"
    assert settings.DATABASE_PASSWORD == "db_secret_pass"
    assert settings.API_KEY == "some_api_key"

def test_settings_validator_rejects_bad_environment(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "invalid")
    with pytest.raises(ValidationError):
        Settings()