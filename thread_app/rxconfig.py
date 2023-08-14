import reflex as rx

class ThreadappConfig(rx.Config):
    pass

config = ThreadappConfig(
    app_name="thread_app",
    db_url="sqlite:///thread_app.db",
)