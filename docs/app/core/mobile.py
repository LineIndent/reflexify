from app.helpers.nav_helpers import NavHelper
import reflex as rx


class RxMobileNav(rx.Accordion):
    def __init__(
        self, components: any, allow_multiple=True, width="100%", padding="1rem 2rem"
    ):
        super().__init__(allow_multiple=allow_multiple, width=width, padding=padding)

        self.components = components

        self.bread_crumb = rx.breadcrumb(
            padding="1.25rem 0.5rem",
        )

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
                    rx.link(
                        rx.text(title),
                        href=route,
                        _hover={"text_decoration": "None"},
                    ),
                ),
            )

        main_navigation = [
            [title, route]
            for title, route in zip(
                NavHelper.__get_navigation_titles__(),
                NavHelper.__get_navigation_paths__(),
            )
        ]

        for title, route in main_navigation:
            self.bread_crumb.children.append(
                rx.breadcrumb_item(rx.link(rx.text(title), href=route))
            )

        self.children = (
            [self.bread_crumb, self.accordian_item]
            if self.components
            else [self.bread_crumb]
        )
