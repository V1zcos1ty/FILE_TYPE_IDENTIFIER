"""
main.py

Main entry point for the File Type Identification project.
"""

import os

from config import WELCOME_MESSAGE, GOODBYE_MESSAGE
from validator import validate_file, get_extension
from file_reader import (
    read_file_header,
    get_file_name,
    get_file_size
)
from detector import detect_file_type
from utils import (
    print_title,
    print_success,
    print_error,
    print_warning,
    format_file_size,
    save_json_report,
    create_result
)
from logger import (
    log_start,
    log_end,
    log_detection,
    log_error
)


def main():

    log_start()

    print(WELCOME_MESSAGE)

    file_path = input("Enter file path: ").strip()

    # Validate file
    if not validate_file(file_path):
        log_error("Invalid file selected.")
        return

    try:
        # Read file information
        file_name = get_file_name(file_path)
        extension = get_extension(file_path)
        file_size = get_file_size(file_path)

        # Read header bytes
        header = read_file_header(file_path)

        # Detect actual type
        detected_type = detect_file_type(header)

        # Check extension
        expected_extension = detected_type.split()[0].lower()

        if extension.replace(".", "") == expected_extension:
            status = "MATCH"
            print_success("Extension matches detected file type.")
        else:
            status = "MISMATCH"
            print_warning("Extension does NOT match detected file type.")

        # Display Results
        print_title("SCAN RESULT")

        print(f"File Name      : {file_name}")
        print(f"Extension      : {extension}")
        print(f"Detected Type  : {detected_type}")
        print(f"File Size      : {format_file_size(file_size)}")
        print(f"Status         : {status}")

        # Save JSON Report
        result = create_result(
            file_name,
            extension,
            detected_type,
            status
        )

        save_json_report(result)

        log_detection(file_name, detected_type)

        print_success("Report saved to output/report.json")

    except Exception as e:
        print_error(str(e))
        log_error(str(e))

    finally:
        log_end()
        print(GOODBYE_MESSAGE)


if __name__ == "__main__":
    main()