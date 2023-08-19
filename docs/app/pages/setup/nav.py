from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx

nav_config = """"navigation": {
        "home": {
            "getting started": "start.py",
            "quick start": "run.py",
            "creating your site": "create.py",
            "publishing your site": "publish.py",
        },
        "setup": {
            "setup": "setup.py",
            "setting up navigation": "nav.py",
            "setting up drawer": "drawer.py",
            "changing the colors": "color.py",
            "changing the fonts": "font.py",
            "adding a git repository": "git.py",
            "adding social media": "socials.py",
        },
        "material": {},
    },
"""

path_ex = """"home": {
    "getting started": "start.py",
},
"""

path_ex_2 = """/home/start"""

right = """# Right navigation panel: manually add your page-specific TOC.
def __right__navigation__(self):
    return []
"""

right_2 = """["Example", "/home/start#example"]"""


right_3 = """# Right navigation panel: manually add your page-specific TOC.
def __right__navigation__(self):
    return [
        ["Example", "/home/start#example"]
    ]

# Main content area: takes in rx.Componenets and passes them to base file
def __components__(self):
    return [
        rf.SubHeader("Example", id="example"),
    ]
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
        return "/setup/nav"

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
            rf.Title("Setting up site navigation"),
            rf.Header("Config.py file"),
            rx.markdown(
                "To understand how navigation works in **Reflexify**, let's take a look at this site's navigation below. A few important notes on the navigation logic for this library. The outter keys, ```home```, ```setup```, etc. correspond to the navigation bar at the top. The inner keys, these correspond to the ```left panel``` navigation rail. Therefore the keys themeselves are the titles that re displayed on screen. Finally, the values of the inner keys are the file names and file paths, as described below."
            ),
            return_code_block(nav_config),
            rf.Header("Navigation paths and routing"),
            rx.markdown(
                "File paths are automatically created everytime the ```config.py``` file is changes for the navigation key. In brief, the file path, meaning the page route, corresponds to a string starting from the outter key and ending in the file name (without the .py exxtension). Here's an example: "
            ),
            rx.markdown("The following navigation key-value pairs: "),
            return_code_block(path_ex),
            rx.markdown("Corresponds to the following route path: "),
            return_code_block(path_ex_2),
            rx.markdown(
                "The route above, and any others taken from the config.py, will automatically be added into the application logic with each reload or startup. This makes generating routes fast, reliable, and easy for developers. "
            ),
            rf.Header("Right panel navigation"),
            rx.markdown(
                "**Reflexify** offers a third navigation system, the ```table of contents``` navigation. This is located on the right side and can be manually added. The table of contents function is to navigate to different sections within the same page. Let's see how to set this up. Every Reflexy generated page consists of a method called ```__right__navigation__```: "
            ),
            return_code_block(right),
            rx.markdown(
                "To utilize this method, you need to pass in a list that consists of two elements: a title and a special string that consists of the page route, a hash, and an ID: "
            ),
            return_code_block(right_2),
            rx.markdown(
                "The final setup should look something like this. Note that you need to pass in the ```id``` parameter, either to Reflexify's rf.SubHeading() or the usual Reflex component: "
            ),
            return_code_block(right_3),
            rx.markdown("Make sure the ```id``` matches the word after the  ```#```."),
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
