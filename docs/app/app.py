# Import the Reflex library and Reflexify modules
import reflex as rx
from .states.mainState import MainState
from .helpers.css_helpers import CSSHelper
from .router import set_application_routes

# Create a new Reflex Application instance + pass in main state and app css
app = rx.App(state=MainState, style=CSSHelper.__app_css__())

# Call the router to get and set the pages to the application routes
set_application_routes(app)

# Compile the application and run
app.compile()
