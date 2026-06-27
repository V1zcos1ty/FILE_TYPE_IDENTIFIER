"""
Unit tests for file_reader.py
"""

import os
from file_reader import read_file_header


def test_read_file_header():

    test_file = "temp_test.txt"

    with open(test_file, "wb") as file:
        file.write(b"Hello World")

    header = read_file_header(test_file)

    assert header.startswith(b"Hello")

    os.remove(test_file)