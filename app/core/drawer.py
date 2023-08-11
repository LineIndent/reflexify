import reflex as rx
from app.states.drawerState import DrawerState
from app.core.repository import RepositoryData
from app.states.headerState import HeaderState


class RxDrawer:
    def __init__(self, config: dict):
        self.config = config
        self.get_repository = self.get_repository_data()
        self.nav_panel = rx.vstack(
            rx.foreach(
                HeaderState.withNav,
                router,
            ),
            spacing="1.25rem",
            align_items="start",
        )

        self.rx_drawer = rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.hstack(
                        rx.heading(self.config.get("site_name", ""), size="lg"),
                        width="100%",
                        height="100px",
                        align_items="end",
                        bg="teal",
                        padding_left="1rem",
                        padding_bottom="1rem",
                        transition="all 550ms ease",
                    ),
                    rx.hstack(
                        self.get_repository,
                        width="100%",
                        height="45px",
                        bg="teal",
                        padding_left="1rem",
                        transition="all 550ms ease",
                    ),
                    rx.drawer_body(
                        self.nav_panel,
                    ),
                    rx.drawer_footer(
                        rx.button("Close", on_click=DrawerState.left),
                    ),
                ),
            ),
            is_open=DrawerState.show_left,
            placement="left",
        )

    def get_repository_data(self):
        data = RepositoryData(self.config)
        return data.build()

    def build(self):
        return self.rx_drawer


def router(data: list[str]):
    return rx.hstack(
        rx.link(
            rx.text(
                data[0],
                size=12,
                font_weight="400",
                color="white",
            ),
            href=data[1],
            _hover={"text_decoration": "None", "color": "#ffffff"},
            padding="0.25rem 0rem",
        ),
        rx.spacer(),
        rx.icon(tag="arrow_forward"),
        align_items="center",
        width="100%",
        cursor="pointer",
        opacity="0.8",
        _hover={"opacity": "1"},
        on_click=[DrawerState.left, rx.redirect(data[1])],
    )
