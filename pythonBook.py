import os
import requests

# مسیر فایل raw
raw_file_path = 'free-programming-books.txt'

# پوشه‌ای که فایل‌های دانلودشده ذخیره می‌شوند
download_folder = 'downloaded_books'

# بررسی و ایجاد پوشه دانلود
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# خواندن فایل raw
if not os.path.exists(raw_file_path):
    print(f"فایل {raw_file_path} پیدا نشد. لطفاً فایل را در پوشه اسکریپت قرار دهید.")
    exit(1)

with open(raw_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# استخراج لینک‌ها و عناوین آن‌ها
pdf_links = []
for line in lines:
    if '.pdf' in line:
        # استخراج نام عنوان (متن بین [])
        title = line.split('[')[1].split(']')[0].strip()
        # استخراج لینک (متن بین پرانتزها)
        url = line.split('](')[1].split(')')[0].strip()
        pdf_links.append((title, url))

# بررسی تعداد لینک‌های پیدا شده
if not pdf_links:
    print("هیچ لینکی با فرمت .pdf پیدا نشد.")
    exit(0)

# دانلود فایل‌ها
for title, pdf_url in pdf_links:
    try:
        print(f"در حال دانلود: {title} از {pdf_url}")
        pdf_response = requests.get(pdf_url)

        # بررسی وضعیت دانلود
        if pdf_response.status_code == 200:
            # حذف کاراکترهای نامعتبر از نام فایل
            safe_title = ''.join(c for c in title if c.isalnum() or c in ' _-').strip()
            file_name = f"{safe_title}.pdf"
            file_path = os.path.join(download_folder, file_name)

            # ذخیره فایل PDF
            with open(file_path, 'wb') as f:
                f.write(pdf_response.content)
            print(f"دانلود شد: {file_name}")
        else:
            print(f"خطا در دانلود {pdf_url}: {pdf_response.status_code}")

    except Exception as e:
        print(f"خطا در دانلود {pdf_url}: {e}")

print("پایان دانلود.")
