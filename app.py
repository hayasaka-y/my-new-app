from flask import Flask, jsonify
from werkzeug.wrappers.response import Response

app = Flask(__name__)


@app.route("/")
def hello_world() -> Response:
    """Return a simple greeting message."""
    return jsonify(message="Hello, world!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
