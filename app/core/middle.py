import reflex as rx


class RxMiddle(rx.Vstack):
    def __init__(
        self,
        components: list,
        style: dict,
    ):
        super().__init__(
            children=components,
            style=style,
        )
