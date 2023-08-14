import reflex as rx


class FxMobileNavigation:
    def __init__(self, components: list, style: dict):
        self.style = style
        self.components = components

        self.main_stack = rx.vstack(style=self.style["main"])

        self.title = rx.hstack(
            rx.text(
                "Title",
                font_size="16px",
                weight="semibold",
                height="50px",
                padding_top="1rem",
            ),
            rx.spacer(),
            rx.text("O"),
            width="100%",
            align_items="center",
            bg="pink",
            padding="0rem 2rem",
        )

        self.main_stack.children = self.components
        self.main_stack.children.insert(0, self.title)

    def build(self):
        return self.main_stack
