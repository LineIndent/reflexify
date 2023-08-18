from .mainState import MainState


class DrawerState(MainState):
    show_left: bool = False

    def left(self):
        self.show_left = not (self.show_left)
