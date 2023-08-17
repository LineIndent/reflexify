import reflex as rx


class RxRight(rx.Vstack):
    def __init__(self, components: list[list[str]], style: dict):
        super().__init__(style=style)
        self.components = components
        self.children = [
            rx.link(
                rx.text(title),
                href=route,
                _hover={"text_decoration": "None"},
            )
            for title, route in self.components
        ]
