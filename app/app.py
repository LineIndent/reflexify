import importlib
import os
import reflex as rx
from .config import app_configuration
from .states.mainState import MainState


config: dict = app_configuration
routes: dict = {}

app = rx.App(state=MainState)


def create_module_from_file_path(file: str):
    filepath = os.path.join(root, file)
    module_spec = importlib.util.spec_from_file_location(file, filepath)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module.RxPage(config)


for root, dirs, files in os.walk("./app/pages"):
    for file in files:
        if file.endswith(".py") and file != "routes.py" and file != "page404.py":
            __module__ = create_module_from_file_path(file)
            routes[__module__.__route__()] = __module__

        if file == "page404.py":
            filepath = os.path.join(root, file)
            __module__ = create_module_from_file_path(file)
            app.add_custom_404_page(__module__.build())


for key, value in routes.items():
    app.add_page(
        component=value.build(),
        route=key,
    )


app.compile()
