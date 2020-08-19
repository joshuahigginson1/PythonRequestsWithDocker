"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from flask import render_template
from service1.src import service1

# Routes ---------------------------------------------------------------


@service1.route("/", methods=['GET'])
def homepage():
    """Returns our homepage for the Animal Style App."""
    return render_template("homepage.html",
                           title="🐳 ~ Animal Style ~ 🐳")


@service1.route("/generate", methods=['GET', 'POST'])
def generate_page():
    """Returns our generate page for the Animal Style App."""
    return render_template("generate_page.html",
                           title="🐋 ~ Generate! ~ 🐋")


