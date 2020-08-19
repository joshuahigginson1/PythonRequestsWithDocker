"""Conftest.py is used to share PyTest Fixtures across multiple test files.

Don’t import conftest into our test files. “The conftest.py file gets read 
by pytest, and is considered a local plugin.
"""
# Imports --------------------------------------------------------------

import pytest


# Fixtures -------------------------------------------------------------

@pytest.fixture(name="list_of_animals", scope='module')
def list_of_animals():
    return ["Monkey 🐵", "Wolf 🐺", "Cat 🐱", "Lion 🦁", "Tiger 🐯",
            "Unicorn 🦄", "Cow 🐮", "Pig 🐷"]


"""@pytest.fixture(name="connect_database", scope='module', autouse=False)
def tasks_db_connection(tmpdir):
        #tasks_db connects to our db before testing, then disconnects straight after.
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()"""
