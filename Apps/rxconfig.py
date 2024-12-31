import reflex as rx

config = rx.Config(
    app_name="Apps",
    tailwind={},
)

"""
frontend_path="/Apps", 
deploy_url="https://luiss1991.github.io",
cp_web_url="https://luiss1991.github.io/",
reflex export --frontend-only
"content": [
            "./pages/**/*.{js,ts,jsx,tsx}",
            "./utils/**/*.{js,ts,jsx,tsx}",
            "./luis/**/*.{js,ts,jsx,tsx}",
        ]

stylesheets=[
        "/fonts/myfont.css",  # This path is relative to assets/
    ],
"""
