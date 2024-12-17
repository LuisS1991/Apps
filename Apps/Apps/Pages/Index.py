import reflex as rx


@rx.page("/", "Apps")
def Index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.center(
            rx.vstack(
                rx.box(
                    rx.heading("Reflex", class_name="text-center mt-6"),
                    class_name="w-full",
                ),
                rx.logo(),
            )
        ),
        class_name="w-full bg-green-300",
    )
