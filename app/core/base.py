from app.core.header import RxHeader

from app.core.left import RxLeft
from app.core.right import RxRight
from app.core.middle import RxMiddle
from app.core.footer import RxFooter
from app.core.drawer import RxDrawer

from app.styles.middle_style import rx_middle_css

from app.styles.left_style import rx_left_css
from app.styles.right_style import rx_right_css
from app.styles.base_style import rx_base_css
from app.styles.footer_style import rx_footer_css, rx_footer_socials_css


import reflex as rx


class RxBasePage:
    def __init__(
        self,
        components: list,
        left_navigation: rx.Component,
        right_navigation: list,
    ):
        self.components = components
        self.left_navigation = left_navigation
        self.right_navigation = right_navigation

        self.rx_main_stack = rx.vstack(style=rx_base_css)

        self.rx_header = RxHeader().build()

        nav = self.left_navigation
        self.rx_left = RxLeft(nav, rx_left_css) if nav else rx.vstack()
        self.rx_right = RxRight(self.right_navigation, rx_right_css)
        self.rx_middle = RxMiddle(self.components, rx_middle_css)
        self.rx_footer = RxFooter(rx_footer_css, rx_footer_socials_css).build()
        self.rx_drawer = RxDrawer().build()

        self.rx_base_components = [
            self.rx_drawer,
            self.set_desktop_layout(),
            self.set_mobile_tablet_layout(),
        ]

        self.children = self.rx_base_components

    def set_desktop_layout(self):
        return rx.desktop_only(
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
        )

    def set_mobile_tablet_layout(self):
        return rx.mobile_and_tablet(
            self.rx_header,
            rx.hstack(
                self.rx_middle,
                width="100%",
                align_items="start",
            ),
            self.rx_footer,
            width="100%",
        )

    def build(self):
        self.rx_main_stack.children = self.rx_base_components

        return self.rx_main_stack
