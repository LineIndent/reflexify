import reflex as rx
from bs4 import BeautifulSoup
import httpx


icon_list = [
    "<img width='10' height='10' src='https://img.icons8.com/ios-filled/50/price-tag.png' style='filter: brightness(0) invert(1);' />",
    "<img width='10' height='10' src='https://img.icons8.com/ios-filled/50/star--v1.png' style='filter: brightness(0) invert(1);'/>",
    "<img width='10' height='10' src='https://img.icons8.com/ios/50/code-fork.png' style='filter: brightness(0) invert(1);'/>",
]


class RepositoryData:
    def __init__(self, config: dict):
        self.config = config
        self.rx_repo_data = rx.hstack(
            spacing="1.15rem",
            cursor="pointer",
            on_click=rx.redirect(self.config.get("repo_url", "")),
        )

        self.git_repo_name = rx.hstack(
            rx.text(
                self.config.get("repo_name", ""), color="white", font_weight="semibold"
            ),
        )

        if "repo_url" in self.config:
            self.git_icon = rx.html(
                "<img width='24' height='24' src='https://img.icons8.com/ios-filled/50/000000/git.png' style='filter: brightness(0) invert(1);'/>"
            )

            self.git_repo_data = self.get_repository_data()

        else:
            self.git_icon = rx.container()
            self.git_repo_data = rx.hstack()

        self.git_data = rx.vstack(
            self.git_repo_name,
            self.git_repo_data,
            spacing="0rem",
            align_items="start",
        )

    def get_repository_data(self):
        temp_repo_data = rx.hstack()

        span_elements = [
            "css-truncate css-truncate-target text-bold mr-2",
            "Counter js-social-count",
            "Counter",
        ]

        with httpx.Client() as client:
            response = client.get(self.config.get("repo_url"))
            data = response.content

        soup = BeautifulSoup(data, "html.parser")

        for i, span in enumerate(span_elements):
            span_element = soup.find("span", span)

            if span_element is not None:
                txt = span_element.text.strip()

                temp_repo_data.children.append(
                    rx.hstack(
                        rx.html(icon_list[i]),
                        rx.text(txt, color="white", font_size=11),
                        spacing="0.35rem",
                    )
                )
            else:
                pass

        return temp_repo_data

    def build(self):
        self.rx_repo_data.children.append(self.git_icon)
        self.rx_repo_data.children.append(self.git_data)

        return rx.tooltip(
            self.rx_repo_data,
            label="Go to repository",
        )