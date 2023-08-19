from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx

repo = """"socials": {
    "github": "https://github.com/LineIndent/reflexify",
    "twitter": "https://twitter.com/getreflex",
    "youtube": "https://www.youtube.com/playlist?list=PLDHA4931gtc7wHBDGQOYlmcpZm7qyici7",
    "mastodon": "",
    "discord": "https://discord.com/invite/T5WSbC2YtQ",
}
"""


def return_code_block(string: str, copy: bool = False):
    return rx.box(
        rx.code_block(
            string,
            language="python",
            can_copy=copy,
            theme="dark",
            width="100%",
        ),
        width="100%",
        padding="1rem 0rem",
    )


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Setup"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/setup/socials"

    # Left navigation panel: automated based on config navigation order
    def __left_navigation__(self):
        nav: list = NavHelper.__get_left_navigation__(self.__title__())
        return NavHelper.__set_left_navigation__(nav)

    # Right navigation panel: manually add your page-specific TOC (table fo content) to navigate wwithin page
    def __right__navigation__(self):
        return []

    # Mobile navigation drop down
    def __mobile_navigation__(self):
        return NavHelper.__get_left_navigation__(self.__title__())

    # Main content area: takes in rx.Componenets and passes them to base file
    def __components__(self):
        return [
            # add your components below #
            rf.Title("Adding social media"),
            rf.Header("Config.py file"),
            rx.markdown(
                "To add social media to your static website, you can add/edit the following paramters in your ```config.py``` file: "
            ),
            return_code_block(repo),
            rx.markdown(
                "The corresponding social media icon will then appear and be displayed inside the site footer. The links to these external websites are functional even with a static website. "
            )
            # end your components above #
        ]

    # Build method: creates a new instance for the page above
    def build(self):
        page = RxBasePage(
            self.__components__(),
            self.__left_navigation__(),
            self.__right__navigation__(),
            self.__mobile_navigation__(),
        )
        return page.build()
