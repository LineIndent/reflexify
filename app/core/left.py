import reflex as rx


class RxLeft(rx.Vstack):
    def __init__(self, left_navigation: list, style: dict):
        super().__init__(style=style)
        self.left_navigation = left_navigation
        self.children = self.left_navigation
