from bing_image_downloader import downloader
import os
currencies = [
    "10 rupees note", 
    "20 rupees note", 
    "50 rupees note", 
    "100 rupees note", 
    "500 rupees note", 
    "2000 rupees note"
]

OUTPUT_DIR = "dataset"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for currency in currencies:
    print(f"Downloading images for: {currency}")
    downloader.download(
        currency,
        limit=50,
        output_dir=OUTPUT_DIR,
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )

print("Image download completed!")
