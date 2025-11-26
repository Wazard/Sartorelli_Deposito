import customtkinter as ctk
import numpy as np
from abc import ABC, abstractmethod

class MyFrame(ctk.CTkFrame, ABC):
    def __init__(self, master, data, app):
        super().__init__(master)
        
        #Variables
        self.app = app
        self.data = data
        self.info_label = ctk.CTkLabel(self, text="")
        self.back_btn = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.reshape_btn = ctk.CTkButton(self, text="Reshape", command=self.reshape)
        self.result_label = ctk.CTkLabel(self, text="result will show here")
        self.tabview = ctk.CTkTabview(self, height=200)

        # Packs
        self.info_label.pack(pady=5)
        self.result_label.pack(pady=10)
        self.tabview.pack(expand=True, fill='both', pady=10, padx=10)
        self.back_btn.pack(side="left", padx=60, pady=20, anchor='s')
        self.reshape_btn.pack(side="right", padx=40, pady=20, anchor='s')

        # Config
        self.result_label.configure(wraplength=400)
    
    def go_back(self):
        self.pack_forget()
        self.app.show_main(self.data)
    
    def update_result(self, oop:str, result:str):
        self.result_label.configure(text=f"{oop.capitalize()} {result}")
        self.app.auto_resize()
    
    @abstractmethod
    def reshape(self):
        pass

    def on_reshaped(self, new_matrix):
        self.data = new_matrix
        pass

class MyPopup(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Popup")

        # Bring on top and force focus
        self.lift()
        self.focus_force()
        self.grab_set()
        self.attributes("-topmost", True)

    def center_on_master(self):
        self.update_idletasks()

        # Master absolute position on screen
        master_x = self.master.winfo_rootx()
        master_y = self.master.winfo_rooty()
        master_w = self.master.winfo_width()
        master_h = self.master.winfo_height()

        # Popup size
        popup_w = self.winfo_width()
        popup_h = self.winfo_height()

        # Compute centered position
        x = master_x + (master_w // 2) - (popup_w // 2)
        y = master_y + (master_h // 2) - (popup_h // 2)

        # Apply position (keep size the same, only move)
        self.geometry(f"+{x}+{y}")

    def confirm(self, timer=500):
        print("self destroying popup")
        self.after(timer, self.destroy)
    
    def top_level_config(self, title:str, geometry:str):
        # TopLetel config
        self.title(title)
        self.geometry(geometry)
        self.resizable(False, False)
        self.center_on_master()


def reshape(matrix:np.ndarray, row, col) -> np.ndarray:
    return matrix.reshape(row, col)