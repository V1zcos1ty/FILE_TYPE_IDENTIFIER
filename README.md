# FileTypeIdentifier


## Overview

File Type Identification is a Python-based cybersecurity tool that determines the **actual type of a file** by examining its binary signature (magic bytes) instead of relying on its file extension.

This helps identify renamed or disguised files that may be malicious or misleading.

---

## Features

- Detect actual file type using magic bytes
- Compare file extension with actual file type
- Identify mismatched or suspicious files
- Support multiple common file formats
- Generate JSON reports
- Log scan activity
- Modular and easy-to-extend codebase

---

## Supported File Types

- PDF
- PNG
- JPEG
- GIF
- ZIP
- RAR
- 7ZIP
- EXE
- MP3

More signatures can easily be added.

---

## Project Structure

```
FileTypeIdentifier/
│
├── main.py
├── detector.py
├── signatures.py
├── file_reader.py
├── validator.py
├── utils.py
├── config.py
├── logger.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── samples/
├── output/
└── tests/
```

---

## Requirements

- Python 3.10+
- colorama
- python-magic
- rich
- pytest

Install dependencies:

```bash
pip3 install -r requirements.txt
```

---

## How It Works

1. User selects a file.
2. The program validates the file.
3. The first bytes (magic bytes) are read.
4. The bytes are converted into hexadecimal.
5. The hexadecimal signature is compared with known file signatures.
6. The actual file type is displayed.
7. A report is generated.

---

## Example

Input:

```
photo.jpg
```

Output:

```
Detected Type : JPEG Image
Status        : Match
```

Example of a renamed file:

Input:

```
virus.jpg
```

Output:

```
Detected Type : Windows Executable
Status        : Warning
Reason        : Extension does not match file signature.
```

---

## Technologies Used

- Python
- File I/O
- Hexadecimal Processing
- Logging
- JSON
- Magic Byte Analysis

---

## Future Improvements

- Drag-and-drop GUI
- Batch folder scanning
- SHA256 and MD5 hash generation
- VirusTotal API integration
- File entropy analysis
- Malware detection
- PDF report generation
- Multi-threaded scanning

---

## Educational Purpose

This project is intended for educational purposes to demonstrate:

- File system operations
- Binary file analysis
- Digital forensics basics
- Malware detection concepts
- Python programming

---

## License

This project is released under the MIT License.

---

## Author

**KumarAkshat**

Cybersecurity Project – File Type Identification
