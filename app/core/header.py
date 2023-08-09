import reflex as rx

# from app.states.headerState import HeaderState


class RxHeader:
    def __init__(self, config: dict):
        self.config = config
        self.theme_toggle = rx.color_mode_button(rx.color_mode_icon())
        self.rx_header = rx.hstack(
            style=rx_header_style_sheet(
                self.config.get("theme", "").get("primary", ""),
            )
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
            ),
            width="100%",
            style=header_desktop_style,
        )

        self.rx_header_mobile = rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        tag="hamburger", font_size="xl", cursor="pointer", color="white"
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

    def build(self):
        self.rx_header.children = self.rx_header_components
        return self.rx_header


def rx_header_style_sheet(bgcolor: str):
    return {
        "width": "100%",
        "height": ["45px", "45px", "45px", "45px", "60px"],
        "position": "fixed",
        "bg": bgcolor,
        "box_shadow": "0 3px 6px 0 rgba(90, 116, 148, 0.2)",
        "transition": "height 350ms ease",
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
