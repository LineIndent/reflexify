from app.config import app_configuration


class Config:
    data: dict = app_configuration

    @staticmethod
    def __site_name__() -> str:
        value = Config.data.get("site_name", "Site Name")
        return value if value else "Site Name"

    @staticmethod
    def __repo_name__() -> str:
        value = Config.data.get("repo_name", "")
        return value if value else ""

    @staticmethod
    def __repo_url__() -> str:
        value = Config.data.get("repo_url", "")
        return value if value else ""

    @staticmethod
    def __copy_right__() -> str:
        value = Config.data.get("copy_right", "")
        return value if value else ""

    @staticmethod
    def __attribute__() -> str:
        value = Config.data.get("attribute", "")
        return value if value else ""

    @staticmethod
    def __drawer__() -> bool:
        value = Config.data.get("drawer", False)
        return value if value else False

    @staticmethod
    def __theme_primary__() -> str:
        value = Config.data["theme"].get("primary", "orange")
        return value if value else "orange"

    @staticmethod
    def __theme_secondary__() -> str:
        value = Config.data["theme"].get("secondary", "orange")
        return value if value else "orange"

    @staticmethod
    def __theme_font__() -> str:
        value = Config.data["theme"].get("font", "Times New Roman")
        return value if value else "Times New Roman"

    @staticmethod
    def __all_social__():
        value = Config.data.get("socials", {})
        return value if value else None

    @staticmethod
    def __navigation__():
        value = Config.data.get("navigation", {})
        return value if value else None
