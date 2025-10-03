import os
import requests

# Path to the raw file
raw_file_path = 'free-programming-books.txt'

# Folder where downloaded files will be stored
download_folder = 'downloaded_books'

# Check and create the download folder
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Read the raw file
if not os.path.exists(raw_file_path):
    print(f"File {raw_file_path} not found. Please place the file in the script folder.")
    exit(1)

with open(raw_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Extract links and their titles
pdf_links = []
for line in lines:
    if '.pdf' in line:
        # Extract title (text inside [])
        title = line.split('[')[1].split(']')[0].strip()
        # Extract link (text inside ())
        url = line.split('](')[1].split(')')[0].strip()
        pdf_links.append((title, url))

# Check the number of found links
if not pdf_links:
    print("No .pdf links found.")
    exit(0)

# Download files
for title, pdf_url in pdf_links:
    try:
        print(f"Downloading: {title} from {pdf_url}")
        pdf_response = requests.get(pdf_url)

        # Check download status
        if pdf_response.status_code == 200:
            # Remove invalid characters from file name
            safe_title = ''.join(c for c in title if c.isalnum() or c in ' _-').strip()
            file_name = f"{safe_title}.pdf"
            file_path = os.path.join(download_folder, file_name)

            # Save the PDF file
            with open(file_path, 'wb') as f:
                f.write(pdf_response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Error downloading {pdf_url}: {pdf_response.status_code}")

    except Exception as e:
        print(f"Error downloading {pdf_url}: {e}")

print("Download completed.")
