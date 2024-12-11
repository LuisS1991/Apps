import reflex as rx


def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def create_styled_link(hover_style, text_color, link_url, link_text):
    """Create a styled anchor element."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover=hover_style,
        color=text_color,
    )


def create_list_item_with_link(hover_style, text_color, link_url, link_text):
    """Create a list item containing a styled link."""
    return rx.el.li(
        create_styled_link(
            hover_style=hover_style,
            text_color=text_color,
            link_url=link_url,
            link_text=link_text,
        )
    )


def create_styled_heading(heading_level, font_size, margin_bottom, heading_text):
    """Create a styled heading element."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_=heading_level,
    )


def create_large_heading(heading_level, font_size, line_height, heading_text):
    """Create a large, bold heading element."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="1rem",
        font_size=font_size,
        line_height=line_height,
        as_=heading_level,
    )


def create_large_paragraph(paragraph_text):
    """Create a large paragraph element with specific styling."""
    return rx.text(
        paragraph_text,
        margin_bottom="2rem",
        font_size="1.25rem",
        line_height="1.75rem",
    )


def create_centered_section_heading(heading_text):
    """Create a centered, large heading for a section."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_feature_icon(alt_text, icon_name):
    """Create an icon element for a feature."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="3rem",
        margin_bottom="1rem",
        color="#7C3AED",
        width="3rem",
    )


def create_colored_text(text_color, content):
    """Create a text element with a specific color."""
    return rx.text(content, color=text_color)


def create_feature_box(
    icon_alt_text,
    icon_name,
    feature_title,
    feature_description,
):
    """Create a box containing a feature's icon, title, and description."""
    return rx.box(
        create_feature_icon(alt_text=icon_alt_text, icon_name=icon_name),
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=feature_title,
        ),
        create_colored_text(
            text_color="#4B5563",
            content=feature_description,
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_product_image(alt_text, image_url):
    """Create an image element for a product."""
    return rx.image(
        alt=alt_text,
        src=image_url,
        height="12rem",
        margin_bottom="1rem",
        object_fit="cover",
        border_radius="0.25rem",
        width="100%",
    )


def create_gray_paragraph(paragraph_text):
    """Create a paragraph element with gray text."""
    return rx.text(
        paragraph_text,
        margin_bottom="1rem",
        color="#4B5563",
    )


def create_learn_more_link():
    """Create a 'Learn More' link with specific styling."""
    return rx.el.a(
        "Learn More →",
        href="#learnmore",
        font_weight="600",
        _hover={"color": "#6D28D9"},
        color="#7C3AED",
    )


def create_product_card(
    image_alt_text,
    image_url,
    product_name,
    product_description,
):
    """Create a card displaying a product's image, name, and description."""
    return rx.box(
        create_product_image(alt_text=image_alt_text, image_url=image_url),
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=product_name,
        ),
        create_gray_paragraph(paragraph_text=product_description),
        create_learn_more_link(),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_avatar_image(alt_text, image_url):
    """Create a circular avatar image."""
    return rx.image(
        alt=alt_text,
        src=image_url,
        height="3rem",
        margin_right="1rem",
        border_radius="9999px",
        width="3rem",
    )


def create_bold_text(text_content):
    """Create a bold text element."""
    return rx.text(text_content, font_weight="600")


def create_small_gray_text(text_content):
    """Create a small, gray text element."""
    return rx.text(
        text_content,
        color="#6B7280",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_name_and_title(name, title):
    """Create a box with a name in bold and a title in small, gray text."""
    return rx.box(
        create_bold_text(text_content=name),
        create_small_gray_text(text_content=title),
    )


def create_testimonial_author(avatar_alt_text, avatar_url, author_name, author_title):
    """Create a flex container with an avatar and author information."""
    return rx.flex(
        create_avatar_image(alt_text=avatar_alt_text, image_url=avatar_url),
        create_name_and_title(name=author_name, title=author_title),
        display="flex",
        align_items="center",
    )


def create_per_month_text():
    """Create a '/month' text span with specific styling."""
    return rx.text.span(
        "/month",
        font_weight="400",
        font_size="1rem",
        line_height="1.5rem",
        color="#6B7280",
    )


def create_price_display(price):
    """Create a price display with a '/month' suffix."""
    return rx.text(
        price,
        create_per_month_text(),
        font_weight="700",
        margin_bottom="1rem",
        font_size="1.875rem",
        line_height="2.25rem",
    )


def create_check_icon():
    """Create a check icon for feature lists."""
    return rx.icon(
        alt="Check",
        tag="check",
        height="1.25rem",
        margin_right="0.5rem",
        color="#10B981",
        width="1.25rem",
    )


def create_text_span(text_content):
    """Create a simple text span."""
    return rx.text.span(text_content)


def create_feature_list_item(feature_text):
    """Create a list item with a check icon and feature text."""
    return rx.el.li(
        create_check_icon(),
        create_text_span(text_content=feature_text),
        display="flex",
        align_items="center",
        margin_bottom="0.5rem",
    )


def create_cta_button(button_url, button_text):
    """Create a call-to-action button with specific styling."""
    return rx.el.a(
        button_text,
        href=button_url,
        background_color="#7C3AED",
        display="block",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#6D28D9"},
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        text_align="center",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )


def create_feature_list(feature1, feature2, feature3, feature4):
    """Create a list of features with check icons."""
    return rx.list(
        create_feature_list_item(feature_text=feature1),
        create_feature_list_item(feature_text=feature2),
        create_feature_list_item(feature_text=feature3),
        create_feature_list_item(feature_text=feature4),
        margin_bottom="1.5rem",
    )


def create_footer_link_list(link1_text, link2_text, link3_text):
    """Create a list of footer links with specific styling."""
    return rx.list(
        create_list_item_with_link(
            hover_style={"color": "#ffffff"},
            text_color="#9CA3AF",
            link_url="#",
            link_text=link1_text,
        ),
        create_list_item_with_link(
            hover_style={"color": "#ffffff"},
            text_color="#9CA3AF",
            link_url="#",
            link_text=link2_text,
        ),
        create_list_item_with_link(
            hover_style={"color": "#ffffff"},
            text_color="#9CA3AF",
            link_url="#",
            link_text=link3_text,
        ),
        display="flex",
        flex_direction="column",
        gap="0.5rem",
    )


def create_footer_section(section_title, link1_text, link2_text, link3_text):
    """Create a footer section with a title and links."""
    return rx.box(
        create_styled_heading(
            heading_level="h4",
            font_size="1.125rem",
            margin_bottom="1rem",
            heading_text=section_title,
        ),
        create_footer_link_list(
            link1_text=link1_text,
            link2_text=link2_text,
            link3_text=link3_text,
        ),
        margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
        width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
    )


def create_social_icon(icon_alt_text, icon_name):
    """Create a social media icon."""
    return rx.icon(
        alt=icon_alt_text,
        tag=icon_name,
        height="1.5rem",
        width="1.5rem",
    )


def create_social_link(icon_alt_text, icon_name):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_social_icon(icon_alt_text=icon_alt_text, icon_name=icon_name),
        href="#",
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
    )


def create_signup_button():
    """Create a 'Sign Up' button with specific styling."""
    return rx.el.a(
        "Sign Up",
        href="#signup",
        background_color="#7C3AED",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#6D28D9"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_header():
    """Create the main header with logo, navigation, and sign-up button."""
    return rx.flex(
        rx.box(
            "AppHub",
            font_weight="700",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#7C3AED",
        ),
        rx.list(
            create_list_item_with_link(
                hover_style={"color": "#7C3AED"},
                text_color="#374151",
                link_url="#features",
                link_text="Features",
            ),
            create_list_item_with_link(
                hover_style={"color": "#7C3AED"},
                text_color="#374151",
                link_url="#products",
                link_text="Products",
            ),
            create_list_item_with_link(
                hover_style={"color": "#7C3AED"},
                text_color="#374151",
                link_url="#testimonials",
                link_text="Testimonials",
            ),
            create_list_item_with_link(
                hover_style={"color": "#7C3AED"},
                text_color="#374151",
                link_url="#pricing",
                link_text="Pricing",
            ),
            display=rx.breakpoints({"0px": "none", "768px": "flex"}),
            column_gap="1.5rem",
        ),
        create_signup_button(),
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


def create_hero_cta():
    """Create the hero section call-to-action button."""
    return rx.el.a(
        "Start Free Trial",
        href="#signup",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#EDE9FE"},
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        color="#7C3AED",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_hero_section():
    """Create the hero section with heading, subtext, and CTA."""
    return rx.box(
        create_large_heading(
            heading_level="h1",
            font_size=rx.breakpoints({"0px": "2.25rem", "768px": "3.75rem"}),
            line_height=rx.breakpoints({"0px": "2.5rem", "768px": "1"}),
            heading_text="Boost Your Productivity with AppHub",
        ),
        create_large_paragraph(
            paragraph_text="All-in-one solution for task management, team collaboration, and workflow optimization"
        ),
        create_hero_cta(),
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


def create_features_section():
    """Create the features section with title and feature boxes."""
    return rx.box(
        create_centered_section_heading(heading_text="Why Choose AppHub?"),
        rx.box(
            create_feature_box(
                icon_alt_text="Seamless Integration",
                icon_name="layers",
                feature_title="Seamless Integration",
                feature_description="Connect all your favorite tools and work seamlessly across platforms.",
            ),
            create_feature_box(
                icon_alt_text="Real-time Collaboration",
                icon_name="users",
                feature_title="Real-time Collaboration",
                feature_description="Work together with your team in real-time, no matter where you are.",
            ),
            create_feature_box(
                icon_alt_text="Advanced Analytics",
                icon_name="bar-chart",
                feature_title="Advanced Analytics",
                feature_description="Gain insights into your productivity and optimize your workflow.",
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
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_products_section():
    """Create the products section with title and product cards."""
    return rx.box(
        create_centered_section_heading(heading_text="Our Products"),
        rx.box(
            create_product_card(
                image_alt_text="TaskMaster - Powerful task management app",
                image_url="https://replicate.delivery/xezq/6N14f167AOXrVagUosUSmuMAsjDPtaPcm5pmBGu71ahYFv8JA/out-0.webp",
                product_name="TaskMaster",
                product_description="Powerful task management app to keep you organized and focused.",
            ),
            create_product_card(
                image_alt_text="TeamSync - Collaborative workspace for teams",
                image_url="https://replicate.delivery/xezq/sqeQuOo7L1yVZ6MQcCIvUceYsSY2vnEwykb1wSY4W69xKeynA/out-0.webp",
                product_name="TeamSync",
                product_description="Collaborative workspace for teams to communicate and share ideas.",
            ),
            create_product_card(
                image_alt_text="TimeTrack - Time tracking and productivity analysis",
                image_url="https://replicate.delivery/xezq/JZn1j2aUu9JXGZi0fwTYVZUbivfOPVG196yEpRgHIDZwKeynA/out-0.webp",
                product_name="TimeTrack",
                product_description="Time tracking and productivity analysis to optimize your workflow.",
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
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_testimonials_grid():
    """Create a grid of testimonials."""
    return rx.box(
        rx.box(
            create_gray_paragraph(
                paragraph_text='"AppHub has transformed the way our team works. We\'re more productive and aligned than ever before."'
            ),
            create_testimonial_author(
                avatar_alt_text="Sarah Johnson, CEO of TechInnovate",
                avatar_url="https://replicate.delivery/xezq/vN0AIgwPK7ZWFdFD46qtwVqCm1mCeIzYEc7Yy7erLFuxKeynA/out-0.webp",
                author_name="Sarah Johnson",
                author_title="CEO, TechInnovate",
            ),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        rx.box(
            create_gray_paragraph(
                paragraph_text='"The suite of apps from AppHub has streamlined our processes and boosted our team\'s efficiency by 40%."'
            ),
            create_testimonial_author(
                avatar_alt_text="Mark Thompson, CTO of AgileWorks",
                avatar_url="https://replicate.delivery/xezq/m0dBQ6GfCPSBcK1duze9mDe7JncewP95ubzL6nmoDIVFr4lPB/out-0.webp",
                author_name="Mark Thompson",
                author_title="CTO, AgileWorks",
            ),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(2, minmax(0, 1fr))",
            }
        ),
    )


def create_testimonials_section():
    """Create the testimonials section with title and testimonial grid."""
    return rx.box(
        rx.box(
            create_centered_section_heading(heading_text="What Our Customers Say"),
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
        id="testimonials",
        padding_top="5rem",
        padding_bottom="5rem",
    )


def create_basic_plan_card():
    """Create a pricing card for the Basic plan."""
    return rx.box(
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text="Basic",
        ),
        create_price_display(price="$9"),
        rx.list(
            create_feature_list_item(feature_text="1 App of your choice"),
            create_feature_list_item(feature_text="Basic support"),
            create_feature_list_item(feature_text="1 GB storage"),
            margin_bottom="1.5rem",
        ),
        create_cta_button(button_url="#signup", button_text="Choose Basic"),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_pro_plan_card():
    """Create a pricing card for the Pro plan."""
    return rx.box(
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text="Pro",
        ),
        create_price_display(price="$29"),
        create_feature_list(
            feature1="All Apps",
            feature2="Priority support",
            feature3="10 GB storage",
            feature4="Advanced analytics",
        ),
        create_cta_button(button_url="#signup", button_text="Choose Pro"),
        background_color="#ffffff",
        border_width="2px",
        border_color="#7C3AED",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_enterprise_plan_card():
    """Create a pricing card for the Enterprise plan."""
    return rx.box(
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text="Enterprise",
        ),
        rx.text(
            "Custom",
            font_weight="700",
            margin_bottom="1rem",
            font_size="1.875rem",
            line_height="2.25rem",
        ),
        create_feature_list(
            feature1="All Pro features",
            feature2="24/7 dedicated support",
            feature3="Unlimited storage",
            feature4="Custom integrations",
        ),
        create_cta_button(
            button_url="#contact",
            button_text="Contact Sales",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_pricing_section():
    """Create the pricing section with title and plan cards."""
    return rx.box(
        create_centered_section_heading(heading_text="Simple, Transparent Pricing"),
        rx.box(
            create_basic_plan_card(),
            create_pro_plan_card(),
            create_enterprise_plan_card(),
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
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_email_input():
    """Create an email input field with specific styling."""
    return rx.el.input(
        placeholder="Enter your email",
        type="email",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "border-color": "#8B5CF6",
            "outline-style": "none",
        },
        margin_bottom="1rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        width="100%",
    )


def create_get_started_button():
    """Create a 'Get Started' submit button with specific styling."""
    return rx.el.button(
        "Get Started",
        type="submit",
        background_color="#7C3AED",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#6D28D9"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )


def create_signup_section():
    """Create the sign-up section with title, subtext, and form."""
    return rx.box(
        rx.heading(
            "Ready to Supercharge Your Productivity?",
            font_weight="700",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        create_large_paragraph(
            paragraph_text="Start your free 14-day trial now. No credit card required."
        ),
        rx.form(
            create_email_input(),
            create_get_started_button(),
            max_width="28rem",
            margin_left="auto",
            margin_right="auto",
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
        text_align="center",
    )


def create_main_content():
    """Create the main content of the page, including all sections."""
    return rx.box(
        rx.box(
            create_hero_section(),
            background_color="#7C3AED",
            margin_top="4rem",
            padding_top="8rem",
            padding_bottom="8rem",
            color="#ffffff",
        ),
        rx.box(
            create_features_section(),
            id="features",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_products_section(),
            id="products",
            background_color="#F3F4F6",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        create_testimonials_section(),
        rx.box(
            create_pricing_section(),
            id="pricing",
            background_color="#F3F4F6",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_signup_section(),
            id="signup",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
    )


def create_footer_content():
    """Create the main content of the footer, including all sections."""
    return rx.flex(
        rx.box(
            create_large_heading(
                heading_level="h3",
                font_size="1.5rem",
                line_height="2rem",
                heading_text="AppHub",
            ),
            create_colored_text(
                text_color="#9CA3AF",
                content="Empowering productivity through innovative applications.",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        create_footer_section(
            section_title="Products",
            link1_text="TaskMaster",
            link2_text="TeamSync",
            link3_text="TimeTrack",
        ),
        create_footer_section(
            section_title="Company",
            link1_text="About Us",
            link2_text="Careers",
            link3_text="Contact",
        ),
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Connect With Us",
            ),
            rx.flex(
                create_social_link(
                    icon_alt_text="Facebook",
                    icon_name="facebook",
                ),
                create_social_link(
                    icon_alt_text="Twitter",
                    icon_name="twitter",
                ),
                create_social_link(
                    icon_alt_text="LinkedIn",
                    icon_name="linkedin",
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
    """Create the complete footer with content and copyright notice."""
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


@rx.page("/home", "Apps")
def Home():
    """
    Create the complete page including styles, fonts, and all content.
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
