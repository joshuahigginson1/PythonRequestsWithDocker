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


def return_animal_noise(animal):
    """This function returns a given animals' specific noise.
    Keyword Arguments:
        animal: A given animal.
    """

    noise_dictionary = {
        "Monkey 🐵": "Ooh Aah (Just a little bit?)",
        "Wolf 🐺": "HOWL.",
        "Cat 🐱": "Meow.",
        "Lion 🦁": "ROAR.",
        "Tiger 🐯": "Carol Baskin.",
        "Unicorn 🦄": "✨ Sparkles ✨",
        "Cow 🐮": "Moo.",
        "Pig 🐷": "Oink."
    }

    return noise_dictionary.get(animal)


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
