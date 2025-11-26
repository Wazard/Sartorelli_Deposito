import customtkinter as ctk
import numpy as np
from gui.reshape_popup import ReshapePopup

class UnsortedArrayError(Exception):
    pass

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        self.data = data
        self.info_label = ctk.CTkLabel(self, text="")
        self.back_btn = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.reshape_btn = ctk.CTkButton(self, text="Reshape", command=self.reshape)

        self.info_label.pack(pady=10)
        self.back_btn.pack(side="left", padx=60, pady=20, anchor='s')
        self.reshape_btn.pack(side="right", padx=40, pady=20, anchor='s')
    
    def go_back(self):
        self.pack_forget()
        self.master.show_main(self.data)
    
    def reshape(self):
        ReshapePopup(self, self.data, self.on_reshaped)

    def on_reshaped(self, new_matrix):
        self.data = new_matrix
        pass


def reshape(matrix:np.ndarray, row, col) -> np.ndarray:
    return matrix.reshape(row, col)