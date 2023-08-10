import importlib.util
import logging
import os
import shutil
import time


def check_if_pages_directory_exists() -> None:
    for __, dirs, __ in os.walk("./app/"):
        if "pages" not in dirs:
            page = os.path.join("./app/", "pages")
            os.mkdir(page)
            break
        else:
            break


def get_list_of_pages_from_directory():
    pages_list = set()
    dirs_list: list = []

    def loop_over_sub_folders(path: str):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if item == "__pycache__":
                continue
            if os.path.isfile(item_path) and item_path.endswith(".py"):
                pages_list.add(item_path)
            elif os.path.isdir(item_path):
                dirs_list.append(item_path)
                loop_over_sub_folders(item_path)

    for root, folders, files in os.walk("./app/pages"):
        for folder in folders:
            if folder != "__pycache__":
                path = os.path.join(root, folder)
                dirs_list.append(path)
                loop_over_sub_folders(path)

        for file in files:
            item_path = os.path.join(root, file)
            if os.path.isfile(item_path) and item_path.endswith(".py"):
                pages_list.add(item_path)

    return dirs_list, pages_list


def get_list_of_pages_from_config_file(docs: dict, parent_path: str = "./app/pages"):
    pages_list: list = []
    dirs_list: list = []

    def loop_over_nested_dict(docs: dict, current_path: str):
        if docs.get("navigation") is not None:
            docs = docs.get("navigation").items()
        else:
            docs = docs.items()

        for key, value in docs:
            if isinstance(value, dict):
                new_path = os.path.join(current_path, key)
                dirs_list.append(new_path)
                loop_over_nested_dict(value, new_path)
            else:
                new_path = os.path.join(current_path, value)
                file_path = new_path
                # file_path = new_path + ".py"
                pages_list.append(file_path)

    loop_over_nested_dict(docs, parent_path)

    return dirs_list, pages_list


def synchronize_directories(docs: dict):
    pages_dirs, pages_files = get_list_of_pages_from_directory()
    dict_dirs, dict_files = get_list_of_pages_from_config_file(docs)

    for pages_dir in pages_dirs:
        try:
            if pages_dir not in dict_dirs:
                shutil.rmtree(pages_dir)
                logging.info(f"Directory removed: {pages_dir}")
        except:  # noqa: E722
            pass

    for dict_dir in dict_dirs:
        if not os.path.exists(dict_dir):
            os.makedirs(dict_dir)
            logging.info(f"Directory created: {dict_dir}")

    for file_path in pages_files:
        try:
            if file_path not in dict_files:
                os.remove(file_path)
                logging.info(f"File removed: {file_path}")
        except:  # noqa: E722
            pass

    with open("./app/utilities/rx_template.py", "r") as file:
        rx_page = file.read()

    for file in dict_files:
        if not os.path.exists(file):
            with open(file, "w") as file:
                file.write(rx_page)
                logging.info(f"File created: {file}")


def get_dict_file():
    filepath = os.path.join("./app/", "config.py")
    module_spec = importlib.util.spec_from_file_location("config.py", filepath)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    return module.app_configuration


def build():
    app_configuration = get_dict_file()
    check_if_pages_directory_exists()
    synchronize_directories(app_configuration)


if __name__ == "__main__":
    # Set up the logging configuration...
    logging.basicConfig(
        filename="./app/reflexify.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Create the loggin stream so that changes also appear on the terminal.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    logging.getLogger().addHandler(console_handler)
    try:
        while True:
            build()
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Program interrupted. Exiting...")
