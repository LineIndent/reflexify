import reflex as rx
from app.core.repository import RepositoryData
from app.states.drawerState import DrawerState
from app.states.headerState import HeaderState


class RxHeader:
    def __init__(self, config: dict):
        self.config = config
        self.get_repository = self.get_repository_data()
        self.theme_toggle = rx.tooltip(
            rx.color_mode_button(
                rx.color_mode_icon(), color_scheme="None", color="white"
            ),
            label="Switch theme mode",
        )
        self.rx_header = rx.hstack(
            style=rx_header_style_sheet(
                self.config.get("theme", "").get("primary", ""),
            ),
            on_mouse_enter=HeaderState.header_expand,
            on_mouse_leave=HeaderState.header_retract,
        )

        self.site_name = rx.heading(
            self.config.get("site_name", "Site Name"),
            style=site_name_style,
        )

        self.rx_header_desktop = rx.desktop_only(
            rx.hstack(
                self.site_name,
                rx.spacer(),
                self.theme_toggle,
                self.get_repository,
            ),
            self.get_navigation_rail(),
            width="100%",
            style=header_desktop_style,
        )

        self.rx_header_mobile = rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.button(
                        rx.icon(
                            tag="hamburger",
                            font_size="xl",
                            cursor="pointer",
                            color="white",
                        ),
                        on_click=DrawerState.left,
                        color_scheme="None",
                    ),
                    self.site_name,
                    spacing="1.5rem",
                ),
                rx.spacer(),
                self.theme_toggle,
            ),
            width="100%",
            style=header_mobile_style,
        )

        self.rx_header_components = [
            self.rx_header_desktop,
            self.rx_header_mobile,
        ]

    def get_navigation_rail(self):
        rail = rx.hstack(
            rx.foreach(
                HeaderState.nav,
                router,
            ),
            width="100%",
            height=HeaderState.nav_height,
            spacing="1.5rem",
            align_items="end",
            opacity=HeaderState.onOpacity,
            transition="opacity 500ms ease 500ms",
        )

        return rail

    def get_repository_data(self):
        data = RepositoryData(self.config)
        return data.build()

    def build(self):
        self.rx_header.children = self.rx_header_components
        return self.rx_header


def router(data: list[str]):
    return rx.link(
        rx.text(data[0], size=10, font_weight="400", color="white"),
        href=data[1],
        _hover={"text_decoration": "None", "color": "#ffffff"},
        transition="opacity 500ms ease 200ms",
    )


def rx_header_style_sheet(bgcolor: str):
    return {
        "width": "100%",
        "height": HeaderState.isHovered,
        "position": "sticky",
        "bg": bgcolor,
        "box_shadow": "0 3px 6px 0 rgba(0, 0, 0, 0.5)",
        "transition": "height 350ms ease",
        "top": "0",
    }


site_name_style = {
    "font_size": ["100%", "115%", "130%", "135%", "150%"],
    "color": "white",
    "transition": "all 550ms ease",
}

header_desktop_style = {
    "padding_left": ["", "", "", "4rem", "10rem"],
    "padding_right": ["", "", "", "4rem", "10rem"],
    "transition": "all 550ms ease",
}

header_mobile_style = {
    "padding_left": ["1rem", "1rem", "1rem", "", ""],
    "padding_right": ["1rem", "1rem", "1rem", "", ""],
    "transition": "all 550ms ease",
}
