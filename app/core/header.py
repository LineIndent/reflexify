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
            on_mouse_enter=HeaderState.header_expand,
            on_mouse_leave=HeaderState.header_retract,
        )

        self.site_name = rx.heading(
            Config.__site_name__(),
            style=header_css["site_name"],
        )

        self.rx_header_desktop = rx.desktop_only(
            rx.hstack(
                self.site_name, rx.spacer(), self.theme_toggle, self.get_repository
            ),
            self.get_navigation_rail(),
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
            rx.foreach(HeaderState.nav, router), style=header_css["navigation"]
        )

        return rail

    def build(self):
        self.rx_header.children = self.rx_header_components
        return self.rx_header


def router(data: list[str]):
    return NavHelper.__get_nav_link__(
        title=data[0],
        route_to=data[1],
        size=15,
        color="white",
    )


header_css: dict = {
    "main": {
        "width": "100%",
        "height": HeaderState.isHovered,
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
        "width": "100%",
        "height": HeaderState.nav_height,
        "spacing": "2rem",
        "align_items": "end",
        "opacity": HeaderState.onOpacity,
        "transition": "opacity 500ms ease 500ms",
    },
    "site_name": {
        "font_size": ["100%", "115%", "130%", "135%", "150%"],
        "color": "white",
        "transition": "all 550ms ease",
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
