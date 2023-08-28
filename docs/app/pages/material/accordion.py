from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
from app.styles._markdown import markdown_css
import app.material as rf
import reflex as rx


intro = """`Accordions` are dynamic user interface elements often used in web and app design to present content in a space-efficient manner. Comprising vertically stacked panels, accordions enable users to expand sections of interest while collapsing others, promoting an organized and uncluttered display. By clicking on a section's header, users can reveal underlying information, making accordions particularly effective for presenting FAQs, navigation menus, or categorized content.

"""

accord_code = """from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import reflex as rx
import app.material as rf

class RxPage:
    ...

    def __components__(self):
        return [
            rf.Admonition(
                "info",
                "Info",
                [
                    rx.accordion_panel("Insert text here...")
                ],
            ).build(),
        ]

    def build(self):
        ...
"""


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Material"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/material/accordion"

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
        accordion: list = [
            # add your components below #
            rf.Title("Accordion setup"),
            rx.box(rx.markdown(intro, custom_styles=markdown_css), padding="2rem 0rem"),
            rx.heading("Basic accordion useage", size="lg"),
            rx.box(
                rx.markdown(
                    "Implementing an accordion is fairly straightforward. Simply pass in the type of accordian, a title, and a list of accordion, if needed, and that will generate a custom accordion for you.",
                    custom_styles=markdown_css,
                ),
                padding="1rem 0rem",
            ),
            rx.box(
                rx.code_block(
                    accord_code,
                    language="python",
                    theme="dark",
                    width="100%",
                    can_copy=True,
                    show_line_numbers=True,
                ),
                width="100%",
            ),
            rf.SubHeader("Supported types"),
            rx.box(
                rx.markdown(
                    "There are several supported accordions, each with a unique icon. Moreover, you can pass in a title and more items inside. Here are the available accordions:",
                    custom_styles=markdown_css,
                ),
                padding="0.75rem 0rem",
            ),
        ]

        exple: list = [
            ["info", "Information"],
            ["warning_two", "Warning"],
            ["close", "Failure"],
            ["calendar", "Note"],
            ["question", "Question"],
            ["check", "Success"],
        ]

        for icon, title in exple:
            accordion.append(
                rx.vstack(
                    rx.markdown(f"`{icon}`"),
                    rf.Admonition(
                        icon,
                        title,
                        [
                            rx.accordion_panel(
                                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.",
                            )
                        ],
                    ).build(),
                    padding="1rem 0rem",
                    width="100%",
                    spacing="1rem",
                    align_items="start",
                ),
            )

        return accordion

    # Build method: creates a new instance for the page above
    def build(self):
        page = RxBasePage(
            self.__components__(),
            self.__left_navigation__(),
            self.__right__navigation__(),
            self.__mobile_navigation__(),
        )
        return page.build()
