import customtkinter as ctk
import numpy as np
from gui.reshape_popup import ReshapePopup

class UnsortedArrayError(Exception):
    pass

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        
        #Variables
        self.data = data
        self.info_label = ctk.CTkLabel(self, text="")
        self.back_btn = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.reshape_btn = ctk.CTkButton(self, text="Reshape", command=self.reshape)
        self.result_label = ctk.CTkLabel(self, text="result will show here")
        self.tabview = ctk.CTkTabview(self, height=200)
    
        #self.button_frame = ctk.CTkFrame(self)

        # Packs
        self.info_label.pack(pady=5)
        self.result_label.pack(pady=10)
        self.tabview.pack(expand=True, fill='both', pady=10, padx=10)
        #self.button_frame.pack(expand=True)
        self.back_btn.pack(side="left", padx=60, pady=20, anchor='s')
        self.reshape_btn.pack(side="right", padx=40, pady=20, anchor='s')

        # Config
        self.result_label.configure(wraplength=400)
    
    def go_back(self):
        self.pack_forget()
        self.master.show_main(self.data)
    
    def update_result(self, oop:str, result:str):
        self.result_label.configure(text=f"{oop.capitalize()} {result}")
    
    def reshape(self):
        ReshapePopup(self, self.data, self.on_reshaped)

    def on_reshaped(self, new_matrix):
        self.data = new_matrix
        pass


def reshape(matrix:np.ndarray, row, col) -> np.ndarray:
    return matrix.reshape(row, col)