import reflex as rx

config = rx.Config(
    app_name="Apps",
    frontend_path="/Apps", 
    tailwind={
        "content": [
            "./pages/**/*.{js,ts,jsx,tsx}",
            "./utils/**/*.{js,ts,jsx,tsx}",
            "./luis/**/*.{js,ts,jsx,tsx}",
        ]
    },
)

"""
frontend_path="/Apps", 
deploy_url="https://luiss1991.github.io"
reflex export --frontend-only

"content": [
            "./pages/**/*.{js,ts,jsx,tsx}",
            "./utils/**/*.{js,ts,jsx,tsx}",
            "./luis/**/*.{js,ts,jsx,tsx}",
        ]


"""
