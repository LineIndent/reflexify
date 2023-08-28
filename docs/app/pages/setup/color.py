from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx

intro = """
The way **Reflexify** is setup makes changing theme properties, such as colors, very easiy and user-friendly. You can configure the **theme** properties by changing the values of the **theme** key in `config.py`.
"""

theme = """
Reflexify supports two color schemes: a light mode and a dark mode. The color scheme can be set by triggering the toggle button below, also located in the header section above.
"""

primary = """
The primary color is used for the header, the sidebar, and several other components. In order to change the primary color, set the following value in `config.py` to a color supported by **Reflex**:
"""

config_1 = """{
    "theme": {
        "primary": "black",
    }
}"""

secondary = """
The secondary color is used for events such as link and selected words highlights. In order to change the secondary color, set the following value in `config.py` to a color supported by **Reflex**:
"""

config_2 = """{
    "theme": {
        "secondary": "teal",
    }
}"""


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Setup"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/setup/color"

    # Left navigation panel: automated based on config navigation order
    def __left_navigation__(self):
        nav: list = NavHelper.__get_left_navigation__(self.__title__())
        return NavHelper.__set_left_navigation__(nav)

    # Right navigation panel: TBD
    def __right__navigation__(self):
        return []

    # Mobile navigation drop down
    def __mobile_navigation__(self):
        return NavHelper.__get_left_navigation__(self.__title__())

    # Main content area: takes in rx.Componenets and passes them to base file
    def __components__(self):
        stack: rx.Componenet = rx.hstack(
            rx.script(
                src="/index.js",
            ),
        )
        colors: list[str] = [
            "black",
            "teal",
            "blue",
            "yellow",
            "orange",
            "indigo",
            "cyan",
            "purple",
        ]

        for color in colors:
            stack.children.append(
                rx.container(
                    color,
                    w="64px",
                    h="64px",
                    bg=color,
                    on_click=rx.client_side(f"setHeaderColor('{color}')"),
                ),
            )

        return [
            rf.Title("Changing App Colors"),
            rf.Header("Configuration"),
            rx.markdown(intro),
            rf.SubHeader("Theme Mode"),
            rx.markdown(theme),
            rx.color_mode_button(rx.color_mode_icon(), width="100%"),
            rf.SubHeader("Primary color"),
            rx.markdown(primary),
            rx.box(
                rx.code_block(
                    config_1,
                    language="python",
                    theme="dark",
                    width="100%",
                ),
                width="100%",
            ),
            rf.SubHeader("Secondary color: TBD"),
            rx.markdown(secondary),
            rx.box(
                rx.code_block(
                    config_2,
                    language="python",
                    theme="dark",
                    width="100%",
                ),
                width="100%",
            ),
            stack,
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
