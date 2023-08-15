import reflex as rx


class ReflexifyConfig(rx.Config):
    pass


config = ReflexifyConfig(
    app_name="./app/app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
