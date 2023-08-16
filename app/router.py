import importlib
import os
import reflex as rx


def create_module_from_file_path(file: str, filepath: str):
    module_spec = importlib.util.spec_from_file_location(file, filepath)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module.RxPage()


def get_application_routes_from_pages_dir(app: rx.App):
    routes: dict = {}
    for root, dirs, files in os.walk("./app/pages"):
        for file in files:
            filepath = os.path.join(root, file)
            if file.endswith(".py") and file != "page404.py":
                page_module = create_module_from_file_path(file, filepath)
                routes[page_module.__route__()] = page_module

            if file == "page404.py":
                filepath = os.path.join(root, file)
                page_module = create_module_from_file_path(file, filepath)
                app.add_custom_404_page(page_module.build())

    add_routes_to_app_pages(app, routes)


def add_routes_to_app_pages(app: rx.App, routes: dict):
    for key, value in routes.items():
        app.add_page(
            component=value.build(),
            route=key,
            title=value.__title__(),
        )


def set_application_routes(app: rx.App):
    get_application_routes_from_pages_dir(app)
