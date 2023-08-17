import reflex as rx
from app.helpers.app_config import Config


class RxFooter:
    def __init__(self, style: dict, socials: dict):
        self.style = style
        self.socials = socials

        self.rx_footer = rx.hstack(style=self.style)

        self.attribution = rx.vstack(
            rx.text(Config.__attribute__()),
            rx.text(Config.__copy_right__()),
            style=footer_css.get("attribute"),
        )

        self.socials = self.get_user_socials()

        self.rx_footer_desktop = rx.desktop_only(
            rx.hstack(self.attribution, rx.spacer(), self.socials),
            style=footer_css.get("max_footer"),
        )

        self.rx_footer_tablet = rx.tablet_only(
            rx.hstack(self.attribution, rx.spacer(), self.socials),
            style=footer_css.get("min_footer"),
        )

        self.rx_footer_mobile = rx.mobile_only(
            rx.hstack(
                rx.vstack(
                    self.attribution, self.socials, align_items="start", spacing="1rem"
                )
            ),
            style=footer_css.get("min_footer"),
        )

        self.rx_footer_components = [
            self.rx_footer_desktop,
            self.rx_footer_tablet,
            self.rx_footer_mobile,
        ]

    def get_user_socials(self):
        stack = rx.hstack(spacing="2rem")
        socials = Config.__all_social__()
        if socials:
            for name, url in socials.items():
                if url:
                    stack.children.append(
                        rx.link(
                            rx.html(
                                self.socials.get(name),
                                # on_click=rx.redirect(url),
                                cursor="pointer",
                            ),
                            href=url,
                            _hover={"text_decoration": "None"},
                        )
                    )

        return stack

    def build(self):
        self.rx_footer.children = self.rx_footer_components
        return self.rx_footer


footer_css: dict = {
    "attribute": {
        "font_size": "80%",
        "color": "white",
        "transition": "all 550ms ease",
        "align_items": "start",
    },
    "max_footer": {
        "width": "100%",
        "padding_left": ["", "", "", "4rem", "10rem"],
        "padding_right": ["", "", "", "4rem", "10rem"],
        "transition": "all 550ms ease",
    },
    "min_footer": {
        "width": "100%",
        "padding_left": ["2rem", "2rem", "2rem", "", ""],
        "padding_right": ["2rem", "2rem", "2rem", "", ""],
        "transition": "all 550ms ease",
    },
}
