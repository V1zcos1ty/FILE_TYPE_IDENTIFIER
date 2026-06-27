"""
logger.py

Handles logging for the File Type Identification project.
"""

import os
import logging

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="output/log.txt",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def log_info(message):
    """
    Log an informational message.
    """
    logging.info(message)


def log_warning(message):
    """
    Log a warning message.
    """
    logging.warning(message)


def log_error(message):
    """
    Log an error message.
    """
    logging.error(message)


def log_detection(filename, detected_type):
    """
    Log a successful file detection.
    """
    logging.info(
        f"File: {filename} | Detected Type: {detected_type}"
    )


def log_start():
    """
    Log program startup.
    """
    logging.info("========== Program Started ==========")


def log_end():
    """
    Log program shutdown.
    """
    logging.info("========== Program Ended ==========")