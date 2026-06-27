"""
validator.py

This module validates the file before it is processed.
"""

import os


def validate_file(file_path):
    """
    Validate the selected file.

    Checks:
    - File path is not empty
    - File exists
    - Path is a file (not a directory)
    - File is not empty
    - File is readable

    Returns:
        True if valid, False otherwise.
    """

    # Check empty input
    if not file_path.strip():
        print("[ERROR] No file path provided.")
        return False

    # Check file exists
    if not os.path.exists(file_path):
        print("[ERROR] File does not exist.")
        return False

    # Check if it is actually a file
    if not os.path.isfile(file_path):
        print("[ERROR] The given path is not a file.")
        return False

    # Check file size
    if os.path.getsize(file_path) == 0:
        print("[ERROR] File is empty.")
        return False

    # Check read permission
    if not os.access(file_path, os.R_OK):
        print("[ERROR] File cannot be read.")
        return False

    return True


def is_supported_extension(file_path):
    """
    Check whether the file extension is known.

    This is only for display purposes.
    Detection is still based on magic bytes.
    """

    supported_extensions = {
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".zip",
        ".rar",
        ".7z",
        ".exe",
        ".mp3",
        ".wav",
        ".ogg",
        ".mp4",
        ".avi",
        ".mkv",
        ".db",
        ".sqlite"
    }

    extension = os.path.splitext(file_path)[1].lower()

    return extension in supported_extensions


def get_extension(file_path):
    """
    Return the file extension.

    Example:
    image.png -> .png
    """

    return os.path.splitext(file_path)[1].lower()


def print_validation_result(file_path):
    """
    Print validation information.
    """

    print("\n========== Validation ==========")
    print(f"File Exists      : {os.path.exists(file_path)}")
    print(f"Readable         : {os.access(file_path, os.R_OK)}")
    print(f"Extension        : {get_extension(file_path)}")
    print(f"Supported        : {is_supported_extension(file_path)}")
    print("================================")