"""Serving our service 2 entry point."""

# Imports --------------------------------------------------------------

from flask import Flask

service2 = Flask(__name__)





# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service2.run(port=5001)
