import reflex as rx
from Apps.Componentes.Icons import create_icon


def create_button_with_icon(
    hover_style, background_color, icon_name, button_text, evento
):
    """Create a button with an icon and specific styling."""
    return rx.el.button(
        create_icon(icon_name=icon_name),
        button_text,
        on_click=evento,
        background_color=background_color,
        display="flex",
        font_weight="700",
        _hover=hover_style,
        align_items="center",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
    )
