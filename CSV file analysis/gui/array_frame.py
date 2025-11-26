import customtkinter as ctk
import numpy as np
from core.utils import MyFrame, UnsortedArrayError
from core import array_oops


class ArrayFrame(MyFrame):
    def __init__(self, master, data):
        super().__init__(master, data)

        # Create Tabs and inner Frames
        basic_tab = self.tabview.add("Basic Analysis")
        position_tab = self.tabview.add("Position Analysis")
        basic_tab_frame = ctk.CTkFrame(basic_tab)
        position_tab_frame = ctk.CTkFrame(position_tab)

        # Basic Analysis
        ctk.CTkButton(basic_tab_frame, text="Min", command=self.show_min).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(basic_tab_frame, text="Max", command=self.show_max).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(basic_tab_frame, text="Mean", command=self.show_mean).grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkButton(basic_tab_frame, text="Deviation", command=self.show_deviation).grid(row=1, column=1, padx=10, pady=10)

        # Position Analysis
        ctk.CTkButton(position_tab_frame, text="Min Index", command=self.show_min_idx).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(position_tab_frame, text="Max Index", command=self.show_max_idx).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(position_tab_frame, text="Percentile", command=self.show_percentile).grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkButton(position_tab_frame, text="Search Sorted", command=self.show_search_sorted).grid(row=1, column=1, padx=10, pady=10)

        # Config
        self.info_label.configure(text=f"Array loaded:\n{np.array2string(data)}")
        self.tabview.configure(width=400, height=200)
        basic_tab_frame.pack(expand=True, anchor='center', pady=10)
        position_tab_frame.pack(expand=True, anchor='center', pady=10)


    # Methods
    def show_max(self):
        self.update_result(oop="Max = ", result=str(array_oops.arr_max(self.data)))

    def show_min(self):
        self.update_result(oop="Min = ", result=str(array_oops.arr_min(self.data)))
    
    def show_mean(self):
        self.update_result(oop="Mean = ", result=str(array_oops.arr_mean(self.data)))

    def show_deviation(self):
        self.update_result(oop="Deviation = ", result=str(array_oops.arr_deviation(self.data)))

    def show_min_idx(self):
        self.update_result(oop="Index of Min = ", result=str(array_oops.arr_min_idx(self.data)))

    def show_max_idx(self):
        self.update_result(oop="Index of Max = ", result=str(array_oops.arr_max_idx(self.data)))

    def show_percentile(self):
        self.update_result(oop="Percentile = ", result=str(array_oops.arr_percentile(self.data)))

    def show_search_sorted(self, value:float):
        try:
            idx = array_oops.arr_search_sorted(self.data, value)
            self.update_result(oop="search_sorted", result=f"value {value} at index {idx}")
        except UnsortedArrayError as e:
            self.update_result(oop="search_sorted", result=str(e))

    # Override
    def on_reshaped(self, new_matrix):
        # Remove current frame
        self.pack_forget()
        # Show MatrixFrame instead
        from gui.matrix_frame import MatrixFrame
        frame = MatrixFrame(self.master, new_matrix)
        frame.pack(expand=True, fill="both")