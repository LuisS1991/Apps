import reflex as rx
from Apps.States import IndexState
from Apps.Models.Llamado import Llamado



def deaw_datos(datos: Llamado):
    return rx.box(rx.text(f"{datos.nombre} estado : {datos.vigencia}"))


@rx.page("/home", "Apps")
def Index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.button("get data", on_click=IndexState.obtener_datos_min_vivienda),
        rx.cond(
            IndexState.listado.length() <= 0,
            rx.text("hoy datos"),
            rx.foreach(IndexState.listado, deaw_datos),
        ),
    )
