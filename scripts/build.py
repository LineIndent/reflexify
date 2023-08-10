import os


def check_if_pages_directory_exists() -> None:
    for __, dirs, __ in os.walk("./app/"):
        if "page" not in dirs:
            page = os.path.join("./app/", "page")
            os.mkdir(page)
            break


if __name__ == "__main__":
    check_if_pages_directory_exists()
