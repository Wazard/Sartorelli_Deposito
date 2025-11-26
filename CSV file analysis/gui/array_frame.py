import customtkinter as ctk
import numpy as np
from core import utils

class ArrayFrame(utils.MyFrame):
    def __init__(self, master, data):
        super().__init__(master, data)

        ctk.CTkButton(self, text="Sum", command=self.show_sum).pack(pady=10)
        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)
    
        self.info_label.configure(text=f"Array loaded:\n{np.array2string(data)}")

    def on_reshaped(self, new_matrix):
        # Remove current frame
        self.pack_forget()
        # Show MatrixFrame instead
        from gui.matrix_frame import MatrixFrame
        frame = MatrixFrame(self.master, new_matrix)
        frame.pack(expand=True, fill="both")
    
    def show_sum(self):
        self.result_label.configure(text=f"Sum = {self.arr.sum()}")