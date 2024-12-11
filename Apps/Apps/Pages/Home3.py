import reflex as rx


def create_nav_link(text):
    """Create a navigation link with hover effect."""
    return rx.el.a(
        text,
        href="#",
        _hover={"color": "#1F2937"},
        color="#4B5563",
    )


def create_nav_list_item(link_text):
    """Create a list item containing a navigation link."""
    return rx.el.li(create_nav_link(text=link_text))


def create_section_heading(text):
    """Create a section heading with specific styling."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="0.5rem",
        font_size="1.125rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_centered_heading(text):
    """Create a centered heading with specific styling."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="0.5rem",
        text_align="center",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_main_heading(text):
    """Create a main heading with large font size and centered alignment."""
    return rx.heading(
        text,
        font_weight="700",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_centered_image(alt_text, image_src):
    """Create a centered image with specific dimensions."""
    return rx.image(
        alt=alt_text,
        src=image_src,
        height="4rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width="4rem",
    )


def create_centered_text(content):
    """Create centered text with specific styling."""
    return rx.text(
        content,
        margin_bottom="1rem",
        text_align="center",
        color="#4B5563",
    )


def create_os_select_label():
    """Create a label for OS selection dropdown."""
    return rx.el.label(
        "Select your OS:",
        display="block",
        font_weight="500",
        margin_bottom="0.5rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_select_option(option_text):
    """Create an option for a select element."""
    return rx.el.option(option_text)


def create_os_select(select_id):
    """Create an OS selection dropdown with styling."""
    return rx.el.select(
        create_select_option(option_text="Windows"),
        create_select_option(option_text="macOS"),
        create_select_option(option_text="Linux"),
        id=select_id,
        border_width="1px",
        border_color="#D1D5DB",
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        width="100%",
    )


def create_os_select_container(select_id):
    """Create a container for OS selection with label and dropdown."""
    return rx.box(
        create_os_select_label(),
        create_os_select(select_id=select_id),
        margin_bottom="1rem",
    )


def create_price_display(price):
    """Create a centered price display with specific styling."""
    return rx.text(
        price,
        font_weight="700",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        text_align="center",
    )


def create_buy_button():
    """Create a 'Buy Now' button with styling and hover effect."""
    return rx.el.a(
        "Buy Now",
        href="#",
        background_color="#2563EB",
        display="block",
        font_weight="600",
        _hover={"background-color": "#1D4ED8"},
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        text_align="center",
        color="#ffffff",
    )


def create_centered_icon(alt_text, icon_tag):
    """Create a centered icon with specific dimensions."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="3rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width="3rem",
    )


def create_feature_description(description):
    """Create a centered feature description with specific styling."""
    return rx.text(description, text_align="center", color="#4B5563")


def create_feature_box(icon_alt, icon_tag, title, description):
    """Create a feature box with icon, title, and description."""
    return rx.box(
        create_centered_icon(alt_text=icon_alt, icon_tag=icon_tag),
        create_centered_heading(text=title),
        create_feature_description(description=description),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_footer_link(text):
    """Create a footer link with hover effect."""
    return rx.el.a(text, href="#", _hover={"color": "#D1D5DB"})


def create_footer_list_item(link_text):
    """Create a list item containing a footer link."""
    return rx.el.li(create_footer_link(text=link_text))


def create_social_icon(alt_text, icon_tag):
    """Create a social media icon with specific dimensions."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )


def create_social_link(icon_alt, icon_tag):
    """Create a social media link with icon."""
    return rx.el.a(
        create_social_icon(alt_text=icon_alt, icon_tag=icon_tag),
        href="#",
    )


def create_logo_with_text():
    """Create a logo with company name."""
    return rx.flex(
        rx.image(
            alt="SoftwareHub Logo",
            src="https://replicate.delivery/xezq/Fj2Vp8ItxvrPPJCa8C5ePfcHfX0DwG2b9QP45FgFzs0SCmznA/out-0.webp",
            height="2rem",
            margin_right="0.5rem",
            width="2rem",
        ),
        rx.text.span(
            "SoftwareHub",
            font_weight="600",
            color="#1F2937",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        display="flex",
        align_items="center",
    )


def create_account_button():
    """Create a 'My Account' button with styling and hover effect."""
    return rx.el.a(
        "My Account",
        href="#",
        background_color="#2563EB",
        _hover={"background-color": "#1D4ED8"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
    )


def create_header():
    """Create the main header with logo, navigation, and account button."""
    return rx.flex(
        create_logo_with_text(),
        rx.list(
            create_nav_list_item(link_text="Home"),
            create_nav_list_item(link_text="Products"),
            create_nav_list_item(link_text="About"),
            create_nav_list_item(link_text="Contact"),
            display="flex",
            column_gap="1.5rem",
        ),
        rx.box(create_account_button()),
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
        padding_left="1rem",
        padding_right="1rem",
        padding_top="1rem",
        padding_bottom="1rem",
    )


def create_explore_button():
    """Create an 'Explore Products' button with styling and hover effect."""
    return rx.el.a(
        "Explore Products",
        href="#products",
        background_color="#ffffff",
        font_weight="600",
        _hover={"background-color": "#F3F4F6"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        color="#1D4ED8",
    )


def create_learn_more_button():
    """Create a 'Learn More' button with border and hover effect."""
    return rx.el.a(
        "Learn More",
        href="#features",
        border_width="2px",
        border_color="#ffffff",
        font_weight="600",
        _hover={"background-color": "#2563EB"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        color="#ffffff",
    )


def create_hero_section():
    """Create the hero section with main heading, subtext, and action buttons."""
    return rx.box(
        rx.heading(
            "Premium Software Solutions",
            font_weight="700",
            margin_bottom="1rem",
            font_size="2.25rem",
            line_height="2.5rem",
            as_="h1",
        ),
        rx.text(
            "Empower your workflow with our cutting-edge digital products",
            margin_bottom="2rem",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        rx.flex(
            create_explore_button(),
            create_learn_more_button(),
            display="flex",
            justify_content="center",
            column_gap="1rem",
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
        padding_left="1rem",
        padding_right="1rem",
        text_align="center",
    )


def create_product_card_x():
    """Create a product card for ProductX."""
    return rx.box(
        create_centered_image(
            alt_text="ProductX icon showing a stylized gear",
            image_src="https://replicate.delivery/xezq/ush1ywpGK6IoFFo4vseUm6mRmxCo3prz5L9On4kTlKAkg58JA/out-0.webp",
        ),
        create_centered_heading(text="ProductX"),
        create_centered_text(content="Advanced productivity suite for professionals"),
        create_os_select_container(select_id="os-select-1"),
        create_price_display(price="$49.99"),
        create_buy_button(),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_product_card_secure_shield():
    """Create a product card for SecureShield."""
    return rx.box(
        create_centered_image(
            alt_text="SecureShield icon depicting a protective shield",
            image_src="https://replicate.delivery/xezq/octiyaaOfenfbpb46KzNRUPijm56Nwrp4akfHwqzIMJjEMnPB/out-0.webp",
        ),
        create_centered_heading(text="SecureShield"),
        create_centered_text(
            content="Comprehensive security solution for your devices"
        ),
        create_os_select_container(select_id="os-select-2"),
        create_price_display(price="$39.99"),
        create_buy_button(),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_product_card_cloud_sync():
    """Create a product card for CloudSync."""
    return rx.box(
        create_centered_image(
            alt_text="CloudSync icon showing interconnected cloud symbols",
            image_src="https://replicate.delivery/xezq/eGmgYtik9GSISiMoX3QowYVvpJwszJLw2SeGyz8Pt9VIBz5TA/out-0.webp",
        ),
        create_centered_heading(text="CloudSync"),
        create_centered_text(
            content="Seamless file synchronization across all devices"
        ),
        create_os_select_container(select_id="os-select-3"),
        create_price_display(price="$29.99"),
        create_buy_button(),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_featured_products_section():
    """Create the featured products section with product cards."""
    return rx.box(
        create_main_heading(text="Our Featured Products"),
        rx.box(
            create_product_card_x(),
            create_product_card_secure_shield(),
            create_product_card_cloud_sync(),
            gap="2rem",
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
        padding_left="1rem",
        padding_right="1rem",
    )


def create_features_section():
    """Create the features section with feature boxes."""
    return rx.box(
        create_main_heading(text="Why Choose SoftwareHub?"),
        rx.box(
            create_feature_box(
                icon_alt="High-quality icon",
                icon_tag="award",
                title="High-Quality Products",
                description="Our software is crafted with precision and care to ensure top-notch performance.",
            ),
            create_feature_box(
                icon_alt="24/7 Support icon",
                icon_tag="headphones",
                title="24/7 Customer Support",
                description="Our dedicated team is always ready to assist you with any questions or issues.",
            ),
            create_feature_box(
                icon_alt="Regular Updates icon",
                icon_tag="refresh-cw",
                title="Regular Updates",
                description="We continuously improve our products to keep you ahead of the curve.",
            ),
            gap="2rem",
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
        padding_left="1rem",
        padding_right="1rem",
    )


def create_cta_button():
    """Create a 'Shop Now' call-to-action button."""
    return rx.el.a(
        "Shop Now",
        href="#products",
        background_color="#2563EB",
        font_weight="600",
        _hover={"background-color": "#1D4ED8"},
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        font_size="1.125rem",
        line_height="1.75rem",
        color="#ffffff",
    )


def create_cta_section():
    """Create the call-to-action section with heading and button."""
    return rx.box(
        rx.heading(
            "Ready to Elevate Your Digital Experience?",
            font_weight="700",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        create_cta_button(),
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
        padding_left="1rem",
        padding_right="1rem",
        text_align="center",
    )


def create_main_content():
    """Create the main content sections of the page."""
    return rx.box(
        rx.box(
            create_hero_section(),
            background_color="#1D4ED8",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
        rx.box(
            create_featured_products_section(),
            id="products",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_features_section(),
            id="features",
            background_color="#F3F4F6",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_cta_section(),
            padding_top="5rem",
            padding_bottom="5rem",
        ),
    )


def create_quick_links_section():
    """Create the quick links section for the footer."""
    return rx.box(
        create_section_heading(text="Quick Links"),
        rx.list(
            create_footer_list_item(link_text="Home"),
            create_footer_list_item(link_text="Products"),
            create_footer_list_item(link_text="About Us"),
            create_footer_list_item(link_text="Contact"),
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
        width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
    )


def create_footer_content():
    """Create the main content of the footer."""
    return rx.flex(
        rx.box(
            create_section_heading(text="SoftwareHub"),
            rx.text(
                "Empowering your digital journey with premium software solutions.",
                font_size="0.875rem",
                line_height="1.25rem",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        create_quick_links_section(),
        rx.box(
            create_section_heading(text="Legal"),
            rx.list(
                create_footer_list_item(link_text="Terms of Service"),
                create_footer_list_item(link_text="Privacy Policy"),
                create_footer_list_item(link_text="Refund Policy"),
                font_size="0.875rem",
                line_height="1.25rem",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        rx.box(
            create_section_heading(text="Connect With Us"),
            rx.flex(
                create_social_link(
                    icon_alt="Facebook icon",
                    icon_tag="facebook",
                ),
                create_social_link(
                    icon_alt="Twitter icon",
                    icon_tag="twitter",
                ),
                create_social_link(
                    icon_alt="Instagram icon",
                    icon_tag="instagram",
                ),
                create_social_link(
                    icon_alt="LinkedIn icon",
                    icon_tag="linkedin",
                ),
                display="flex",
                column_gap="1rem",
            ),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        display="flex",
        flex_wrap="wrap",
        justify_content="space-between",
    )


def create_footer():
    """Create the complete footer with content and copyright."""
    return rx.box(
        create_footer_content(),
        rx.box(
            rx.text("© 2023 SoftwareHub. All rights reserved."),
            border_color="#374151",
            border_top_width="1px",
            margin_top="2rem",
            padding_top="1.5rem",
            text_align="center",
            font_size="0.875rem",
            line_height="1.25rem",
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
        padding_left="1rem",
        padding_right="1rem",
    )


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        rx.box(
            create_header(),
            background_color="#ffffff",
            box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
        ),
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="2rem",
            padding_bottom="2rem",
            color="#ffffff",
        ),
        class_name="font-['Inter']",
        background_color="#F9FAFB",
    )


@rx.page("/home3", "Apps")
def Home3():
    """Create the complete application with necessary scripts, styles, and content.rx.script(src="https://cdn.tailwindcss.com"),"""
    return rx.fragment(

        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        create_page_layout(),
    )
