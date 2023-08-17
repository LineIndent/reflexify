from .mainState import MainState
from app.helpers.nav_helpers import NavHelper


def get_modified_navigation_list(
    titles: callable = NavHelper.__get_navigation_titles__(),
    paths: callable = NavHelper.__get_navigation_paths__(),
):
    return [[title, path] for title, path in zip(titles, paths)]


class HeaderState(MainState):
    withNav: list[list[str]] = get_modified_navigation_list()
