from flask import Flask, jsonify


app = Flask(__name__)

data: dict = {
    "site_name": {
        "type": "string",
        "*": "not required",
    },
    "repo_name": {
        "type": "string",
        "*": "not required",
    },
    "repo_url": {
        "type": "string (URL format)",
        "*": "not required",
    },
    "copy_right": {
        "type": "string",
        "*": "not required",
    },
    "attribute": {
        "type": "string",
        "*": "not required",
    },
    "theme": {
        "primary": {
            {
                "type": "string",
                "*": "required",
            },
        },
        "secondary": {
            "type": "string",
            "*": "required",
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
        "type": "string",
        "*": "not required",
    },
    "navigation": ["Single file or single-level sub-directory", "Not required"],
}


@app.route("/reflexify")
def home():
    return jsonify(data)
