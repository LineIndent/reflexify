import reflex as rx
from app.states.drawerState import DrawerState
from app.states.headerState import HeaderState
from app.helpers.app_config import Config
from app.helpers.nav_helpers import NavHelper
from app.helpers.css_helpers import CSSHelper


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
                        style=CSSHelper.__drawer_heading_css__(),
                    ),
                    rx.hstack(
                        self.repo_data,
                        style=CSSHelper.__drawer_repo_css__(),
                    ),
                    rx.drawer_body(self.nav_panel),
                    rx.drawer_footer(
                        rx.button("Close", on_click=DrawerState.left),
                    ),
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
        style=CSSHelper.__drawer_router_css__(),
        on_click=[DrawerState.left, rx.redirect(data[1])],
    )
