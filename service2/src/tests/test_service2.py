"""A script to test the functionality of service2."""

# Imports --------------------------------------------------------------

import pytest
from unittest.mock import patch

from service2.src.service2 import return_animal

# Classes --------------------------------------------------------------


# Tests ----------------------------------------------------------------


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
    assert False

# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
