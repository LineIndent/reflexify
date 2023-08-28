import pytest  # noqa: F401
from app.config import app_configuration


@pytest.fixture
def config():
    return app_configuration


def test_config_data_type(config):
    assert isinstance(config, dict)


def test_config_navigation_key(config):
    assert "navigation" in config.keys()
