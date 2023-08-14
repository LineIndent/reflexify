from app.core.base import RxBasePage
import reflex as rx


class RxPage:
    def __title__(self):
        return "Error404"

    def __route__(self):
        return "/page_error_404"

    def __right__navigation__(self):
        return []

    def __components__(self):
        return [
            rx.heading("Error 404", size="2xl"),
            rx.heading("The page you are looking for does not exist!", size="l"),
        ]

    def build(self):
        page = RxBasePage(
            self.__title__(),
            self.__components__(),
            self.__right__navigation__(),
        )
        return page.build()
