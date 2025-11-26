import customtkinter as ctk
import numpy as np
from gui.reshape_popup import ReshapePopup
from gui.dot_product_popup import DotProductPopup
from core import classes_utils, matrix_oops


class MatrixFrame(classes_utils.MyFrame):
    def __init__(self, master, data, app):
        super().__init__(master, data, app)

        # Create Tabs
        axis_tab = self.tabview.add("Axis Analysis")
        algebra_tab = self.tabview.add("Algebra")
        axis_tab_frame = ctk.CTkFrame(axis_tab)
        algebra_tab_frame = ctk.CTkFrame(algebra_tab)

        # Axis analysis buttons
        ctk.CTkButton(axis_tab_frame, text="Sum by Col", command=self.show_sum_by_col).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(axis_tab_frame, text="Sum by Row", command=self.show_sum_by_row).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(axis_tab_frame, text="Mean by Col", command=self.show_mean_by_col).grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkButton(axis_tab_frame, text="Mean by Row", command=self.show_mean_by_row).grid(row=1, column=1, padx=10, pady=10)

        # Algebraical operations buttons
        ctk.CTkButton(algebra_tab_frame, text="Dot Product", command=self.show_mat_dot).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(algebra_tab_frame, text="Transpose", command=self.show_mat_transpose).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(algebra_tab_frame, text="Norm", command=self.show_mat_norm).grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkButton(algebra_tab_frame, text="Covariant", command=self.show_mat_covariant).grid(row=1, column=1, padx=10, pady=10)

        #configuraion
        self.info_label.configure(text=f"Matrix loaded:\n{np.array2string(data)}")
        self.tabview.configure(width=400, height=200)
        axis_tab_frame.pack(expand=True, anchor='center', pady=10)
        algebra_tab_frame.pack(expand=True, anchor='center', pady=10)

        self.flatten_btn = ctk.CTkButton(self, text="Flatten", command=self.flatten)
        self.flatten_btn.pack(side="bottom", pady=20, anchor='s')
    
    # Methods
    def show_sum_by_col(self):
        self.update_result(oop="Sum by columns = ", result=np.array2string(matrix_oops.sum_by_col(self.data)))

    def show_sum_by_row(self):
        self.update_result(oop="Sum by rows = ", result=np.array2string(matrix_oops.sum_by_row(self.data)))

    def show_mean_by_col(self):
        self.update_result(oop="Mean by columns = ", result=np.array2string(matrix_oops.mean_by_col(self.data)))

    def show_mean_by_row(self):
        self.update_result(oop="Mean by rows = ", result=np.array2string(matrix_oops.mean_by_row(self.data)))

    def show_mat_dot(self):

        def followup(matrix1:np.ndarray):
            result = matrix_oops.mat_dot(self.master, self.data, matrix1)
            self.update_result(oop="Dot result:\n", result=np.array2string(result))
        
        DotProductPopup(self, followup)

    def show_mat_transpose(self):
        self.update_result(oop="Transposition:\n", result=np.array2string(matrix_oops.mat_transpose(self.data)))

    def show_mat_norm(self):
        self.update_result(oop="Normalization = ", result=str(matrix_oops.mat_norm(self.data)))

    def show_mat_covariant(self):
        self.update_result(oop="Covariant:\n", result=np.array2string(matrix_oops.mat_covariant(self.data)))
    
    def flatten(self):
        # Remove current frame
        self.pack_forget()
        flattened_matrix = matrix_oops.flatten(self.data)
        # Show ArrayFrame instead
        from gui.array_frame import ArrayFrame
        frame = ArrayFrame(self.master, flattened_matrix, app=self.app)
        frame.pack(expand=True, fill="both")

    def reshape(self):
        ReshapePopup(self, self.data, self.on_reshaped)

    def on_reshaped(self, new_matrix):
        super().on_reshaped(new_matrix)
        self.info_label.configure(text=f"Matrix loaded:\n{np.array2string(self.data)}")
