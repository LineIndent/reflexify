import reflex as rx


class RxMiddle(rx.Vstack):
    def __init__(self, components: list, style: dict):
        super().__init__(style=style)
        self.components = components
        self.children = self.components
