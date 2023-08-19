from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper

import app.material as rf
import reflex as rx

intro = """
 **Reflexify** is a Python web boilerplate project built with **[Reflex](https://reflex.dev)**. and designed to provide a solid foundation for building web applications with Python and Reflex. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools.
"""

installation = """
To use **Reflexify**, you need to have have the latest version of **Reflex** and **Python 3.5+** installed. If you don't have Reflex installed, installing Reflexify automatically installs it for you. You can install Reflexify using the following command:

"""

pip_install = """Currently you can get the **Reflexify** library by using the popular Python package manager `pip`. Ideally, you'll want to install this, as well as the main Reflexify library in a virtual environment. Open up a terminal and enter the following command:
"""

rf_command = """pip install reflexify"""

git_clone = """To clone the Reflexify repository from GitHub, open a terminal or command prompt and navigate to the directory where you want to store the cloned repository. Then, run the following command:"""

git_command = """git clone https://github.com/LineIndent/reflexify.git"""

git_conclusion = """This will download the repository to your local machine, and you can then start using the library."""


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Home"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/home/start"

    # Left navigation panel: automated based on config navigation order
    def __left_navigation__(self):
        nav: list = NavHelper.__get_left_navigation__(self.__title__())
        return NavHelper.__set_left_navigation__(nav)

    # Right navigation panel: TBD
    def __right__navigation__(self):
        return [
            ["Prerequisites", "/home/start#prereq"],
            ["PIP Package", "/home/start#pip"],
            ["GitHub Clone", "/home/start#git"],
        ]

    # Mobile navigation drop down
    def __mobile_navigation__(self):
        return NavHelper.__get_left_navigation__(self.__title__())

    # Main content area: takes in rx.Componenets and passes them to base file
    def __components__(self):
        return [
            rf.Title("Welcome to Reflexify!"),
            rf.Header("Getting started"),
            rx.markdown(intro),
            rx.spacer(),
            rf.Header("Installation guide"),
            rf.SubHeader("Prerequisites", id="prereq"),
            rx.markdown(installation),
            rf.SubHeader("Python PIP Package", id="pip"),
            rx.markdown(pip_install),
            rx.box(
                rx.code_block(
                    rf_command,
                    language="python",
                    can_copy=True,
                    theme="dark",
                    width="100%",
                ),
                width="100%",
                padding="1rem 0rem",
            ),
            rf.SubHeader("GitHub Clone", id="git"),
            rx.markdown(git_clone),
            rx.box(
                rx.code_block(
                    git_command,
                    language="python",
                    can_copy=True,
                    theme="dark",
                    width="100%",
                ),
                width="100%",
                padding="1rem 0rem",
            ),
            rx.markdown(
                git_conclusion,
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
