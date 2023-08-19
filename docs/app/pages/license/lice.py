from app.core.base import RxBasePage
from app.helpers.nav_helpers import NavHelper
import app.material as rf
import reflex as rx


lice = """MIT License

Copyright (c) 2023 Seyed Ahmad Pour Hakimi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""


class RxPage:
    # Title of page: must match high-level key in config.py
    def __title__(self):
        return "License"

    # Page route path: must follow /parent-key/file-name *without .py extension*
    def __route__(self):
        return "/license/lice"

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
            rf.Title("License"),
            rx.box(
                rx.code_block(
                    lice,
                    language="plaintext",
                    theme="dark",
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
