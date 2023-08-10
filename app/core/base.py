from app.core.header import RxHeader
from app.core.left import RxLeft
from app.core.right import RxRight
from app.core.middle import RxMiddle
from app.core.footer import RxFooter

import reflex as rx

rx_base_page_style_sheet: dict = {
    "width": "100%",
    "min_height": "100vh",
    "spacing": "0rem",
}


class RxBasePage:
    def __init__(self, config: dict, components: list):
        self.config = config
        self.components = components

        self.rx_main_stack = rx.vstack(style=rx_base_page_style_sheet)

        self.rx_header = RxHeader(self.config).build()
        self.rx_left = RxLeft()
        self.rx_right = RxRight()
        self.rx_middle = RxMiddle()
        self.rx_footer = RxFooter(self.config).build()

        self.rx_base_components = [
            rx.desktop_only(
                self.rx_header,
                rx.hstack(
                    self.rx_left,
                    self.rx_middle,
                    self.rx_right,
                    width="100%",
                    align_items="start",
                ),
                self.rx_footer,
                width="100%",
            ),
            rx.mobile_and_tablet(
                self.rx_header,
                rx.hstack(
                    self.rx_middle,
                    width="100%",
                    align_items="start",
                ),
                self.rx_footer,
                width="100%",
            ),
        ]

        self.children = self.rx_base_components

    def build(self):
        self.rx_main_stack.children = self.rx_base_components

        return self.rx_main_stack
