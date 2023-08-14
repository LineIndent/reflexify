import reflex as rx


class RxLeft(rx.Vstack):
    def __init__(self, components: rx.Component, style: dict):
        super().__init__(children=[components], style=style)
