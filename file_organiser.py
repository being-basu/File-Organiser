import os
import shutil

# Folder to organize
folder_path = r"C:\Users\hp\Downloads"  

# File categories and extensions
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

# Creating Folder
for folder in folders:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Moving  files to corresponding folders
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                break

print("Folder organized successfully!")
