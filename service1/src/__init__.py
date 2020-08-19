"""This file initialises our service1 app."""

# Imports --------------------------------------------------------------
from flask import Flask

# Create Flask App -----------------------------------------------------

service1 = Flask(__name__)

# Routes ---------------------------------------------------------------

from service1.src import service1_routes
