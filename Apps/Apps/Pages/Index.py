import reflex as rx
from Apps.States import IndexState
from Apps.Componentes import (
    create_button_with_icon,
    create_section_heading,
    create_featured_properties_grid,
)


def create_main_content():
    """Create the main content section including headings, buttons, and featured properties."""
    return rx.box(
        rx.box(
            create_section_heading(text="Cargar listados de casas"),
            rx.flex(
                create_button_with_icon(
                    hover_style={"background-color": "#059669"},
                    background_color="#10B981",
                    icon_name="home",
                    button_text=" Ministerio de Vivienda ",
                    evento=IndexState.obtener_datos_min_vivienda,
                ),
                create_button_with_icon(
                    hover_style={"background-color": "#D97706"},
                    background_color="#F59E0B",
                    icon_name="building",
                    button_text=" Agencia Nacional de Vivienda (ANV) ",
                    evento=IndexState.obtener_datos_anv,
                ),
                create_button_with_icon(
                    hover_style={"background-color": "#DC2626"},
                    background_color="#EF4444",
                    icon_name="landmark",
                    button_text=" Banco Hipotecario del Uruguay (BHU) ",
                    evento=IndexState.obtener_datos_bhu,
                ),
                display="flex",
                flex_wrap="wrap",
                gap="1rem",
            ),
            margin_bottom="2rem",
        ),
        rx.box(
            create_section_heading(text="Llamados Vigentes"),
            create_featured_properties_grid(listado=IndexState.listado),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_top="2rem",
        margin_left="auto",
        margin_right="auto",
        padding="1rem",
    )


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        rx.box(
            rx.heading(
                "House Advertisements",
                font_weight="700",
                font_size="1.875rem",
                line_height="2.25rem",
                as_="h1",
            ),
            background_color="#2563EB",
            padding="1rem",
            color="#ffffff",
        ),
        rx.box(
            create_main_content(),
            height="80vh",
            overflow="scroll",
        ),
        rx.box(
            rx.text("© 2023 House Advertisements. All rights reserved."),
            background_color="#1F2937",
            margin_top="2rem",
            padding_top="1rem",
            padding_bottom="1rem",
            text_align="center",
            color="#ffffff",
        ),
        background_color="#F3F4F6",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
    )


@rx.page("/", "Apps")
def index():
    """Render the complete house advertisements page with necessary styles and content."""
    return create_page_layout()
