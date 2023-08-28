from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper

import app.material as rf
import reflex as rx


one = rx.box(
    rx.code_block(
        "$ reflex init",
        language="python",
        can_copy=True,
        theme="dark",
        width="100%",
    ),
    width="100%",
    padding="1rem 0rem",
)


two = rx.box(
    rx.code_block(
        """$ rf-init""",
        language="python",
        can_copy=True,
        theme="dark",
        width="100%",
    ),
    width="100%",
    padding="1rem 0rem",
)

three = rx.box(
    rx.code_block(
        """$ python3 reflexify_scripts/build.py""",
        language="python",
        can_copy=True,
        theme="dark",
        width="100%",
    ),
    width="100%",
    padding="1rem 0rem",
)


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Home"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/home/run"

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
            rf.Title("Running your first application"),
            rf.Header("Quick Start"),
            rx.markdown(
                "After installing **Reflexify**, you can test if the library is working properly by going over the following steps in order."
            ),
            rx.markdown(
                "1. Inside the root directory, initiate the reflex application (as you would a normal Reflex app):"
            ),
            one,
            rx.markdown(
                "2. Once the Reflex application is created, run the following Reflexify command to setup the components:"
            ),
            two,
            rx.markdown(
                "If the package was installed correctly, a folder called app will be generated inside the root directory. Other directories and files will also be generated."
            ),
            rx.markdown(
                "3. Next, run the watch script by entering the following command:"
            ),
            three,
            rx.markdown(
                "This script will now monitor your ```config.py``` file inside the app directory. Specifically, it will watch for changes to your navigation and update the changes accordingly inside the ```pages``` directory."
            ),
            rx.spacer(),
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
