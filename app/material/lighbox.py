import reflex as rx


class LightBox(rx.Box):
    def __init__(
        self,
        components: list,
        transition="all 550ms ease",
        # _hover={
        #     "bg": "rgba(255,255,255, 0.025)",
        # },
    ):
        super().__init__(
            children=components,
            transition=transition,
            # _hover=_hover,
        )
