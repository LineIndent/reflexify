from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx

intro = """
Reflexify's base compoenents come pre-configured in order to provide rapid devleopment of web applications or Python documentation. However, a wide range of options for customizing your application are available. We'll go over the options and explain each one in this section.
"""

structure = """
As a developer, you have access to the base configurations of your application, and as such can access base attributes such as the app header, footer, and navigation. Below are the main file structure for **Reflexify**:
"""

purpose = """
Even though each above component of your application comes preconfigured, you can always go to the base configuration files and personalize them as needed. This gives developers the flexibility to make each application unique. 
"""

drop_items = [
    """│app/
├── core/
│   ├── __init__.py
│   ├── base.py
│   ├── drawer.py
│   ├── footer.py
│   ├── header.py
│   ├── left.py
│   ├── middle.py
│   ├── mobile.py
│   ├── repository.py
│   └── right.py
""",
    """│app/
├── helpers/
│   ├── app_config.py
│   ├── css_helpers.py
│   └── nav_helpers.py
""",
    """│app/
├── material/
│   ├── __init__.py
│   └── typography.py
│
""",
    """│app/
├── states/
│   ├── __init__.py
│   ├── drawerState.py
│   ├── headerState.py
│   ├── mainState.py

""",
    """│app/   
├── styles/
│   ├── _base.py
""",
]
drop_titles = ["Core", "Helpers", "Material", "States", "Styles"]

drop_list = rx.accordion(
    allow_multiple=True,
    width="100%",
    padding_top="1rem",
    padding_bottom="1rem",
)
for index, item in enumerate(drop_items):
    drop_list.children.append(
        rx.accordion_item(
            rx.accordion_button(
                rx.heading(drop_titles[index], size="md"),
                rx.spacer(),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
                rx.code_block(
                    item,
                    language="plaintext",
                    theme="dark",
                    width="100%",
                ),
            ),
            padding="0.25rem 0rem",
        ),
    )


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "Setup"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/setup/setup"

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
            rf.Title("Application File Setup"),
            rf.Header("Setup"),
            rx.markdown(intro),
            rf.SubHeader("Application structure"),
            rx.markdown(structure),
            drop_list,
            rx.markdown(purpose),
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
