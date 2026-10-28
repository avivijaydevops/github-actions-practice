
"""Flask application with a home page and health-check endpoint."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Render the home page."""
    return render_template("index.html")

if ee:
    fe


@app.route("/health")
def health():
    """Return the application health status."""
    return "Server is up and running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
