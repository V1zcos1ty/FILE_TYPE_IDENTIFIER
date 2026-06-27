"""
detector.py

Compares a file's magic bytes with known file signatures
to determine the actual file type.
"""

from signatures import FILE_SIGNATURES


def detect_file_type(file_header):
    """
    Detect file type using magic bytes.

    Args:
        file_header (bytes): First bytes read from the file.

    Returns:
        str: Detected file type.
    """

    # Convert bytes to uppercase hexadecimal string
    hex_header = file_header.hex().upper()

    # Check every known signature
    for signature, file_type in FILE_SIGNATURES.items():

        if hex_header.startswith(signature):
            return file_type

    return "Unknown File Type"


def is_known_file(file_header):
    """
    Returns True if the file signature is recognized.
    """

    hex_header = file_header.hex().upper()

    for signature in FILE_SIGNATURES:

        if hex_header.startswith(signature):
            return True

    return False


def get_file_signature(file_header):
    """
    Returns the hexadecimal signature read from the file.
    """

    return file_header.hex().upper()


def print_detection_result(file_type):
    """
    Print detection result in a readable format.
    """

    print("\n========== Detection Result ==========")
    print(f"Detected File Type : {file_type}")
    print("======================================")