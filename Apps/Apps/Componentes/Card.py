import reflex as rx
from Apps.Models import Llamado
from Apps.Componentes.SubHeading import create_subheading


def create_property_image(alt_text, image_url):
    return rx.image(
        src=image_url,
        alt=alt_text,
        height="12rem",
        object_fit="cover",
        width="100%",
    )


def create_property_details(details_text):
    """Create a text element for property details with specific styling."""
    return rx.text(details_text, color="#374151")


def create_property_price(price_text):
    """Create a text element for property price with specific styling."""
    return rx.text(
        price_text,
        font_weight="700",
        margin_top="0.5rem",
        color="#059669",
    )


def create_view_details_button(link: str):
    """Create a 'View Details' button with specific styling."""
    return rx.el.button(
        "Ver Detalles",
        on_click=rx.redirect(link),
        background_color="#3B82F6",
        font_weight="700",
        _hover={"background-color": "#2563EB"},
        margin_top="1rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
    )


def create_property_info_box(title, details, linkDetalle):
    """Create a box containing property information including title, details, price, and a view details button."""
    return rx.box(
        create_subheading(text=title),
        create_property_details(details_text=details),
        # create_property_price(price_text=price),
        create_view_details_button(linkDetalle),
        padding="1rem",
    )


def Card(datos: Llamado)->rx.Component:
    return  rx.box(
            create_property_image(
                alt_text=datos.nombre,
                image_url="https://placehold.co/400x300?text=Modern+House+with+Garden",
            ),
            create_property_info_box(
                title=datos.nombre,
                details=datos.vigencia,
                linkDetalle=datos.link,
            ),
            background_color="#ffffff",
            overflow="hidden",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        )
