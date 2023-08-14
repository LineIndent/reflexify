from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return ""

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return ""

    # Left navigation panel: automated based on config navigation order
    def __left_navigation__(self):
        nav: list = NavHelper.__get_left_navigation__(self.__title__())
        return NavHelper.__set_left_navigation__(nav)

    # Right navigation panel: TBD
    def __right__navigation__(self):
        return []

    # Main content area: takes in rx.Componenets and passes them to base file
    def __components__(self):
        return []

    # Build method: creates a new instance for the page above
    def build(self):
        page = RxBasePage(
            self.__components__(),
            self.__left_navigation__(),
            self.__right__navigation__(),
        )
        return page.build()
