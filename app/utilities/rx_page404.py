from app.core.base import RxBasePage
import reflex as rx


class RxPage:
    def __init__(self, config: dict):
        self.config = config

    def __route__(self):
        return "/index"

    def __left__navigation__(self):
        return []

    def __right__navigation__(self):
        return []

    def __components__(self):
        return [
            rx.heading("Error 404", size="2xl"),
            rx.heading("The page you are looking for does not exist!", size="l"),
        ]

    def build(self):
        page = RxBasePage(
            self.config,
            self.__components__(),
            self.__left__navigation__(),
            self.__right__navigation__(),
        )
        return page.build()
