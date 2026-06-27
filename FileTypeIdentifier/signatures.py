"""
signatures.py

This module contains known file signatures (magic bytes) used to
identify the actual file type regardless of its extension.
"""

FILE_SIGNATURES = {
    # Documents
    "25504446": "PDF Document",

    # Images
    "89504E470D0A1A0A": "PNG Image",
    "FFD8FF": "JPEG Image",
    "474946383761": "GIF Image (GIF87a)",
    "474946383961": "GIF Image (GIF89a)",
    "424D": "BMP Image",
    "49492A00": "TIFF Image (Little Endian)",
    "4D4D002A": "TIFF Image (Big Endian)",
    "52494646": "WEBP Image",

    # Archives
    "504B0304": "ZIP Archive",
    "504B0506": "ZIP Archive (Empty)",
    "504B0708": "ZIP Archive (Spanned)",
    "526172211A0700": "RAR Archive",
    "377ABCAF271C": "7-Zip Archive",
    "1F8B08": "GZIP Archive",

    # Executables
    "4D5A": "Windows Executable (EXE)",
    "7F454C46": "Linux ELF Executable",

    # Audio
    "494433": "MP3 Audio",
    "FFFB": "MP3 Audio",
    "664C6143": "FLAC Audio",
    "4F676753": "OGG Audio",
    "52494646": "WAV Audio",

    # Video
    "0000001866747970": "MP4 Video",
    "1A45DFA3": "MKV Video",
    "52494646": "AVI Video",

    # Microsoft Office
    "D0CF11E0A1B11AE1": "Microsoft Office Document (Legacy)",

    # Database
    "53514C69746520666F726D6174203300": "SQLite Database",

    # Scripts
    "2321": "Script File (Shebang)",

    # ISO
    "4344303031": "ISO Disk Image"
}


def get_signatures():
    """
    Returns the complete dictionary of known file signatures.
    """
    return FILE_SIGNATURES


def list_supported_types():
    """
    Returns a sorted list of supported file types.
    """
    return sorted(set(FILE_SIGNATURES.values()))