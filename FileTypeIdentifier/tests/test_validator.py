"""
Unit tests for validator.py
"""

import os
from validator import validate_file


def test_valid_file():

    test_file = "temp_test.txt"

    with open(test_file, "w") as file:
        file.write("Testing")

    assert validate_file(test_file) is True

    os.remove(test_file)


def test_invalid_file():

    assert validate_file("does_not_exist.txt") is False