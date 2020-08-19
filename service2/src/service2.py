"""Contains all of the functions to run service 2."""

# Imports --------------------------------------------------------------

import random

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------

def return_animal():
    """This function returns a random animal used with a route GET request."""

    animal_list = ["Monkey 🐵", "Wolf 🐺", "Cat 🐱", "Lion 🦁", "Tiger 🐯",
                   "Unicorn 🦄", "Cow 🐮", "Pig 🐷"]

    return random.choice(animal_list)


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
