from app.styles._base import base_css


class CSSHelper:
    @staticmethod
    def __base_css__() -> dict:
        return base_css

    @staticmethod
    def __app_css__() -> dict:
        return base_css.get("app", {})

    @staticmethod
    def __base_css__() -> dict:
        return base_css.get("base", {})

    @staticmethod
    def __left_css__() -> dict:
        return base_css.get("left", {})

    @staticmethod
    def __middle_css__() -> dict:
        return base_css.get("middle", {})

    @staticmethod
    def __right_css__() -> dict:
        return base_css.get("right", {})

    @staticmethod
    def __header_css__() -> dict:
        return base_css.get("header", {})

    @staticmethod
    def __header_main_css__() -> dict:
        return CSSHelper.__header_css__().get("main", {})

    @staticmethod
    def __header_icon_css__() -> dict:
        return CSSHelper.__header_css__().get("icon", {})

    @staticmethod
    def __header_navigation_css__() -> dict:
        return CSSHelper.__header_css__().get("navigation", {})

    @staticmethod
    def __header_link_text_css__() -> dict:
        return CSSHelper.__header_css__().get("link_text", {})

    @staticmethod
    def __header_site_name_css__() -> dict:
        return CSSHelper.__header_css__().get("site_name", {})

    @staticmethod
    def __header_max_header_css__() -> dict:
        return CSSHelper.__header_css__().get("max_header", {})

    @staticmethod
    def __header_min_header_css__() -> dict:
        return CSSHelper.__header_css__().get("min_header", {})

    @staticmethod
    def __footer_css__() -> dict:
        return base_css.get("footer", {})

    @staticmethod
    def __footer_style_css__() -> dict:
        return CSSHelper.__footer_css__().get("style", {})

    @staticmethod
    def __footer_socials_css__() -> dict:
        return CSSHelper.__footer_css__().get("socials", {})

    @staticmethod
    def __drawer_css__() -> dict:
        return base_css.get("drawer", {})

    @staticmethod
    def __drawer_heading_css__() -> dict:
        return CSSHelper.__drawer_css__().get("heading", {})

    @staticmethod
    def __drawer_repo_css__() -> dict:
        return CSSHelper.__drawer_css__().get("repo", {})

    @staticmethod
    def __drawer_router_css__() -> dict:
        return CSSHelper.__drawer_css__().get("router", {})
