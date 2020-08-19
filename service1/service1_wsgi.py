"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from service1.src import service1


# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service1.run(port=5000)

