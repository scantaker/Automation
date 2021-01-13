import tkinter as tk
from tkinter import filedialog


def file_paths_openfile():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames()

    return file_paths
