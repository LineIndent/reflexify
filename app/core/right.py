import reflex as rx


class RxRight(rx.Vstack):
    def __init__(self, right_navigation: list, style: dict):
        super().__init__(children=right_navigation, style=style)
