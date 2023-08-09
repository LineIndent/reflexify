from app.core.header import RxHeader


import reflex as rx


class RxBasePage:
    def __init__(self, config: dict, components: list):
        self.config = config
        self.components = components

        self.rx_main_stack = rx.vstack(
            width="100%",
            min_height="200vh",
        )

        self.rx_header = RxHeader(self.config).build()
        self.rx_base_components = [
            self.rx_header,
        ]

    def build(self):
        self.rx_main_stack.children = self.rx_base_components

        return self.rx_main_stack
