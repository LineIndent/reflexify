from app.core.base import RxBasePage
import reflex as rx


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Error404"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/page_error_404"

    # Left navigation panel: automated based on config navigation order
    def __left_navigation__(self):
        return []

    # Right navigation panel: TBD
    def __right__navigation__(self):
        return []

    # Mobile navigation drop down
    def __mobile_navigation__(self):
        return []

    # Main content area: takes in rx.Componenets and passes them to base file
    def __components__(self):
        return [
            rx.box(
                rx.heading("Error 404", size="2xl", padding_bottom="1.5rem"),
                rx.heading("The page you are looking for does not exist!", size="md"),
                padding_left=["1rem", "1rem", "1rem", "4rem", "9rem"],
                transition="all 550ms ease",
            )
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
