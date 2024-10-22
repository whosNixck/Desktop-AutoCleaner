import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_TYPES = {
    "Bilder": [".jpeg", ".jpg", ".png", ".gif"],
    "Dokumente": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Tabelle": [".xlsm", ".xlsx", ".csv"],
    "Praesentation": [".pptx", ".odp"],
    "Zip-Datein": [".zip"],
    "Others": []
}

def clean_folder(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            dest_folder = next((f for f, exts in FILE_TYPES.items() if ext in exts), "Others")
            dest_folder_path = os.path.join(folder, dest_folder)
            os.makedirs(dest_folder_path, exist_ok=True)

            dest_file_path = os.path.join(dest_folder_path, file)

            if os.path.exists(dest_file_path):
                response = messagebox.askyesno("Datei existiert", f"Die Datei '{file}' existiert bereits. Moechten Sie sie ersetzen?")
                if response:
                    shutil.move(file_path, dest_file_path)
                else:
                    base, extension = os.path.splitext(file)
                    counter = 1
                    new_file_name = f"{base} ({counter}){extension}"
                    new_dest_file_path = os.path.join(dest_folder_path, new_file_name)
                    
                    while os.path.exists(new_dest_file_path):
                        counter += 1
                        new_file_name = f"{base} ({counter}){extension}"
                        new_dest_file_path = os.path.join(dest_folder_path, new_file_name)

                    shutil.move(file_path, new_dest_file_path)
            else:
                shutil.move(file_path, dest_file_path)

def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

folder = select_folder()
if folder:
    tk.Tk().withdraw() 
    clean_folder(folder)
