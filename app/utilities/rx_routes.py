from app.config import app_configuration
import reflex as rx

config = app_configuration


def router(title: str, route_to: str):
    return rx.link(
        rx.text(title, size=10, font_weight="semibold"),
        href=route_to,
        _hover={
            "text_decoration": "None",
            "color": config.get("theme", "").get("secondary", ""),
            "transition": "all 550ms ease",
        },
    )
