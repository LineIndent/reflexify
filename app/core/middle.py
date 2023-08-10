import reflex as rx

rx_middle_style_sheet = {
    "width": ["100%", "100%", "100%", "60%", "60%"],
    "top": "0",
    "position": "block",
    "padding_top": "5rem",
    "align_items": "start",
    "padding_left": ["1rem", "1rem", "1rem", "", ""],
    "padding_bottom": "6rem",
    "transition": "all 550ms ease",
    "min_height": "100vh",
}


class RxMiddle(rx.Vstack):
    def __init__(self, style=rx_middle_style_sheet):
        super().__init__(style=style)

        self.children = []
