import reflex as rx

rx_right_style_sheet = {
    "width": ["0%", "0%", "0%", "20%", "20%"],
    "top": "0",
    "position": "sticky",
    "z_index": "-2",
    "padding_top": "5rem",
    "align_items": ["end", "end", "end", "start", "start"],
    "padding_right": ["1rem", "1rem", "1rem", "", ""],
    "transition": "all 550ms ease",
}


class RxRight(rx.Vstack):
    def __init__(self, style=rx_right_style_sheet):
        super().__init__(style=style)

        self.children = []
