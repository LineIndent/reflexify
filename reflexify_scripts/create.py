import os
from pathlib import Path
import shutil
import click


file_structure = {
    "core": [
        "__init__.py",
        "base.py",
        "drawer.py",
        "footer.py",
        "header.py",
        "left.py",
        "middle.py",
        "mobile.py",
        "repository.py",
        "right.py",
    ],
    "helpers": ["__init__.py", "app_config.py", "css_helpers.py", "nav_helpers.py"],
    "material": ["__init__.py", "typography.py"],
    "states": ["__init__.py", "drawerState.py", "headerState.py", "mainState.py"],
    "styles": ["__init__.py", "_base.py"],
    "utilities": ["__init__.py", "rx_page404.py", "rx_template.py", "rx_index.py"],
    "app.py": None,
    "config.py": None,
    "router.py": None,
}


scripts_structure = {
    "reflexify_scripts": ["__init__.py", "build.py", "create.py"],
}


def create_src_directory():
    if not os.path.exists("./app"):
        os.mkdir("./app")

    if not os.path.exists("./reflexify_scripts"):
        os.mkdir("./reflexify_scripts")


def create_src_file_structure():
    source = os.path.join(Path(__file__).parent.parent, "app")
    replicate = Path("./app")

    def create_dir_file_structure(dir_path: str, key: str, files):
        os.mkdir(dir_path)
        for file in files:
            source_path = os.path.join(source, key, file)
            replicate_path = os.path.join(dir_path, file)
            with open(source_path, "r") as src_file, open(
                replicate_path, "w"
            ) as dst_file:
                dst_file.write(src_file.read())

    for key, value in file_structure.items():
        if value is not None:
            dir_path = os.path.join(replicate, key)
            if isinstance(value, list):
                create_dir_file_structure(dir_path, key, value)
        else:
            source_file = os.path.join(source, key)
            file_path = os.path.join(replicate, key)
            with open(source_file, "r") as src_file, open(file_path, "w") as file:
                file.write(src_file.read())


def change_rx_config_details():
    dir_name = os.getcwd().split("/")[-1]

    for file in os.listdir(os.getcwd()):
        if file == "rxconfig.py":
            file_path = os.path.join(os.getcwd(), file)
            with open(file_path, "r") as rder:
                config = rder.read()
                config = config.replace(f"{dir_name}", "app")
            with open(file_path, "w") as wter:
                wter.write(config)

    remove_folder = os.path.join(os.getcwd(), dir_name)
    shutil.rmtree(remove_folder)


def set_up_reflexify_scripts():
    scripts_src = Path(__file__).parent
    scripts_dst = "./reflexify_scripts"

    for key, values in scripts_structure.items():
        for value in values:
            src_file = os.path.join(scripts_src, value)
            dst_file = os.path.join(scripts_dst, value)

            with open(src_file, "r") as rder, open(dst_file, "w") as wter:
                wter.write(rder.read())


@click.command()
def create():
    click.echo("Setting up Reflexify directory...")
    create_src_directory()
    create_src_file_structure()
    set_up_reflexify_scripts()
    click.echo("Source directory created successfully.")

    click.echo("Configuring rxconfig.py file...")
    change_rx_config_details()


@click.group()
def reflexify():
    pass


reflexify.add_command(create)

if __name__ == "__main__":
    reflexify()
