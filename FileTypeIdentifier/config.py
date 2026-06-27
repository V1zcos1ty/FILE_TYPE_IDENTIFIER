"""
config.py

Configuration settings for the File Type Identification project.
Modify values here instead of changing them throughout the code.
"""

# ==========================================================
# File Reading Configuration
# ==========================================================

# Number of bytes to read from the beginning of the file
HEADER_SIZE = 32

# ==========================================================
# Output Configuration
# ==========================================================

# Output folder
OUTPUT_FOLDER = "output"

# JSON report file
REPORT_FILE = "output/report.json"

# Log file
LOG_FILE = "output/log.txt"

# ==========================================================
# Application Configuration
# ==========================================================

# Application name
APP_NAME = "File Type Identification"

# Application version
VERSION = "1.0.0"

# Author
AUTHOR = "Akshat"

# ==========================================================
# Supported Extensions
# (Only used for displaying information)
# ==========================================================

SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp",
    ".zip",
    ".rar",
    ".7z",
    ".gz",
    ".exe",
    ".elf",
    ".mp3",
    ".wav",
    ".ogg",
    ".flac",
    ".mp4",
    ".avi",
    ".mkv",
    ".sqlite",
    ".db"
]

# ==========================================================
# Report Settings
# ==========================================================

SAVE_JSON_REPORT = True

ENABLE_LOGGING = True

SHOW_FILE_SIZE = True

SHOW_EXTENSION = True

SHOW_TIMESTAMP = True

# ==========================================================
# Display Settings
# ==========================================================

SEPARATOR = "=" * 60

WELCOME_MESSAGE = """
============================================
        FILE TYPE IDENTIFICATION
============================================
Identify the real file type using magic bytes.
"""

GOODBYE_MESSAGE = """
============================================
      Scan Completed Successfully
============================================
"""