from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import reflex as rx


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Reflexify"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/"

    # Left navigation panel: automated based on config navigation order
    def __left_navigation__(self):
        nav: list = NavHelper.__get_left_navigation__(self.__title__())
        return NavHelper.__set_left_navigation__(nav)

    # Right navigation panel: TBD
    def __right__navigation__(self):
        return []

    # Mobile navigation drop down
    def __mobile_navigation__(self):
        return NavHelper.__get_left_navigation__(self.__title__())

    # Main content area: takes in rx.Componenets and passes them to base file
    def __components__(self):
        return [
            # add your components below #
            rx.heading("Welcome to Reflexify!", size="xl", padding_bottom="2rem"),
            rx.heading(
                "This is the library's documentation. Select a link above to get started.",
                size="sm",
            )
            # end your components above #
        ]

    # Build method: creates a new instance for the page above
    def build(self):
        page = RxBasePage(
            self.__components__(),
            self.__left_navigation__(),
            self.__right__navigation__(),
            self.__mobile_navigation__(),
        )
        return page.build()
