"""Serving our service 2 entry point."""

# Imports --------------------------------------------------------------

from service2.src.service2 import return_animal

from flask import Flask, Response

# Create Flask App -----------------------------------------------------

service2 = Flask(__name__)


# Routes ---------------------------------------------------------------

@service2.route("/animal", methods=["GET"])
def on_get_request():
    """This function triggers on every GET request to the chosen url."""
    return Response(return_animal(), mimetype='text/plain')


# Run our App ----------------------------------------------------------


if __name__ == "__main__":
    service2.run(port=5001)
