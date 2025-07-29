# multi_tool.py

import qrcode
from pytube import YouTube
import pywhatkit as kit
import sys

# ---- Generate QR Code ----
def create_qr():
    data = input("Enter text or URL for QR code: ")
    filename = input("Enter filename to save (e.g., qrcode.png): ")
    img = qrcode.make(data)
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

# ---- Download YouTube Video ----
def download_youtube_video():
    try:
        url = input("Enter YouTube video URL: ").split('&')[0]  # Remove extra params
        path = input("Enter download path (or press Enter for current folder): ") or "."
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)
        print("✅ Video downloaded successfully!")
    except Exception as e:
        print(f"❌ Error downloading video: {e}")


# ---- Send WhatsApp Message ----
def send_whatsapp_message():
    phone = input("Enter phone number with country code (e.g., +911234567890): ")
    message = input("Enter your message: ")
    hour = int(input("Enter hour (24-hour format): "))
    minute = int(input("Enter minute: "))
    print("✅ Scheduling message... (Do not close this window)")
    kit.sendwhatmsg(phone, message, hour, minute)
    print(f"✅ WhatsApp message scheduled to {phone}")

# ---- Menu ----
def main():
    while True:
        print("\n===== Python Multi Tool =====")
        print("1. Generate QR Code")
        print("2. Download YouTube Video")
        print("3. Send WhatsApp Message")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            create_qr()
        elif choice == "2":
            download_youtube_video()
        elif choice == "3":
            send_whatsapp_message()
        elif choice == "4":
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
