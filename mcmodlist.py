from zipfile import ZipFile
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showwarning

import tkinter as tk
import os

class Main():
    def __init__(self):
        # instance variables
        self.root = tk.Tk()
        self.master_canvas = tk.Canvas(self.root)
        self.info_label = tk.Label(self.root)
        self.zip_button = tk.Button(self.root)
        self.folder_button = tk.Button(self.root)
        self.zip_path = ""
        self.folder_path = ""
        # class method calls
        self.__config_window()
        self.__make_elements()
    
    def __config_window(self):
        self.root.wm_resizable(False, False)
        self.master_canvas.config(background="lightGray")
        return None
    
    def __make_elements(self):
        # create the label
        self.info_label.config(text="Choose which file type to analyze.", font=("Helvectica Bold", 16), padx=50, pady=25)
        self.info_label.grid(column=0, row=0, columnspan=3, rowspan=1)
        # create the buttons
        self.zip_button.config(text="ZIP", command=self.select_zip, padx=0, pady=25, font=("Helvetica Bold", 8))
        self.zip_button.grid(column=0, row=1, columnspan=1, rowspan=1)
        self.folder_button.config(text="FOLDER", command=self.select_folder, padx=0, pady=25, font=("Helvetica Bold", 8))
        self.folder_button.grid(column=2, row=1, columnspan=1, rowspan=1)
        return None

    def select_zip(self):
        zip_file = askopenfilename(filetypes=[("ZIP files", "*.zip")])
        while not zip_file:
            showwarning("No File Selected.", "No zip file was selected. Please try again")
            zip_file = askopenfilename(filetypes=[("ZIP files", "*.zip")])
        self.zip_path = zip_file
        self.__print_contents()
        return None
    
    def select_folder(self):
        folder_dir = askdirectory()
        while not folder_dir:
            showwarning("No Folder Selected.", "No folder was selected. Please try again.")
            folder_dir = askdirectory()
        self.folder_path = folder_dir
        self.__print_contents()
        return None
    
    def __print_contents(self):
        if self.zip_path != "":
            with ZipFile(self.zip_path, 'r') as z:
                with open("mods.txt", 'w') as f:
                    for file in z.namelist():
                        f.write(f"{os.path.basename(file)}\n")
                    f.close()
                z.close()
                        
        elif self.folder_path != "":
            with open("mods.txt", 'w') as f:
                for file in os.listdir(self.folder_path):
                    f.write(f"{file}\n")
                f.close()
        return None

if __name__ == "__main__":
    instance = Main()
    instance.root.mainloop()
    