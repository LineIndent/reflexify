import reflex as rx
from app.states.drawerState import DrawerState
from app.core.repository import RepositoryData


class RxDrawer:
    def __init__(self, config: dict):
        self.config = config
        self.get_repository = self.get_repository_data()

        self.rx_drawer = rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.hstack(
                        rx.heading("Reflexify", size="lg"),
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
                    rx.drawer_body("Do you want to confirm example?"),
                    rx.drawer_footer(rx.button("Close", on_click=DrawerState.left)),
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
