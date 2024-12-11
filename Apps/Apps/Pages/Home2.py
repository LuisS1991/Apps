import reflex as rx


def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def create_styled_link(hover_style, text_color, link_url, link_text):
    """Create a styled anchor element with hover effects."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover=hover_style,
        color=text_color,
    )


def create_list_item_link(hover_style, text_color, link_url, link_text):
    """Create a list item containing a styled link."""
    return rx.el.li(
        create_styled_link(
            hover_style=hover_style,
            text_color=text_color,
            link_url=link_url,
            link_text=link_text,
        )
    )


def create_custom_heading(heading_level, font_size, margin_bottom, heading_text):
    """Create a custom heading with specified styles."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_=heading_level,
    )


def create_main_heading(heading_level, font_size, line_height, heading_text):
    """Create a main heading with bold styling."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="1rem",
        font_size=font_size,
        line_height=line_height,
        as_=heading_level,
    )


def create_download_button():
    """Create a styled download button with hover effects."""
    return rx.el.a(
        "Download",
        href="#download",
        background_color="#2563EB",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#1D4ED8"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_section_heading(heading_text):
    """Create a centered section heading."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_centered_icon(alt_text, icon_height, icon_tag, icon_width):
    """Create a centered icon with specified dimensions."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height=icon_height,
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width=icon_width,
    )


def create_feature_box(icon_alt, icon_tag, feature_title):
    """Create a feature box with an icon and title."""
    return rx.box(
        create_centered_icon(
            alt_text=icon_alt,
            icon_height="4rem",
            icon_tag=icon_tag,
            icon_width="4rem",
        ),
        create_custom_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=feature_title,
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        text_align="center",
    )


def create_description_text(description_text):
    """Create a styled description text."""
    return rx.text(
        description_text,
        margin_bottom="1rem",
        color="#4B5563",
    )


def create_hover_link(link_url, link_text):
    """Create a link with hover effect."""
    return rx.el.a(
        link_text,
        href=link_url,
        font_weight="600",
        _hover={"color": "#1E40AF"},
        color="#2563EB",
    )


def create_app_image(alt_text, image_src):
    """Create a styled image for an app."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height="12rem",
        margin_bottom="1rem",
        object_fit="cover",
        border_radius="0.25rem",
        width="100%",
    )


