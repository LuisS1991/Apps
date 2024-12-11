"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from Apps.Pages import *
from Apps.Api.RelesesApi import descargaractualizacion


app = rx.App()
# app.add_page(index)
app.api.add_api_route("/releeas", descargaractualizacion)
