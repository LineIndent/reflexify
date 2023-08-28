# import the CSSHelper class to easily get application stylesheet
from app.helpers.css_helpers import CSSHelper
from app.helpers.app_config import Config

# import the core componenets of the web application
from app.core.header import RxHeader
from app.core.left import RxLeft
from app.core.right import RxRight
from app.core.middle import RxMiddle
from app.core.footer import RxFooter
from app.core.drawer import RxDrawer
from app.core.mobile import RxMobileNav

# import the Reflex library
import reflex as rx


class RxBasePage:
    def __init__(
        self,
        components: list,
        left_navigation: rx.Component,
        right_navigation: list,
        mobile_navigation: list,
        remove_drawer: bool = Config.__drawer__(),
    ):
        self.components = components
        self.left_navigation = left_navigation
        self.right_navigation = right_navigation
        self.mobile_navigation = mobile_navigation
        self.remove_drawer = remove_drawer

        self.rx_main_stack = rx.vstack(style=CSSHelper.__base_css__())

        self.rx_header = RxHeader().build()

        nav = self.left_navigation
        self.rx_left = (
            RxLeft(
                nav,
                CSSHelper.__left_css__(),
            )
            if nav
            else rx.vstack()
        )

        self.rx_mobile_nav = RxMobileNav(self.mobile_navigation) if nav else []

        self.rx_right = RxRight(
            self.right_navigation,
            CSSHelper.__right_css__(),
        )

        self.rx_middle = RxMiddle(
            self.components,
            CSSHelper.__middle_css__(),
        )

        self.rx_footer = RxFooter(
            CSSHelper.__footer_style_css__(),
            CSSHelper.__footer_socials_css__(),
        ).build()

        self.rx_drawer = RxDrawer().build()

        self.rx_base_components = (
            [
                self.set_desktop_layout(),
                self.set_mobile_tablet_layout(),
            ]
            if self.remove_drawer
            else [
                self.rx_drawer,
                self.set_desktop_layout(),
                self.set_mobile_tablet_layout(),
            ]
        )

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
            self.rx_mobile_nav,
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
