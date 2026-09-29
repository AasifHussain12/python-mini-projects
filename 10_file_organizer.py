# File Organizer

import os
import shutil

print("===================================")
print("        FILE ORGANIZER")
print("===================================")

folder = input("Enter folder path: ")

if os.path.exists(folder):

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1].lower()

            if extension == ".txt":
                destination = os.path.join(folder, "Text Files")

            elif extension == ".pdf":
                destination = os.path.join(folder, "PDF Files")

            elif extension == ".jpg" or extension == ".png":
                destination = os.path.join(folder, "Images")

            elif extension == ".mp3":
                destination = os.path.join(folder, "Music")

            elif extension == ".mp4":
                destination = os.path.join(folder, "Videos")

            else:
                destination = os.path.join(folder, "Others")

            os.makedirs(destination, exist_ok=True)
            shutil.move(file_path, os.path.join(destination, file))

    print("\n✅ Files organized successfully!")

else:
    print("❌ Folder not found.")