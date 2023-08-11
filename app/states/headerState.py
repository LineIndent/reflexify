from .mainState import MainState
from app.config import app_configuration

config: dict = app_configuration


def get_navigation_titles() -> list:
    navigation = [
        name.capitalize()
        for name in list(
            config.get("navigation").keys(),
        )
    ]

    return navigation


def get_navigation_paths(
    data: dict = config.get("navigation"),
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


def get_modified_navigation_list(
    titles: callable = get_navigation_titles(),
    paths: callable = get_navigation_paths(),
):
    return [[title, path] for title, path in zip(titles, paths)]


class HeaderState(MainState):
    default: list[str] = ["45px", "45px", "45px", "65px", "65px"]
    expanded: list[str] = ["45px", "45px", "45px", "100px", "100px"]
    isHovered: list[str] = default

    nav_height: str = "0px"
    onOpacity: str = "0"

    withNav: list[list[str]] = get_modified_navigation_list()
    nav: list[list[str]] = []

    def header_expand(self):
        if self.isHovered == self.default:
            self.isHovered = self.expanded
            self.nav_height = "35px"
            self.nav = self.withNav
            self.onOpacity = "1"

    def header_retract(self):
        if self.isHovered == self.expanded:
            self.onOpacity = "0"
            self.nav = []
            self.nav_height = "0px"
            self.isHovered = self.default
