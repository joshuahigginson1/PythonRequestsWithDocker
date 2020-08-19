"""A script to test the functionality of service2."""

# Imports --------------------------------------------------------------

import pytest
from unittest.mock import patch

from service2.src.service2 import return_animal, return_animal_noise


# Classes --------------------------------------------------------------


# Test GET requests ----------------------------------------------------


def test_return_animal(list_of_animals):
    """This test checks to see if a random animal is returned.
    Keyword Arguments:
        list_of_animals: Our list of animals, mocked in conftest.
        """

    random_animal = return_animal()

    assert random_animal in list_of_animals
    assert isinstance(random_animal, str)


def test_on_get_request():
    """This test checks the functionality of the get request. """
    # TODO
    assert False

# Test POST requests ---------------------------------------------------


def test_return_animal_noise(list_of_animals, dict_of_noises):
    """This test check to to see if our animal noise function operates
    correctly.
    Keyword Arguments:
        list_of_animals: Our list of animals, mocked in conftest..
        dict_of_noises: Our dict of noises, mocked in conftest.
    """

    for animal in list_of_animals:
        noise = dict_of_noises.get(animal)

        assert return_animal_noise(animal) == noise
        assert isinstance(return_animal_noise(animal), str)

    assert return_animal_noise("Cow 🐮") == "Moo."
    assert return_animal_noise("Pig 🐷") == "Oink."


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
