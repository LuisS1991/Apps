from reflex import heading


def create_section_heading(text):
    """Create a section heading with specific styling."""
    return heading(
        text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        as_="h2",
    )
