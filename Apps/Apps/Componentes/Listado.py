import reflex as rx
from . import Card
from typing import List
from Apps.Models.Llamado import Llamado


def list_item(datos : Llamado):
    return Card(datos)

#rx.foreach(listado, list_item)

def create_featured_properties_grid(listado: List[Llamado]):
    """Create a grid of featured properties with responsive layout."""
    return rx.box(
        rx.cond(listado.length() > 0, rx.foreach(listado, list_item)  , rx.text("sin datos")),
        gap="1.5rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(2, minmax(0, 1fr))",
                "1024px": "repeat(3, minmax(0, 1fr))",
            }
        ),
    )


"""
    Card(
            title="Modern House with Garden",
            details="3 bedrooms • 2 bathrooms • 150 m²",
            alt_text="Modern house with a beautiful garden",
            image_url="https://placehold.co/400x300?text=Modern+House+with+Garden",
        ),

        Card(
            title="Cozy Apartment Downtown",
            details="2 bedrooms • 1 bathroom • 80 m²",
            alt_text="Cozy apartment in the heart of downtown",
            image_url="https://placehold.co/400x300?text=Cozy+Apartment+Downtown",
        ),
        Card(
            title="Luxurious Villa with Pool",
            details="5 bedrooms • 4 bathrooms • 300 m²",
            alt_text="Luxurious villa with a large swimming pool",
            image_url="https://placehold.co/400x300?text=Luxurious+Villa+with+Pool",
        ),
        Card(
            title="Modern House with Garden",
            details="3 bedrooms • 2 bathrooms • 150 m²",
            alt_text="Modern house with a beautiful garden",
            image_url="https://placehold.co/400x300?text=Modern+House+with+Garden",
        ),
        Card(
            title="Cozy Apartment Downtown",
            details="2 bedrooms • 1 bathroom • 80 m²",
            alt_text="Cozy apartment in the heart of downtown",
            image_url="https://placehold.co/400x300?text=Cozy+Apartment+Downtown",
        ),
        Card(
            title="Luxurious Villa with Pool",
            details="5 bedrooms • 4 bathrooms • 300 m²",
            alt_text="Luxurious villa with a large swimming pool",
            image_url="https://placehold.co/400x300?text=Luxurious+Villa+with+Pool",
        ), """
