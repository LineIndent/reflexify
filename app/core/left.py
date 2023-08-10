import reflex as rx

rx_left_style_sheet = {
    "width": "20%",
    "top": "0",
    "position": "sticky",
    "z_index": "-2",
    "padding_top": "5rem",
    "align_items": "start",
    "padding_left": ["", "", "", "4rem", "10rem"],
    "transition": "all 550ms ease",
}


class RxLeft(rx.Vstack):
    def __init__(self, style=rx_left_style_sheet):
        super().__init__(style=style)

        self.children = []
