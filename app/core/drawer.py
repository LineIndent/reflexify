import reflex as rx
from app.states.drawerState import DrawerState
from app.states.headerState import HeaderState
from app.helpers.app_config import Config
from app.helpers.nav_helpers import NavHelper


class RxDrawer:
    def __init__(self):
        self.repo_data = NavHelper.__get_repository__()
        self.nav_panel = rx.vstack(
            rx.foreach(HeaderState.withNav, router),
            spacing="1.25rem",
            align_items="start",
        )

        self.rx_drawer = rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.hstack(
                        rx.heading(Config.__site_name__(), size="lg"),
                        style=drawer_css["heading"],
                    ),
                    rx.hstack(self.repo_data, style=drawer_css["repo"]),
                    rx.drawer_body(self.nav_panel),
                    rx.drawer_footer(rx.button("Close", on_click=DrawerState.left)),
                ),
            ),
            is_open=DrawerState.show_left,
            placement="left",
        )

    def build(self):
        return self.rx_drawer


def router(data: list[str]):
    return rx.hstack(
        NavHelper.__get_nav_link__(
            title=data[0],
            route_to=data[1],
            size=15,
            color=None,
        ),
        rx.spacer(),
        rx.icon(
            tag="arrow_forward",
        ),
        style=drawer_css["router"],
        on_click=[DrawerState.left, rx.redirect(data[1])],
    )


drawer_css: dict = {
    "heading": {
        "width": "100%",
        "height": "100px",
        "align_items": "end",
        "bg": "teal",
        "padding_left": "1rem",
        "padding_bottom": "1rem",
        "transition": "all 550ms ease",
    },
    "repo": {
        "width": "100%",
        "height": "45px",
        "bg": "teal",
        "padding_left": "1rem",
        "transition": "all 550ms ease",
    },
    "router": {
        "align_items": "center",
        "width": "100%",
        "cursor": "pointer",
        "opacity": "0.8",
        "_hover": {"opacity": "1"},
    },
}
