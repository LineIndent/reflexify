from app.core.header import RxHeader
import reflex as rx
import pytest


@pytest.fixture
def build():
    return RxHeader().build()


@pytest.fixture
def header():
    return RxHeader()


def test_header_type(build, header):
    assert isinstance(build, rx.Component)
    assert isinstance(header.theme_toggle, rx.Tooltip)
    assert isinstance(header.rx_header, rx.Hstack)
    assert isinstance(header.site_name, rx.Link)


def test_header_background_color(header):
    header.rx_header.__dict__["style"]["bg"] = "orange"
    assert header.rx_header.__dict__["style"]["bg"] == "orange"
