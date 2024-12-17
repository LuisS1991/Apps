import reflex as rx



def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def create_hover_link(link_text):
    """Create a hoverable link with custom styling."""
    return rx.el.a(
        link_text,
        href="#",
        _hover={"color": "#4F46E5"},
        color="#374151",
    )


def create_subheading(heading_text):
    """Create a subheading with specific styling."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom="0.5rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_custom_text(margin_bottom, text_content):
    """Create a custom text element with specific styling and margin."""
    return rx.text(
        text_content,
        margin_bottom=margin_bottom,
        font_size="1.25rem",
        line_height="1.75rem",
    )


def create_main_heading(heading_text):
    """Create a main heading with centered alignment and specific styling."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_icon(alt_text, icon_tag):
    """Create an icon with specific dimensions and color."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="3rem",
        margin_bottom="1rem",
        color="#4F46E5",
        width="3rem",
    )


def create_gray_text(text_content):
    """Create a text element with gray color."""
    return rx.text(text_content, color="#4B5563")


def create_feature_box(icon_alt, icon_tag, title, description):
    """Create a feature box with an icon, title, and description."""
    return rx.box(
        create_icon(alt_text=icon_alt, icon_tag=icon_tag),
        create_subheading(heading_text=title),
        create_gray_text(text_content=description),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_testimonial_text(testimonial_content):
    """Create a testimonial text with specific styling."""
    return rx.text(
        testimonial_content,
        margin_bottom="1rem",
        color="#4B5563",
    )


def create_avatar(alt_text, image_src):
    """Create an avatar image with circular shape."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height="3rem",
        margin_right="1rem",
        border_radius="9999px",
        width="3rem",
    )


def create_bold_text(text_content):
    """Create a bold text element."""
    return rx.text(text_content, font_weight="600")


