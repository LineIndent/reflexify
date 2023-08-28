from app.core.repository import RepositoryData
from app.helpers.app_config import Config
import reflex as rx


class NavHelper:
    @staticmethod
    def __get_repository__():
        data = RepositoryData().build()
        return data

    @staticmethod
    def __get_navigation_titles__() -> list:
        navigation = (
            [
                name.capitalize()
                for name in list(
                    Config.__navigation__().keys(),
                )
            ]
            if Config.__navigation__()
            else []
        )

        return navigation

    @staticmethod
    def __get_navigation_paths__(
        data: dict = Config.__navigation__(),
        parent: str = "/",
        paths: list = [],
    ) -> list[tuple]:
        for key, value in data.items():
            if isinstance(value, str) and key == "home":
                paths.append("/")
            if isinstance(value, dict):
                for path in list(value.values()):
                    paths.append(f"{parent}{key}/{path.split('.py')[0]}")
                    break

        return paths

    @staticmethod
    def __get_nav_link__(
        title: str,
        route_to: str,
        size: str,
        color: str,
    ):
        style = nav_helper_css.copy()
        style["text"]["font_size"] = size
        style["text"]["color"] = color
        return rx.link(
            rx.text(title, style=style["text"]), href=route_to, style=style["link"]
        )

    @staticmethod
    def __get_left_navigation__(
        ref: str,
        data: dict = Config.__navigation__(),
    ):
        paths: list = []
        for key, value in data.items():
            if isinstance(value, dict) and key == ref.lower():
                for title, path in value.items():
                    paths.append(
                        [
                            title.capitalize(),
                            f"/{ref.lower()}/{path.split('.py')[0]}",
                        ]
                    )
        return paths

    @staticmethod
    def __set_left_navigation__(inc_paths: list) -> rx.Component:
        out_paths: list = []
        nav: rx.Component = rx.vstack(style=nav_helper_css["nav"])
        if inc_paths:
            for title, route in inc_paths:
                out_paths.append(
                    NavHelper.__get_nav_link__(
                        title=title.capitalize(),
                        route_to=route,
                        size=13,
                        color=None,
                    )
                )

        nav.children = out_paths
        return nav


nav_helper_css: dict = {
    "nav": {
        "align_items": "start",
    },
    "link": {
        "_hover": {"text_decoration": "None"},
        "padding": "0.25rem 0rem",
    },
    "text": {
        "font_size": "%s",
        "font_weight": "500",
        "color": "%s",
        "opacity": "0.85",
        "transition": "opacity 350ms ease",
        "_hover": {"opacity": "1"},
    },
}
