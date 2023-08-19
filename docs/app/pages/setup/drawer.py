from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx


drawer = """{
    "drawer": True
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
        return "/setup/drawer"

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
            rf.Title("Setting up drawer menu"),
            rf.Header("Configuring drawer"),
            rx.markdown(
                "The drawer is a side menu that is prsent when the screen breaks after a certain point, typically at screen widths for tablets and mobile devices. The drawer contains the main header navigation. You can disable the drawer by setting it's key value in ```config.py``` to ```True```: "
            ),
            return_code_block(drawer),
            rx.box(
                rx.hstack(
                    rx.icon(tag="warning", color="orange"),
                    rx.heading("Static sites with side menus", size="sm"),
                    spacing="2rem",
                    border="0.1rem solid orange",
                    border_radius="6px",
                    width="100%",
                    padding="1rem 1rem",
                    bg="rgba(246, 139, 23, 0.54)",
                ),
                width="100%",
                padding="1rem 0rem",
            ),
            rx.markdown(
                "Because we're focusing mainly on static sites, any compoenent that needs to send a event to Reflex will not work. Therefore the click event on the icon to trigger the drawer will not work when deploying the site statically. As a result, the drawer is disabled by default and should be kept that away unless your app is deployed with a back end."
            ),
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
