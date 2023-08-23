FONT_H1 = [f"{56 * size}px" for size in [0.70, 0.80, 0.80, 0.90, 1]]
FONT_H2 = [f"{45 * size}px" for size in [0.70, 0.80, 0.80, 0.90, 1]]
FONT_H3 = [f"{34 * size}px" for size in [0.70, 0.80, 0.80, 0.90, 1]]


markdown_css: dict = {
    "h1": {
        "font_size": FONT_H1,
        "font_weight": "400",
        "line_height": "1.35",
        "letter_spacing": "-0.02em",
        "margin_bottom": "24px",
        "margin": "0",
        "padding": "0",
        "transition": "all 550ms ease",
    },
    "h2": {
        "font_size": FONT_H2,
        "font_weight": "400",
        "line_height": "48px",
        "margin_top": "24px",
        "margin_bottom": "24px",
        "margin": "0",
        "padding": "0",
        "transition": "all 550ms ease",
    },
    "h3": {
        "font_size": FONT_H3,
        "font_weight": "400",
        "line_height": "40px",
        "margin_top": "24px",
        "margin_bottom": "24px",
        "margin": "0",
        "padding": "0",
        "transition": "all 550ms ease",
    },
    "p": {
        "font_size": "14px",
        "font_weight": "400",
        "line_height": "24px",
        "letter_spacing": "0",
        "margin_bottom": "16px",
        "margin": "0",
        "padding": "0",
        "transition": "all 550ms ease",
    },
}