def create_small_gray_text(text_content):
    """Create a small gray text element."""
    return rx.text(
        text_content,
        color="#6B7280",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_name_title_box(name, title):
    """Create a box with a name and title."""
    return rx.box(
        create_bold_text(text_content=name),
        create_small_gray_text(text_content=title),
    )


def create_testimonial_author(avatar_alt, avatar_src, author_name, author_title):
    """Create a testimonial author section with avatar, name, and title."""
    return rx.flex(
        create_avatar(alt_text=avatar_alt, image_src=avatar_src),
        create_name_title_box(name=author_name, title=author_title),
        display="flex",
        align_items="center",
    )


def create_small_icon(alt_text, icon_tag):
    """Create a small icon."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )


def create_social_link(icon_alt, icon_tag):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_small_icon(alt_text=icon_alt, icon_tag=icon_tag),
        href="#",
        transition_duration="300ms",
        _hover={"color": "#818CF8"},
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_get_started_button():
    """Create a 'Get Started' button with specific styling."""
    return rx.el.button(
        "Get Started",
        background_color="#4F46E5",
        transition_duration="300ms",
        _hover={"background-color": "#4338CA"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_header():
    """Create the main header of the page with logo, navigation, and CTA button."""
    return rx.flex(
        rx.box(
            "InnovateMKT",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            color="#4F46E5",
        ),
        rx.box(
            create_hover_link(link_text="Home"),
            create_hover_link(link_text="Services"),
            create_hover_link(link_text="About"),
            create_hover_link(link_text="Contact"),
            display=rx.breakpoints({"0px": "none", "768px": "flex"}),
            column_gap="1.5rem",
        ),
        create_get_started_button(),
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
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
    )


def create_discover_services_button():
    """Create a 'Discover Our Services' button with specific styling."""
    return rx.el.button(
        "Discover Our Services",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#E0E7FF"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        color="#4338CA",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_hero_text_section():
    """Create the hero text section with heading, description, and CTA button."""
    return rx.box(
        rx.heading(
            "Elevate Your Brand with Innovative Marketing",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size=rx.breakpoints({"0px": "2.25rem", "768px": "3rem"}),
            line_height=rx.breakpoints({"0px": "2.5rem", "768px": "1"}),
            as_="h1",
        ),
        create_custom_text(
            margin_bottom="2rem",
            text_content="We help businesses thrive in the digital age with cutting-edge marketing strategies and creative solutions.",
        ),
        create_discover_services_button(),
        margin_bottom=rx.breakpoints({"0px": "2.5rem", "768px": "0"}),
        width=rx.breakpoints({"768px": "50%"}),
    )


def create_hero_section():
    """Create the full hero section with text and image."""
    return rx.flex(
        create_hero_text_section(),
        rx.box(
            rx.image(
                src="https://replicate.delivery/xezq/paQHS7Uy8KKGG5S50HkBk0ff8sIbfPfQwRy3bqO7Rwcga6pPB/out-0.webp",
                alt="Marketing team collaborating on a project",
                border_radius="0.5rem",
                box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            ),
            width=rx.breakpoints({"768px": "50%"}),
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
        display="flex",
        flex_direction=rx.mobile_and_tablet(rx.breakpoints({"0px": "column", "768px": "row"})),
        align_items="center",
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_services_section():
    """Create the services section with heading and feature boxes."""
    return rx.box(
        create_main_heading(heading_text="Our Services"),
        rx.box(
            create_feature_box(
                icon_alt="Digital Marketing icon",
                icon_tag="palette",
                title="Digital Marketing",
                description="Boost your online presence and reach your target audience effectively.",
            ),
            create_feature_box(
                icon_alt="Analytics icon",
                icon_tag="palette",
                title="Data Analytics",
                description="Make data-driven decisions with our advanced analytics solutions.",
            ),
            create_feature_box(
                icon_alt="Branding icon",
                icon_tag="palette",
                title="Brand Strategy",
                description="Develop a strong, cohesive brand identity that resonates with your audience.",
            ),
            gap="2.5rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
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
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_testimonials_grid():
    """Create a grid of testimonials."""
    return rx.box(
        rx.box(
            create_testimonial_text(
                testimonial_content='"InnovateMKT transformed our marketing strategy, resulting in a 200% increase in leads within just three months."'
            ),
            create_testimonial_author(
                avatar_alt="John Smith, CEO of TechStart",
                avatar_src="https://replicate.delivery/xezq/TxGkCfboxzStXyAyFR3QHWe3WDSpSxk4iYJFmBMFFfAQN90nA/out-0.webp",
                author_name="John Smith",
                author_title="CEO, TechStart",
            ),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        rx.box(
            create_testimonial_text(
                testimonial_content='"The team\'s creativity and data-driven approach helped us stand out in a crowded market. Highly recommended!"'
            ),
            create_testimonial_author(
                avatar_alt="Sarah Lee, Marketing Director at GrowthCo",
                avatar_src="https://replicate.delivery/xezq/IwnkNz0PSL5bJtMVp2vIyf02InlBLxtAgi2OylsWvQNUTP9JA/out-0.webp",
                author_name="Sarah Lee",
                author_title="Marketing Director, GrowthCo",
            ),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        gap="2.5rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(2, minmax(0, 1fr))",
            }
        ),
    )


def create_testimonials_section():
    """Create the full testimonials section with heading and testimonials grid."""
    return rx.box(
        rx.box(
            create_main_heading(heading_text="What Our Clients Say"),
            create_testimonials_grid(),
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
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
        ),
        background_color="#F3F4F6",
        padding_top="5rem",
        padding_bottom="5rem",
    )


def create_contact_button():
    """Create a 'Get in Touch' button with specific styling."""
    return rx.el.button(
        "Get in Touch",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#E0E7FF"},
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        color="#4F46E5",
        font_size="1.125rem",
        line_height="1.75rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_cta_section():
    """Create the call-to-action section with heading, description, and button."""
    return rx.box(
        rx.heading(
            "Ready to Elevate Your Marketing?",
            font_weight="700",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        create_custom_text(
            margin_bottom="2.5rem",
            text_content="Let's collaborate to create a tailored strategy that drives results for your business.",
        ),
        create_contact_button(),
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
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        text_align="center",
    )


def create_main_content():
    """Create the main content of the page including hero, services, testimonials, and CTA sections."""
    return rx.box(
        rx.box(
            create_hero_section(),
            background_color="#4338CA",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
        rx.box(
            create_services_section(),
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        create_testimonials_section(),
        rx.box(
            create_cta_section(),
            background_color="#4F46E5",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
    )


def create_footer_logo_section():
    """Create the logo and tagline section for the footer."""
    return rx.box(
        rx.heading(
            "InnovateMKT",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            as_="h3",
        ),
        rx.text(
            "Innovative Marketing Solutions",
            margin_top="0.5rem",
            color="#9CA3AF",
        ),
        margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
    )


def create_footer_content():
    """Create the main content of the footer including logo, tagline, and social links."""
    return rx.flex(
        create_footer_logo_section(),
        rx.flex(
            create_social_link(icon_alt="Facebook", icon_tag="facebook"),
            create_social_link(icon_alt="Twitter", icon_tag="twitter"),
            create_social_link(icon_alt="LinkedIn", icon_tag="linkedin"),
            create_social_link(icon_alt="Instagram", icon_tag="instagram"),
            display="flex",
            column_gap="1.5rem",
        ),
        display="flex",
        flex_direction=rx.breakpoints({"0px": "column", "768px": "row"}),
        align_items="center",
        justify_content="space-between",
    )


def create_footer_copyright():
    """Create the copyright section of the footer."""
    return rx.box(
        rx.text("© 2023 InnovateMKT. All rights reserved."),
        border_color="#374151",
        border_top_width="1px",
        margin_top="2rem",
        padding_top="2rem",
        text_align="center",
        color="#9CA3AF",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_footer():
    """Create the full footer section."""
    return rx.box(
        rx.box(
            create_footer_content(),
            create_footer_copyright(),
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
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
        ),
        background_color="#1F2937",
        padding_top="2.5rem",
        padding_bottom="2.5rem",
        color="#ffffff",
    )


def create_full_page():
     
    return rx.fragment(
        rx.box(
            rx.box(
                create_header(),
                background_color="#ffffff",
                box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
            ),
            create_main_content(),
            create_footer(),
            class_name="font-['Poppins']",
            background_color="#F9FAFB",
        ),
    )



@rx.page("/home1", "Apps")
def Home1() -> rx.Component:
    # Welcome Page (Index)
    return create_full_page()