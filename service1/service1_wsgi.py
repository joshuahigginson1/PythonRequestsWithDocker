"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from flask import Flask

service1 = Flask(__name__)


# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service1.run(port=5000)
