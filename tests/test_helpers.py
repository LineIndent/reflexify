import pytest  # noqa: F401
from app.helpers.app_config import Config


def test_config_site_name():
    assert isinstance(Config.__site_name__(), str)


def test_config_repo_name():
    assert isinstance(Config.__repo_name__(), str)


def test_config_repo_url():
    assert isinstance(Config.__repo_url__(), str)


def test_config_drawer():
    assert isinstance(Config.__drawer__(), bool)


def test_config_navigation():
    assert isinstance(Config.__navigation__(), dict)
