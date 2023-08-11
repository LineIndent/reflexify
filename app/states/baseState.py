from .mainState import MainState


class BaseState(MainState):
    txt: str = "Hi"

    def get_scroll_data(self):
        print(self.txt)
