"""
utils.py

Utility functions used throughout the File Type Identification project.
"""

import os
import json
from datetime import datetime


def bytes_to_hex(data):
    """
    Convert bytes to uppercase hexadecimal string.

    Args:
        data (bytes)

    Returns:
        str
    """
    return data.hex().upper()


def get_timestamp():
    """
    Return current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_file_size(size):
    """
    Convert bytes into KB, MB, GB.

    Example:
    1024 -> 1.00 KB
    """

    for unit in ["Bytes", "KB", "MB", "GB", "TB"]:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


def save_json_report(data, filename="output/report.json"):
    """
    Save scan result as JSON.
    """

    os.makedirs("output", exist_ok=True)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def print_separator():
    """
    Print a separator line.
    """

    print("=" * 50)


def print_title(title):
    """
    Print a formatted title.
    """

    print_separator()
    print(title.center(50))
    print_separator()


def print_success(message):
    """
    Print success message.
    """

    print(f"[SUCCESS] {message}")


def print_warning(message):
    """
    Print warning message.
    """

    print(f"[WARNING] {message}")


def print_error(message):
    """
    Print error message.
    """

    print(f"[ERROR] {message}")


def create_result(filename, extension, detected_type, status):
    """
    Create a dictionary for JSON report.
    """

    return {
        "filename": filename,
        "extension": extension,
        "detected_type": detected_type,
        "status": status,
        "timestamp": get_timestamp()
    }