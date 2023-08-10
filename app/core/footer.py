import reflex as rx


class RxFooter:
    def __init__(self, config: dict):
        self.config = config

        self.rx_footer = rx.hstack(
            style=rx_footer_style_sheet("#15171b"),
        )

        self.attribution = rx.vstack(
            rx.text(self.config.get("copy_right", "")),
            rx.text(self.config.get("attribute", "")),
            style=attribution_style,
        )

        self.socials = self.get_user_socials()

        self.rx_footer_desktop = rx.desktop_only(
            rx.hstack(
                self.attribution,
                rx.spacer(),
                self.socials,
            ),
            width="100%",
            style=header_desktop_style,
        )

        self.rx_footer_mobile = rx.mobile_and_tablet(
            rx.hstack(
                self.attribution,
                rx.spacer(),
                # self.socials,
            ),
            width="100%",
            style=footer_mobile_style,
        )

        self.rx_footer_components = [
            self.rx_footer_desktop,
            self.rx_footer_mobile,
        ]

    def get_user_socials(self):
        stack = rx.hstack(spacing="2rem")
        if "socials" in self.config:
            for name, link in self.config.get("socials").items():
                if link:
                    stack.children.append(
                        rx.html(
                            socials_map.get(name),
                            on_click=rx.redirect(link),
                            cursor="pointer",
                        )
                    )

        return stack

    def build(self):
        self.rx_footer.children = self.rx_footer_components
        return self.rx_footer


def rx_footer_style_sheet(bgcolor: str):
    return {
        "width": "100%",
        "height": ["105px", "75px", "65px", "65px", "65px"],
        "position": "sticky",
        "bg": bgcolor,
        "transition": "height 350ms ease",
        "top": "0",
        "overflow": "hidden",
    }


attribution_style = {
    "font_size": "80%",
    "color": "white",
    "transition": "all 550ms ease",
    "align_items": "start",
}

header_desktop_style = {
    "padding_left": ["", "", "", "4rem", "10rem"],
    "padding_right": ["", "", "", "4rem", "10rem"],
    "transition": "all 550ms ease",
}

footer_mobile_style = {
    "padding_left": ["1rem", "1rem", "1rem", "", ""],
    "padding_right": ["1rem", "1rem", "1rem", "", ""],
    "transition": "all 550ms ease",
}

socials_map = {
    "github": "<img width='20' height='20' src='https://img.icons8.com/material-outlined/24/github.png' style='filter: brightness(0) invert(1)';/>",
    "twitter": "<img width='20' height='20' src='https://img.icons8.com/ios-filled/24/twitter.png' style='filter: brightness(0) invert(1)';/>",
    "youtube": "<img width='20' height='20' src='https://img.icons8.com/ios-filled/24/youtube.png' style='filter: brightness(0) invert(1)';/>",
    "mastodon": "<img width='20' height='20' src='https://img.icons8.com/windows/24/mastodon.png' style='filter: brightness(0) invert(1)';/>",
    "discord": "<img width='20' height='20' src='https://img.icons8.com/ios-filled/24/discord.png' style='filter: brightness(0) invert(1)';/>",
}
