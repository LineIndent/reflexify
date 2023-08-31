from app.styles._button import button_css
import reflex as rx


class Button:
    def __init__(
        self,
        __title: str,
    ):
        self.__title = __title

        self.button = rx.button(
            rx.text(self.__title, font_size="14px", color="white"),
            style=button_css,
        )

    def build(self):
        return self.button
