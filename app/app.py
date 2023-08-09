import importlib
import os
import reflex as rx
from .config import app_configuration
from .states.mainState import MainState


config: dict = app_configuration

app = rx.App(state=MainState)

routes: dict = {}

for root, dirs, files in os.walk("./app/pages"):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            module_spec = importlib.util.spec_from_file_location(file, filepath)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            __module__ = module.RxPage(config)
            routes[__module__.__route__()] = __module__


for key, value in routes.items():
    app.add_page(
        component=value.build(),
        route=key,
    )

app.compile()
