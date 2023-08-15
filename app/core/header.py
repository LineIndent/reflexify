import reflex as rx
from app.states.drawerState import DrawerState
from app.states.headerState import HeaderState
from app.helpers.app_config import Config
from app.helpers.nav_helpers import NavHelper


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
            style=header_css["main"],
        )

        self.site_name = rx.tooltip(
            rx.link(
                rx.heading(
                    Config.__site_name__(),
                    style=header_css["site_name"],
                ),
                href="/",
                _hover={
                    "text_decoration": "None",
                },
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
            style=header_css["max_header"],
        )

        self.rx_header_mobile = rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.button(
                        rx.icon(tag="hamburger", style=header_css["icon"]),
                        on_click=DrawerState.left,
                        color_scheme="None",
                    ),
                    self.site_name,
                    spacing="1.5rem",
                ),
                rx.spacer(),
                self.theme_toggle,
            ),
            style=header_css["min_header"],
        )

        self.rx_header_components = [
            self.rx_header_desktop,
            self.rx_header_mobile,
        ]

    def get_navigation_rail(self):
        rail = rx.hstack(
            rx.foreach(HeaderState.withNav, router),
            style=header_css["navigation"],
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


header_css: dict = {
    "main": {
        "width": "100%",
        "height": "50px",
        "position": "sticky",
        "bg": Config.__theme_primary__(),
        "box_shadow": "0 3px 6px 0 rgba(0, 0, 0, 0.5)",
        "transition": "height 350ms ease",
        "top": "0",
        "z_index": "2",
    },
    "icon": {
        "font_size": "xl",
        "cursor": "pointer",
        "color": "white",
    },
    "navigation": {
        "align_items": "end",
        "transition": "opacity 500ms ease 500ms",
    },
    "link_text": {
        "size": "s",
        "padding_top": "0.3rem",
        "color": "white",
        "font_weight": "semibold",
    },
    "site_name": {
        "font_size": ["100%", "115%", "130%", "135%", "150%"],
        "color": "white",
        "transition": "all 550ms ease",
        "opacity": "1",
        "_hover": {"opacity": "0.85"},
        "padding_right": "3.5rem",
    },
    "max_header": {
        "width": "100%",
        "padding_left": ["", "", "", "4rem", "10rem"],
        "padding_right": ["", "", "", "4rem", "10rem"],
        "transition": "all 550ms ease",
    },
    "min_header": {
        "width": "100%",
        "padding_left": ["1rem", "1rem", "1rem", "", ""],
        "padding_right": ["1rem", "1rem", "1rem", "", ""],
        "transition": "all 550ms ease",
    },
}
