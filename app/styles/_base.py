from app.helpers.app_config import Config

# set the width and height of social media icons
SOCIAL_SIZE = 19

# set inverse filteration color scheme for social media icons
SOCIAL_COLOR = r"filter: brightness(0) invert(1)"

# main base css stylesheet for preconfigured web application
base_css: dict = {
    "app": {
        "font_family": Config.__theme_font__(),
    },
    "base": {
        "width": "100%",
        "min_height": "100vh",
        "spacing": "0rem",
        "padding": "0",
        "margin": "0",
    },
    "left": {
        "width": "20%",
        "top": "0",
        "position": "sticky",
        "padding_top": "5rem",
        "align_items": "start",
        "padding_left": ["", "", "", "4rem", "10rem"],
        "transition": "all 550ms ease",
    },
    "middle": {
        "width": ["100%", "100%", "100%", "60%", "60%"],
        "top": "0",
        "position": "block",
        "padding_top": ["2rem", "2rem", "2rem", "5rem", "5rem"],
        "align_items": "start",
        "padding_left": ["2rem", "2rem", "2rem", "2rem", "2rem"],
        "padding_right": ["2rem", "2rem", "2rem", "2rem", "2rem"],
        "padding_bottom": "6rem",
        "transition": "all 550ms ease",
        "min_height": "100vh",
    },
    "right": {
        "width": ["0%", "0%", "0%", "20%", "20%"],
        "top": "0",
        "position": "sticky",
        "padding_top": "5rem",
        "align_items": ["end", "end", "end", "start", "start"],
        "padding_right": ["1rem", "1rem", "1rem", "", ""],
        "transition": "all 550ms ease",
    },
    "header": {
        "main": {
            "width": "100%",
            "height": "50px",
            "position": "sticky",
            "bg": Config.__theme_primary__(),
            "box_shadow": "0 3px 6px 0 rgba(0, 0, 0, 0.5)",
            "transition": "height 350ms ease",
            "top": "0",
            "z_index": "2",
        },
        "icon": {
            "font_size": "xl",
            "cursor": "pointer",
            "color": "white",
        },
        "navigation": {
            "align_items": "end",
            "transition": "opacity 500ms ease 500ms",
        },
        "link_text": {
            "size": "s",
            "padding_top": "0.3rem",
            "color": "white",
            "font_weight": "semibold",
        },
        "site_name": {
            "font_size": ["100%", "115%", "130%", "135%", "150%"],
            "color": "white",
            "transition": "all 550ms ease",
            "opacity": "1",
            "_hover": {"opacity": "0.85"},
            "padding_right": "3.5rem",
        },
        "max_header": {
            "width": "100%",
            "padding_left": ["", "", "", "4rem", "10rem"],
            "padding_right": ["", "", "", "4rem", "10rem"],
            "transition": "all 550ms ease",
        },
        "min_header": {
            "width": "100%",
            "padding_left": ["1rem", "1rem", "0.5rem", "", ""],
            "padding_right": ["1rem", "1rem", "0.5rem", "", ""],
            "transition": "all 550ms ease",
        },
    },
    "footer": {
        "style": {
            "width": "100%",
            "height": ["105px", "75px", "65px", "65px", "65px"],
            "position": "sticky",
            "bg": "#15171b",
            "transition": "height 350ms ease",
            "top": "0",
            "overflow": "hidden",
        },
        "socials": {
            "github": f"<img width='{SOCIAL_SIZE}' height='{SOCIAL_SIZE}' src='https://img.icons8.com/material-outlined/24/github.png' style='{SOCIAL_COLOR}';/>",  # noqa: E501
            "twitter": f"<img width='{SOCIAL_SIZE}' height='{SOCIAL_SIZE}' src='https://img.icons8.com/ios-filled/24/twitter.png' style='{SOCIAL_COLOR}';/>",  # noqa: E501
            "youtube": f"<img width='{SOCIAL_SIZE}' height='{SOCIAL_SIZE}' src='https://img.icons8.com/ios-filled/24/youtube.png' style='{SOCIAL_COLOR}';/>",  # noqa: E501
            "mastodon": f"<img width='{SOCIAL_SIZE}' height='{SOCIAL_SIZE}' src='https://img.icons8.com/windows/24/mastodon.png' style='{SOCIAL_COLOR}';/>",  # noqa: E501
            "discord": f"<img width='{SOCIAL_SIZE}' height='{SOCIAL_SIZE}' src='https://img.icons8.com/ios-filled/24/discord.png' style='{SOCIAL_COLOR}';/>",  # noqa: E501
        },
    },
    "drawer": {
        "heading": {
            "width": "100%",
            "height": "100px",
            "align_items": "end",
            "bg": Config.__theme_primary__(),
            "padding_left": "1rem",
            "padding_bottom": "1rem",
            "transition": "all 550ms ease",
            "color": "white",
        },
        "repo": {
            "width": "100%",
            "height": "45px",
            "bg": Config.__theme_primary__(),
            "padding_left": "1rem",
            "transition": "all 550ms ease",
        },
        "router": {
            "align_items": "center",
            "width": "100%",
            "cursor": "pointer",
            "opacity": "0.8",
            "_hover": {"opacity": "1"},
        },
    },
}
