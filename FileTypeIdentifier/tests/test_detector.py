"""
Unit tests for detector.py
"""

from detector import detect_file_type


def test_png_detection():
    header = bytes.fromhex("89504E470D0A1A0A")
    assert detect_file_type(header) == "PNG Image"


def test_pdf_detection():
    header = bytes.fromhex("25504446")
    assert detect_file_type(header) == "PDF Document"


def test_unknown_detection():
    header = bytes.fromhex("1234567890")
    assert detect_file_type(header) == "Unknown File Type"