import reflex as rx


class RxRight(rx.Vstack):
    def __init__(self, right_navigation: list, style: dict):
        super().__init__(style=style)
        self.right_navigation = right_navigation
        self.children = self.right_navigation
