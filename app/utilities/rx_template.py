from app.core.base import RxBasePage


class RxPage:
    def __init__(self, config: dict):
        self.config = config

    def __route__(self):
        return ""

    def __left__navigation__(self):
        return []

    def __right__navigation__(self):
        return []

    def __components__(self):
        return []

    def build(self):
        page = RxBasePage(
            self.config,
            self.__components__(),
            self.__left__navigation__(),
            self.__right__navigation__(),
        )
        return page.build()
