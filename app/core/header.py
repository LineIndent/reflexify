import reflex as rx
from app.states.drawerState import DrawerState
from app.states.headerState import HeaderState
from app.helpers.app_config import Config
from app.helpers.nav_helpers import NavHelper
from app.helpers.css_helpers import CSSHelper


class RxHeader:
    def __init__(self):
        self.get_repository = NavHelper.__get_repository__()
        self.theme_toggle = rx.tooltip(
            rx.color_mode_button(
                rx.color_mode_icon(), color_scheme="None", color="white"
            ),
            label="Switch theme mode",
        )
        self.rx_header = rx.hstack(
            style=CSSHelper.__header_main_css__(),
        )

        self.site_name = rx.tooltip(
            rx.link(
                rx.heading(
                    Config.__site_name__(), style=CSSHelper.__header_site_name_css__()
                ),
                href="/",
                _hover={"text_decoration": "None"},
            ),
            label="Reflexify Template",
        )
        self.rx_header_desktop = rx.desktop_only(
            rx.hstack(
                self.site_name,
                self.get_navigation_rail(),
                rx.spacer(),
                self.theme_toggle,
                self.get_repository,
            ),
            style=CSSHelper.__header_max_header_css__(),
        )

        self.rx_header_mobile = rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.button(
                        rx.icon(tag="hamburger", style=CSSHelper.__header_icon_css__()),
                        on_click=DrawerState.left,
                        color_scheme="None",
                    ),
                    self.site_name,
                    spacing="1.5rem",
                ),
                rx.spacer(),
                self.theme_toggle,
            ),
            style=CSSHelper.__header_min_header_css__(),
        )

        self.rx_header_components = [
            self.rx_header_desktop,
            self.rx_header_mobile,
        ]

    def get_navigation_rail(self):
        rail = rx.hstack(
            rx.foreach(HeaderState.withNav, router),
            style=CSSHelper.__header_navigation_css__(),
            spacing="2rem",
        )

        return rail

    def build(self):
        self.rx_header.children = self.rx_header_components
        return self.rx_header


def router(data: list[str]):
    return rx.link(
        rx.heading(
            data[0],
            size="s",
            padding_top="0.3rem",
            color="white",
            font_weight="semibold",
        ),
        href=data[1],
        opacity="0.85",
        transition="opacity 600ms ease",
        _hover={
            "text_decoration": "None",
            "opacity": "1",
        },
    )
