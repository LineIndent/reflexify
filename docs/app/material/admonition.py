import reflex as rx
from app.styles._admonition import admonition_css

# tags: info, not_allowed, warning, warning_two, calendar

css: dict = admonition_css


class Admonition:
    def __init__(
        self,
        __type: str,
        __title: str,
        __components: list = [],
    ):
        self.__type = __type
        self.__title = __title
        self.__components = __components

        self.admonition = rx.accordion(
            rx.accordion_item(
                rx.accordion_button(
                    rx.icon(
                        tag=self.__type,
                        style=css.get(self.__type, "").get("icon", ""),
                    ),
                    rx.heading(self.__title, size="sm", padding_left="0.75rem"),
                    rx.spacer(),
                    rx.accordion_icon(),
                    style=css.get(self.__type, "").get("header", ""),
                    margin="0",
                    _hover={"opacity": "1"},
                ),
                padding="0",
                margin="0",
                overflow="hidden",
                border="0px solid transparent",
            ),
            width="100%",
            allow_multiple=True,
            border_radius="6px",
            padding="0",
            margin="0",
            overflow="hidden",
            style=css.get(self.__type, "").get("body", ""),
        )

    def build(self):
        for item in self.__components:
            self.admonition.children[0].children.append(item)

        return self.admonition
