"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from Apps.Pages import *
from Apps.Api.RelesesApi import descargaractualizacion,tst


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    ],
)
# app.add_page(index)
app.api.add_api_route("/releeas", descargaractualizacion)
app.api.add_api_route("/test", tst)
