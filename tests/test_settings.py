import pytest
from settings import Settings


@pytest.fixture
def settings():
    return Settings()


def test_settings_loads_correctly(settings):
    assert settings.APP_NAME == "MyTestApp"
    assert settings.ENVIRONMENT == "test"
