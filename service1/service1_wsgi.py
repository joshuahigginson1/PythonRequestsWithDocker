"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from src.service1_initialise import service1


# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service1.run(port=5000)

