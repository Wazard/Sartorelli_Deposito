import customtkinter as ctk
import numpy as np
from core import utils

class MatrixFrame(utils.MyFrame):
    def __init__(self, master, data):
        super().__init__(master, data)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)
    
        self.info_label.configure(text=f"Matrix loaded:\n{np.array2string(data)}")
    
    def on_reshaped(self, new_matrix):
        super().on_reshaped(new_matrix)
        self.info_label.configure(text=f"Matrix loaded:\n{np.array2string(self.data)}")
