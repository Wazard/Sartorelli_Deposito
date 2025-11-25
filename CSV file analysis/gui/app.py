import customtkinter as ctk
from core import file_io as IO
from gui import matrix_frame, array_frame
import numpy as np

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.title("CSV Loader")
        self.geometry("500x300")

        self.info_label = ctk.CTkLabel(self, text="No file loaded yet")
        self.array_info_label = ctk.CTkLabel(self, text="")
        self.browse_btn = ctk.CTkButton(self, text="Browse CSV", command=self.on_browse)

        # packs
        self.info_label.pack(pady=20)
        self.browse_btn.pack(pady=10)
        self.array_info_label.pack(pady=10)

        self.start_btn = None
        self.data = None

    def on_browse(self):
        arr,arr_type,file_name = IO.load_csv()
    
        if arr is None:
            self.info_label.configure(text="No file loaded or error")
            return

        self.data = arr
        preview = np.array2string(arr)
    
        self.info_label.configure(text=f"{file_name} loaded")
        self.array_info_label.configure(text=f"{arr_type}:\n{preview}")

        # Show Start button dynamically
        if not self.start_btn:
            self.start_btn = ctk.CTkButton(self, text="Start", command=self.go_next)
            self.start_btn.pack(pady=10)

    def go_next(self):
        # Remove preview widgets
        self.info_label.pack_forget()
        self.browse_btn.pack_forget()
        if self.start_btn:
            self.start_btn.pack_forget()

        # Decide automatically
        if self.data.ndim == 1:
            frame = array_frame.main_frame(self, self.data)
        else:
            frame = matrix_frame.main_frame(self, self.data)

        frame.pack(expand=True, fill="both")