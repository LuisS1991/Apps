import reflex as rx



class Hello(rx.Component):
    library = "../luis/Hello"
    tag = "Hello"


HelloReact = Hello.create


@rx.page("/pokemon", "Apps")
def React() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.center(
            rx.vstack(
                rx.box(
                    rx.heading("Reflex con React js", class_name="text-center mt-6"),
                    class_name="w-full",
                ),
                HelloReact(),
            )
        ),
        class_name="w-full bg-green-300",
    )
