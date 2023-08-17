from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "site_name": {
        "type": "string",
        "required": False,
    },
    "repo_name": {
        "type": "string",
        "required": False,
    },
    "repo_url": {
        "type": "string (URL format)",
        "required": False,
    },
    "copy_right": {
        "type": "string",
        "required": False,
    },
    "attribute": {
        "type": "string",
        "required": False,
    },
    "drawer": {
        "type": "bool",
        "required": False,
        "description": "Removes side drawer from app if True. Note: turn off drawer (set to True) if app is static.",
    },
    "theme": {
        "primary": {
            "type": "string",
            "required": True,
        },
        "secondary": {
            "type": "string",
            "required": True,
        },
        "font": {
            "type": "string",
            "required": False,
        },
    },
    "socials": {
        "key_names": [
            "github",
            "twitter",
            "youtube",
            "mastodon",
            "discord",
        ],
        "value": "url of corresponding social media account.",
        "type": "string",
        "required": False,
    },
    "navigation": {
        "description": "Single file or single-level sub-directory. Must have home:index.py key:value pair. Cannot have values with same name.",
        "required": True,
    },
}


@app.route("/")
def home():
    return jsonify(data)
