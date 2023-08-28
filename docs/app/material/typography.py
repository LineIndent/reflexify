import reflex as rx


class Title(rx.Heading):
    def __init__(
        self,
        title: str,
        size="2xl",
        opacity="0.80",
        padding="0rem 0rem",
        letter_spacing="0.01em",
    ):
        super().__init__(
            children=[rx.text(title)],
            size=size,
            opacity=opacity,
            padding=padding,
            letter_spacing=letter_spacing,
        )


class Header(rx.Heading):
    def __init__(
        self,
        title: str,
        size="lg",
        opacity="0.90",
        padding="2rem 0rem",
        letter_spacing="0.01em",
    ):
        super().__init__(
            children=[rx.text(title)],
            size=size,
            opacity=opacity,
            padding=padding,
            letter_spacing=letter_spacing,
        )


class SubHeader(rx.Heading):
    def __init__(
        self,
        title: str,
        id: str = None,
        size="md",
        opacity="1",
        padding="0.75rem 0rem",
        letter_spacing="0.01em",
    ):
        super().__init__(
            children=[rx.text(title)],
            id=id,
            size=size,
            opacity=opacity,
            padding=padding,
            letter_spacing=letter_spacing,
        )
