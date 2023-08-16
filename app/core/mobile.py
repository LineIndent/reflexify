import reflex as rx


class RxMobileNav(rx.Accordion):
    def __init__(
        self, components: any, allow_multiple=True, width="100%", padding="1rem 2rem"
    ):
        super().__init__(allow_multiple=allow_multiple, width=width, padding=padding)

        self.components = components

        self.accordian_item = rx.accordion_item(
            rx.accordion_button(
                rx.heading("Navigation", size="xs"),
                rx.spacer(),
                rx.accordion_icon(),
                padding="1rem 0.5rem",
            )
        )

        for title, route in self.components:
            self.accordian_item.children.append(
                rx.accordion_panel(
                    rx.link(rx.text(title), href=route),
                ),
            )

        self.children.append(self.accordian_item)
