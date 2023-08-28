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
        return "/home/publish"

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
            rf.Title("Publishing your first application"),
            rf.Header("Hosting Your Site"),
            rx.hstack(
                rx.icon(tag="warning_two", color="red"),
                rx.heading("Hosting static site on Vercel", size="sm"),
                spacing="2rem",
                border="0.1rem solid red",
                border_radius="6px",
                width="100%",
                padding="1rem 1rem",
                bg="rgba(210, 9, 9, 0.39)",
            ),
            rx.box(
                rx.markdown(
                    "This guide uses **[Vercel](https://vercel.com/)** as the hosting provider. Morover, we'll be hosting a static app, which are limited in some aspects. These limitations are discussed here."
                ),
                padding="1rem 0rem",
            ),
            rx.hstack(
                rx.icon(tag="warning", color="orange"),
                rx.heading(
                    "You need to have NodeJS installed to use Vercel", size="sm"
                ),
                spacing="2rem",
                border="0.1rem solid orange",
                border_radius="6px",
                width="100%",
                padding="1rem 1rem",
                bg="rgba(246, 139, 23, 0.54)",
            ),
            rx.box(
                rx.markdown(
                    "In order to host your web application as a static site, you'll need to check off a few things. First, a vercel account is required. If you don't have one already, headover to Vercel and create one. You can also link your Vercel account to GitHub. Second, you need to have the latest version of ```vercel cli``` installed. If you don't already have it installed, you can visit their documentation **[here](https://vercel.com/docs/cli)** to see how to install."
                ),
                padding="1rem 0rem",
            ),
            rx.markdown(
                "To quickly get started, run the following command to install ```Vercel CLI```:"
            ),
            return_code_block("$ npm i -g vercel"),
            rx.markdown(
                "If you already have ```Vercel CLI``` installed, make sure it's the altest version by running: "
            ),
            return_code_block("$ npm i -g vercel@latest"),
            rx.box(
                rx.markdown(
                    "Once you have the above, navigate to the root of your ```.web``` folder. Make sure you're in the root and not inside ```_static``` fodler. Then, run the following command to start deployment: "
                ),
                padding="1rem 0rem",
            ),
            return_code_block("$ vercel deploy"),
            rx.box(
                rx.markdown(
                    "The above command will guide you through a series of steps that will deploy your website to vercel, if there are no previous issues. Once the deployment process is complete, you'll get a production link where you can view your static site hosted on Vercel."
                ),
                padding="1rem 0rem",
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
