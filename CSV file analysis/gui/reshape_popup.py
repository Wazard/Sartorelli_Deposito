import customtkinter as ctk
from core.utils import MyPopup

class ReshapePopup(MyPopup):
    def __init__(self, master, data, on_reshaped):
        super().__init__(master)
        #attributes
        self.data = data
        self.on_reshaped = on_reshaped  # callback to parent
        self.row_label = ctk.CTkLabel(self, text="Rows:")
        self.col_label = ctk.CTkLabel(self, text="Cols:")
        self.confirm_btn = ctk.CTkButton(self, text="Confirm", command=self.confirm)

        # TopLetel config
        self.title("Reshape")
        self.geometry("300x200")
        self.resizable(False, False)

        # row settings and pack
        self.rows_entry = ctk.CTkEntry(self)
        self.row_label.pack()
        self.rows_entry.pack()

        # col settings and pack
        self.cols_entry = ctk.CTkEntry(self)
        self.col_label.pack()
        self.cols_entry.pack()

        self.confirm_btn.pack(pady=2)

        # info label settings and pack
        self.info_label = ctk.CTkLabel(self, text="")
        self.info_label.configure(wraplength=200)
        self.info_label.pack(pady = 1)

    def confirm(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            reshaped = self.data.reshape(rows, cols)
        except Exception as e:
            self.info_label.configure(text=f"Error: {e}", text_color="red")
            return

        self.info_label.configure(text="correctly reshaped!", text_color="green")

        # Call back to parent with reshaped array
        self.on_reshaped(reshaped)

        super().confirm()