def create_small_text(text_content):
    """Create small, gray text."""
    return rx.text.span(
        text_content,
        color="#6B7280",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_app_info_footer(platform_text):
    """Create a footer for app information with platform text and download button."""
    return rx.flex(
        create_small_text(text_content=platform_text),
        create_download_button(),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )


def create_app_card(image_alt, image_src, app_name, app_description):
    """Create a card displaying app information."""
    return rx.box(
        create_app_image(alt_text=image_alt, image_src=image_src),
        create_custom_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=app_name,
        ),
        create_description_text(description_text=app_description),
        create_app_info_footer(platform_text="Linux, Windows, macOS"),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_small_icon(alt_text, icon_tag):
    """Create a small icon."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )


def create_social_link(link_url, icon_alt, icon_tag):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_small_icon(alt_text=icon_alt, icon_tag=icon_tag),
        href=link_url,
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
    )


def create_search_input():
    """Create a styled search input field."""
    return rx.el.input(
        placeholder="Search apps...",
        type="text",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "border-color": "#3B82F6",
            "outline-style": "none",
        },
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_top_left_radius="9999px",
        border_bottom_left_radius="9999px",
    )


def create_search_button():
    """Create a styled search button with an icon."""
    return rx.el.button(
        rx.icon(
            alt="Search",
            tag="search",
            height="1.25rem",
            display="inline",
            width="1.25rem",
        ),
        background_color="#2563EB",
        transition_duration="300ms",
        _hover={"background-color": "#1D4ED8"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_top_right_radius="9999px",
        border_bottom_right_radius="9999px",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_header():
    """Create the main header with logo, navigation, and search."""
    return rx.flex(
        rx.box(
            "AppHub",
            font_weight="700",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#2563EB",
        ),
        rx.list(
            create_list_item_link(
                hover_style={"color": "#2563EB"},
                text_color="#374151",
                link_url="#home",
                link_text="Home",
            ),
            create_list_item_link(
                hover_style={"color": "#2563EB"},
                text_color="#374151",
                link_url="#categories",
                link_text="Categories",
            ),
            create_list_item_link(
                hover_style={"color": "#2563EB"},
                text_color="#374151",
                link_url="#platforms",
                link_text="Platforms",
            ),
            create_list_item_link(
                hover_style={"color": "#2563EB"},
                text_color="#374151",
                link_url="#about",
                link_text="About",
            ),
            display=rx.breakpoints({"0px": "none", "768px": "flex"}),
            column_gap="1.5rem",
        ),
        rx.flex(
            create_search_input(),
            create_search_button(),
            display="flex",
            align_items="center",
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
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
    )


def create_browse_apps_button():
    """Create a styled 'Browse Apps' button."""
    return rx.el.a(
        "Browse Apps",
        href="#browse",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#DBEAFE"},
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        color="#2563EB",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_hero_section():
    """Create the hero section with main heading and call-to-action."""
    return rx.box(
        create_main_heading(
            heading_level="h1",
            font_size=rx.breakpoints({"0px": "2.25rem", "768px": "3.75rem"}),
            line_height=rx.breakpoints({"0px": "2.5rem", "768px": "1"}),
            heading_text="Boost Your Productivity",
        ),
        rx.text(
            "Download the best productivity apps for Linux, Windows, and macOS",
            margin_bottom="2rem",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_browse_apps_button(),
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


def create_categories_section():
    """Create the categories section with feature boxes."""
    return rx.box(
        create_section_heading(heading_text="Popular Categories"),
        rx.box(
            create_feature_box(
                icon_alt="Task Management",
                icon_tag="clipboard-list",
                feature_title="Task Management",
            ),
            create_feature_box(
                icon_alt="Calendar & Scheduling",
                icon_tag="calendar",
                feature_title="Calendar & Scheduling",
            ),
            create_feature_box(
                icon_alt="Note Taking",
                icon_tag="pen-tool",
                feature_title="Note Taking",
            ),
            create_feature_box(
                icon_alt="Time Tracking",
                icon_tag="timer",
                feature_title="Time Tracking",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(2, minmax(0, 1fr))",
                    "768px": "repeat(4, minmax(0, 1fr))",
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


def create_linux_platform_box():
    """Create an information box for Linux platform."""
    return rx.box(
        create_centered_icon(
            alt_text="Linux",
            icon_height="6rem",
            icon_tag="laptop",
            icon_width="6rem",
        ),
        create_custom_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text="Linux",
        ),
        create_description_text(
            description_text="Open-source power for developers and enthusiasts"
        ),
        create_hover_link(
            link_url="#linux-apps",
            link_text="Browse Linux Apps",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        text_align="center",
        width="16rem",
    )


def create_windows_platform_box():
    """Create an information box for Windows platform."""
    return rx.box(
        create_centered_icon(
            alt_text="Windows",
            icon_height="6rem",
            icon_tag="monitor",
            icon_width="6rem",
        ),
        create_custom_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text="Windows",
        ),
        create_description_text(
            description_text="Versatile apps for the world's most popular OS"
        ),
        create_hover_link(
            link_url="#windows-apps",
            link_text="Browse Windows Apps",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        text_align="center",
        width="16rem",
    )


def create_macos_platform_box():
    """Create an information box for macOS platform."""
    return rx.box(
        create_centered_icon(
            alt_text="macOS",
            icon_height="6rem",
            icon_tag="smartphone",
            icon_width="6rem",
        ),
        create_custom_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text="macOS",
        ),
        create_description_text(
            description_text="Sleek and powerful apps for Apple enthusiasts"
        ),
        create_hover_link(
            link_url="#macos-apps",
            link_text="Browse macOS Apps",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        text_align="center",
        width="16rem",
    )


def create_platforms_section():
    """Create the platforms section with platform boxes."""
    return rx.box(
        create_section_heading(heading_text="Available Platforms"),
        rx.flex(
            create_linux_platform_box(),
            create_windows_platform_box(),
            create_macos_platform_box(),
            display="flex",
            flex_wrap="wrap",
            gap="2rem",
            justify_content="center",
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


def create_featured_apps_grid():
    """Create a grid of featured app cards."""
    return rx.box(
        create_app_card(
            image_alt="TaskMaster - Advanced task management app",
            image_src="https://replicate.delivery/xezq/qcBC63Jgv8Z4Gx2kPpPQXIzvmxvJ6bYzSF7cgoX6vRPhnXeJA/out-0.webp",
            app_name="TaskMaster",
            app_description="Advanced task management with collaborative features",
        ),
        rx.box(
            create_app_image(
                alt_text="FocusTime - Pomodoro timer and productivity tracker",
                image_src="https://replicate.delivery/xezq/lfTpU4utR8SmGKQaVm5pIqFYLDv3yORIWgXgZVXoTZ1BPv8JA/out-0.webp",
            ),
            create_custom_heading(
                heading_level="h3",
                font_size="1.25rem",
                margin_bottom="0.5rem",
                heading_text="FocusTime",
            ),
            create_description_text(
                description_text="Pomodoro timer and productivity tracker"
            ),
            create_app_info_footer(platform_text="Windows, macOS"),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        create_app_card(
            image_alt="MindMap Pro - Visual brainstorming and idea organization",
            image_src="https://replicate.delivery/xezq/LOMb55DfVesRdEmtvholiY0JrSl0fkzkgTIuRntZkhXI88ynA/out-0.webp",
            app_name="MindMap Pro",
            app_description="Visual brainstorming and idea organization",
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(3, minmax(0, 1fr))",
            }
        ),
    )


def create_featured_apps_section():
    """Create the featured apps section."""
    return rx.box(
        rx.box(
            create_section_heading(heading_text="Featured Apps"),
            create_featured_apps_grid(),
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
        id="featured",
        padding_top="5rem",
        padding_bottom="5rem",
    )


def create_learn_more_button():
    """Create a styled 'Learn More' button."""
    return rx.el.a(
        "Learn More",
        href="#learn-more",
        background_color="#2563EB",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#1D4ED8"},
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_about_section():
    """Create the about section with description and call-to-action."""
    return rx.box(
        rx.heading(
            "About AppHub",
            font_weight="700",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        rx.text(
            "AppHub is your one-stop destination for discovering and downloading the best productivity apps across Linux, Windows, and macOS platforms. We curate high-quality apps to help you boost your efficiency and streamline your workflow.",
            max_width="42rem",
            margin_bottom="2rem",
            margin_left="auto",
            margin_right="auto",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_learn_more_button(),
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
    """Create the main content sections of the page."""
    return rx.box(
        rx.box(
            create_hero_section(),
            id="home",
            background_color="#2563EB",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
        rx.box(
            create_categories_section(),
            id="categories",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_platforms_section(),
            id="platforms",
            background_color="#F3F4F6",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        create_featured_apps_section(),
        rx.box(
            create_about_section(),
            id="about",
            background_color="#F3F4F6",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
    )


def create_quick_links_footer_section():
    """Create the quick links section for the footer."""
    return rx.box(
        create_custom_heading(
            heading_level="h4",
            font_size="1.125rem",
            margin_bottom="1rem",
            heading_text="Quick Links",
        ),
        rx.list(
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#home",
                link_text="Home",
            ),
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#categories",
                link_text="Categories",
            ),
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#platforms",
                link_text="Platforms",
            ),
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#about",
                link_text="About",
            ),
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
        margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
        width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
    )


def create_support_footer_section():
    """Create the support section for the footer."""
    return rx.box(
        create_custom_heading(
            heading_level="h4",
            font_size="1.125rem",
            margin_bottom="1rem",
            heading_text="Support",
        ),
        rx.list(
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#faq",
                link_text="FAQ",
            ),
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#contact",
                link_text="Contact Us",
            ),
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#privacy",
                link_text="Privacy Policy",
            ),
            create_list_item_link(
                hover_style={"color": "#ffffff"},
                text_color="#9CA3AF",
                link_url="#terms",
                link_text="Terms of Service",
            ),
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
        margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
        width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
    )


def create_footer_content():
    """Create the main content of the footer."""
    return rx.flex(
        rx.box(
            create_main_heading(
                heading_level="h3",
                font_size="1.5rem",
                line_height="2rem",
                heading_text="AppHub",
            ),
            rx.text(
                "Your source for productivity apps across platforms.",
                color="#9CA3AF",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        create_quick_links_footer_section(),
        create_support_footer_section(),
        rx.box(
            create_custom_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Connect With Us",
            ),
            rx.flex(
                create_social_link(
                    link_url="#facebook",
                    icon_alt="Facebook",
                    icon_tag="facebook",
                ),
                create_social_link(
                    link_url="#twitter",
                    icon_alt="Twitter",
                    icon_tag="twitter",
                ),
                create_social_link(
                    link_url="#linkedin",
                    icon_alt="LinkedIn",
                    icon_tag="linkedin",
                ),
                display="flex",
                column_gap="1rem",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        display="flex",
        flex_wrap="wrap",
        justify_content="space-between",
    )


def create_footer():
    """Create the complete footer section."""
    return rx.box(
        create_footer_content(),
        rx.box(
            rx.text("© 2023 AppHub. All rights reserved."),
            border_color="#374151",
            border_top_width="1px",
            margin_top="2rem",
            padding_top="2rem",
            text_align="center",
            color="#9CA3AF",
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


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        rx.box(
            create_header(),
            background_color="#ffffff",
            box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
            position="sticky",
            top="0",
            width="100%",
            z_index="10",
        ),
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="2.5rem",
            padding_bottom="2.5rem",
            color="#ffffff",
        ),
        class_name="font-['Poppins']",
        background_color="#F9FAFB",
    )


@rx.page("/home2", "Apps")
def Home2():
    """
    Create the complete app with styles and layout. 
    create_stylesheet_link(
            stylesheet_url="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        ),
    """
    return rx.fragment(
       
        create_stylesheet_link(
            stylesheet_url="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
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
