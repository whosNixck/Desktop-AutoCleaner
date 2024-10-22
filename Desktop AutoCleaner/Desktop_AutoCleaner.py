import os, shutil, tkinter as tk
from tkinter import filedialog

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
        ext = os.path.splitext(file)[1].lower()
        dest_folder = next((f for f, exts in FILE_TYPES.items() if ext in exts), "Others")
        os.makedirs(os.path.join(folder, dest_folder), exist_ok = True)
        shutil.move(os.path.join(folder, file), os.path.join(folder, dest_folder, file))

def select_folder():
    root = tk.Tk(); root.withdraw()
    return filedialog.askdirectory()

folder = select_folder()
if folder: clean_folder(folder)