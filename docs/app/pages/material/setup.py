from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import reflex as rx
from app.styles._markdown import markdown_css
import app.material as rf

intro = """A `material library` is a comprehensive collection of pre-designed and pre-engineered materials that serve as a valuable resource for designers, architects, engineers, and artists. It encompasses a diverse range of materials, each with specific properties, textures, colors, and performance characteristics. Material libraries provide a structured repository of options for use in various projects, enabling creators to efficiently select and apply suitable materials without the need for extensive research or testing. These libraries often include samples, specifications, and digital representations of materials, fostering creativity, standardization, and informed decision-making in design and construction processes.

"""


temp_with_import = """from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper

# Add the following import statement...
import app.material as rf
"""


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Material"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/material/setup"

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
            rf.Title("Material setup"),
            rx.box(
                rx.markdown(intro, custom_styles=markdown_css), padding="1.5rem 0rem"
            ),
            rx.heading("Importing material library", size="lg"),
            rx.markdown(
                "To import and use the material library, we need to import the module at the top first. Add the following import statment to your page: ",
                custom_styles=markdown_css,
            ),
            rx.box(
                rx.code_block(
                    temp_with_import,
                    theme="dark",
                    language="python",
                    width="100%",
                ),
                width="100%",
            ),
            rx.markdown(
                "Once you have the above module imported, you can start using the various material design library available. Check out the left panel for a list of available material design for `Reflex`",
                custom_styles=markdown_css,
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
