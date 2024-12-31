from reflex import heading


def create_subheading(text):
    """Create a subheading with specific styling."""
    return heading(
        text,
        font_weight="700",
        margin_bottom="0.5rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )
