from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx


_static_tree = """_static/
│
├── _next/
│   └── ...
│
├── home/
│   └── start.html
│
├── setup/
│   ├── color.html
│   └── setup.html
│
├── 404.html
├── favicon.ico
└── index.html
"""


def return_code_block(string: str):
    return rx.box(
        rx.code_block(
            string,
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
        return "/home/create"

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
            rf.Title("Creating your first application"),
            rf.Header("Exporting Site"),
            rx.markdown(
                "After putting on the finishing touches to your web application, we can look at creating the site itself. We'll be using **Reflex's** [documentation](https://reflex.dev/docs/hosting/self-hosting/) for the first part, i.e., exporting the application. To export the web application, run the following commands: "
            ),
            rx.markdown("Inside the root directory, run: "),
            return_code_block("$ reflex export --no-zip"),
            rx.markdown(
                "If the build is successful, you should be able to see changes to  your ```.web``` directory. Move into the ```.web``` directory and locate a folder called ```_static``` :"
            ),
            return_code_block("$ cd .web"),
            rx.markdown(
                "Inside the ```.web``` folder, you'll see a buch of files, mainly ```.json``` and other HTML/JS files. What we're intrested in is the ```_static``` directory, so move into:"
            ),
            return_code_block("$ cd _static"),
            rx.markdown(
                "Once inside the ```_static``` directory, you'll find all your web application files and folders accordingly. For example, a web application with two folders, ```home``` and ```setup```, will have the following file structure: "
            ),
            return_code_block(_static_tree),
            rx.markdown(
                "If the export was successful, you now have your web application compiled and ready to be hosted online as a static website. To see how we can deploy the application, head over to the publish section to see how."
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
