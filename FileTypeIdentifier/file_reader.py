"""
file_reader.py

This module is responsible for reading the first few bytes
(header/magic bytes) of a file.
"""

import os
from config import HEADER_SIZE


def read_file_header(file_path):
    """
    Reads the first HEADER_SIZE bytes from a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        bytes: The header bytes of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If access to the file is denied.
        IOError: If the file cannot be read.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not os.path.isfile(file_path):
        raise ValueError(f"'{file_path}' is not a valid file.")

    try:
        with open(file_path, "rb") as file:
            header = file.read(HEADER_SIZE)
            return header

    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")

    except Exception as e:
        raise IOError(f"Error reading file: {e}")


def get_file_size(file_path):
    """
    Returns the file size in bytes.

    Args:
        file_path (str): Path to the file.

    Returns:
        int: File size in bytes.
    """
    return os.path.getsize(file_path)


def get_file_name(file_path):
    """
    Returns only the file name.

    Example:
        /Users/Akshat/Desktop/image.png
        ↓
        image.png
    """
    return os.path.basename(file_path)


def get_file_extension(file_path):
    """
    Returns the file extension.

    Example:
        image.png
        ↓
        .png
    """
    return os.path.splitext(file_path)[1].lower()


def read_entire_file(file_path):
    """
    Reads the complete file in binary mode.

    Useful for future features like:
    - Hash generation
    - Entropy analysis
    - Malware detection

    Returns:
        bytes
    """
    with open(file_path, "rb") as file:
        return file.read()