# Python Book Downloader

A Python script that automatically downloads programming books from a curated list of free PDF resources.

## Description

This project contains a Python script that reads a list of free programming books from a text file and downloads the PDF versions of these books. The script processes a specially formatted text file containing book titles and their download URLs, then saves the downloaded PDFs to a designated folder.

## Features

- Automatically downloads PDF books from provided URLs
- Handles file naming and organization
- Error handling for failed downloads
- UTF-8 support for international characters
- Creates a dedicated download directory

## Prerequisites

- Python 3.x
- Required Python packages:
  - requests

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-book-download.git
cd python-book-download
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install requests
```

## Usage

1. Ensure you have the `free-programming-books.txt` file in the project directory
2. Run the script:
```bash
python pythonBook.py
```

The script will:
- Create a `downloaded_books` directory if it doesn't exist
- Read the book list from `free-programming-books.txt`
- Download PDF files and save them to the `downloaded_books` directory
- Display progress and any errors during the download process

## File Structure

- `pythonBook.py` - Main script file
- `free-programming-books.txt` - Source file containing book information
- `downloaded_books/` - Directory where downloaded PDFs are stored
- `.venv/` - Python virtual environment directory

## Notes

- The script expects the input file to be in a specific format with book titles in square brackets and URLs in parentheses
- Downloaded files are saved with sanitized filenames to avoid any filesystem issues
- The script includes error handling for failed downloads and invalid URLs

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome! 