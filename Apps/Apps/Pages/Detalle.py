import reflex as rx


def create_styled_text(text_color, margin_bottom, content):
    """Create a styled text component with custom color and margin."""
    return rx.text(
        content,
        margin_bottom=margin_bottom,
        color=text_color,
    )


def create_icon(icon_height, icon_tag, icon_width):
    """Create an icon component with custom height, width, and tag."""
    return rx.icon(
        tag=icon_tag,
        height=icon_height,
        margin_right="0.5rem",
        width=icon_width,
    )


def create_text_span(content):
    """Create a text span component with right margin."""
    return rx.text.span(content, margin_right="1rem")


def create_list_item(content):
    """Create a list item component."""
    return rx.el.li(content)


def create_property_image(alt_text, image_src):
    """Create a property image component with custom alt text and source."""
    return rx.image(
        alt=alt_text,
        src=image_src,
        height="6rem",
        object_fit="cover",
        border_radius="0.5rem",
        width="100%",
    )


def create_property_features():
    """Create a flex container with property features (bedrooms, bathrooms, area)."""
    return rx.flex(
        create_icon(
            icon_height="1.5rem",
            icon_tag="bed",
            icon_width="1.5rem",
        ),
        create_text_span(content="3 bedrooms"),
        create_icon(
            icon_height="1.5rem",
            icon_tag="bath",
            icon_width="1.5rem",
        ),
        create_text_span(content="2 bathrooms"),
        create_icon(
            icon_height="1.5rem",
            icon_tag="square",
            icon_width="1.5rem",
        ),
        rx.text.span("150 m²"),
        display="flex",
        align_items="center",
        margin_bottom="1rem",
    )


def create_schedule_viewing_button():
    """Create a 'Schedule a Viewing' button component."""
    return rx.el.button(
        "Schedule a Viewing",
        background_color="#3B82F6",
        font_weight="700",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.25rem",
        color="#ffffff",
        width="100%",
    )


def create_contact_agent_button():
    """Create a 'Contact Listing Agent' button component with phone icon."""
    return rx.el.button(
        create_icon(
            icon_height="1.25rem",
            icon_tag="phone",
            icon_width="1.25rem",
        ),
        " Contact Listing Agent ",
        background_color="#10B981",
        display="flex",
        font_weight="700",
        _hover={"background-color": "#059669"},
        align_items="center",
        justify_content="center",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.25rem",
        color="#ffffff",
        width="100%",
    )


def create_property_details():
    """Create a component with detailed property information and features."""
    return rx.box(
        rx.heading(
            "Modern House with Garden",
            font_weight="700",
            margin_bottom="1rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        create_styled_text(
            text_color="#4B5563",
            margin_bottom="1rem",
            content="123 Maple Street, Cityville, State 12345",
        ),
        create_property_features(),
        rx.text(
            "$250,000",
            font_weight="700",
            margin_bottom="1rem",
            font_size="1.5rem",
            line_height="2rem",
            color="#059669",
        ),
        create_styled_text(
            text_color="#374151",
            margin_bottom="1.5rem",
            content="This stunning modern house features a beautiful garden, open-concept living spaces, and high-end finishes throughout. Perfect for families or those who love to entertain.",
        ),
        rx.heading(
            "Property Features:",
            font_weight="600",
            margin_bottom="0.5rem",
            font_size="1.25rem",
            line_height="1.75rem",
            as_="h3",
        ),
        rx.list(
            create_list_item(content="Spacious open-plan kitchen and living area"),
            create_list_item(content="Master bedroom with ensuite bathroom"),
            create_list_item(content="Large windows providing ample natural light"),
            create_list_item(content="Beautifully landscaped garden with patio"),
            create_list_item(content="Two-car garage"),
            create_list_item(content="Energy-efficient appliances"),
            list_style_type="disc",
            list_style_position="inside",
            margin_bottom="1.5rem",
        ),
        rx.box(
            create_schedule_viewing_button(),
            create_contact_agent_button(),
            display="flex",
            flex_direction="column",
            gap="1rem",
        ),
        padding="1.5rem",
    )


def create_property_gallery():
    """Create a gallery component with multiple property images."""
    return rx.box(
        rx.image(
            alt="Front view of the modern house with a beautiful garden",
            src="https://placehold.co/800x600?text=Modern+House+Front+View",
            height="16rem",
            margin_bottom="1rem",
            object_fit="cover",
            border_radius="0.5rem",
            width="100%",
        ),
        rx.box(
            create_property_image(
                alt_text="Spacious living room with large windows",
                image_src="https://placehold.co/300x200?text=Living+Room",
            ),
            create_property_image(
                alt_text="Modern kitchen with island",
                image_src="https://placehold.co/300x200?text=Kitchen",
            ),
            create_property_image(
                alt_text="Master bedroom with ensuite bathroom",
                image_src="https://placehold.co/300x200?text=Master+Bedroom",
            ),
            create_property_image(
                alt_text="Beautifully landscaped backyard with patio",
                image_src="https://placehold.co/300x200?text=Backyard",
            ),
            create_property_image(
                alt_text="Modern bathroom with double vanity",
                image_src="https://placehold.co/300x200?text=Bathroom",
            ),
            create_property_image(
                alt_text="Two-car garage",
                image_src="https://placehold.co/300x200?text=Garage",
            ),
            gap="1rem",
            display="grid",
            grid_template_columns="repeat(3, minmax(0, 1fr))",
        ),
        padding="1.5rem",
    )


def create_property_listing():
    """Create a complete property listing component with details and gallery."""
    return rx.box(
        rx.box(
            create_property_details(),
            create_property_gallery(),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
        ),
        background_color="#ffffff",
        overflow="hidden",
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    )


def create_house_advertisement_page():
    """Create the main house advertisement page with header, content, and footer."""
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
            create_property_listing(),
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


@rx.page(route="/llamado/detalle")
def detalle():
    return create_house_advertisement_page()
