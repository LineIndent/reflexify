from app.core.header import RxHeader
import reflex as rx
import pytest


@pytest.fixture
def header():
    return RxHeader().build()


def test_header_is_reflex_component(header):
    assert isinstance(header, rx.Component)
