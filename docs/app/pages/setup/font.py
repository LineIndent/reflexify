from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx

intro = """
**Reflexify** makes it super easy to change the typface of your application by simply changing the value of your ```config.py``` file. Let's take a look at how we can do this.

"""

fonts = """
Reflexify supports fonts that are in turn supported by it's parent library, **Reflex**. So any fonts supported within Reflex can be used here as well.
"""

font_code = """{
    "theme": {
        "fonts": "Times New Roman",
    }
}"""

fonts_2 = """
If you prefer to keep the default system fonts, you can simply leave the value of the ```fonts``` key blank, and this will trigger a fall back to systems fonts.
"""
font_code_2 = """{
    "theme": {
        "fonts": "",
    }
}"""


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Setup"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/setup/font"

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
        return [
            rf.Title("Changing App Fonts"),
            rf.Header("Configuration"),
            rx.markdown(intro),
            rf.SubHeader("Fonts"),
            rx.markdown(fonts),
            rx.box(
                rx.code_block(
                    font_code,
                    language="python",
                    theme="dark",
                    width="100%",
                ),
                width="100%",
            ),
            rx.markdown(fonts_2),
            rx.box(
                rx.code_block(
                    font_code_2,
                    language="python",
                    theme="dark",
                    width="100%",
                ),
                width="100%",
            ),
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
