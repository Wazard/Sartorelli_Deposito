import customtkinter as ctk
from core.classes_utils import MyPopup
from core import file_io
import os

class DotProductPopup(MyPopup):
    def __init__(self, master, on_confirm):
        super().__init__(master)
        # attributes
        self.on_confirm = on_confirm  # callback to parent
        self.selected_path = None

        # TopLevel config
        self.title("Load CSV")
        self.geometry("350x150")
        self.resizable(False, False)

        # Label
        self.path_label = ctk.CTkLabel(self, text="CSV Path:")
        self.path_label.pack(pady=5)

        # Browse button
        self.browse_btn = ctk.CTkButton(self, text="Browse...", command=self.browse_file)
        self.browse_btn.pack(pady=5)

        # Confirm button
        self.confirm_btn = ctk.CTkButton(self, text="Confirm", command=self.confirm)
        self.confirm_btn.pack(pady=5)

        # Info label
        self.info_label = ctk.CTkLabel(self, text="")
        self.info_label.configure(wraplength=280)
        self.info_label.pack(pady=5)

    def browse_file(self):
        path = ctk.filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")],
            title="Select a CSV file"
        )
        if path:
            self.selected_path = path
            self.info_label.configure(text=f"Selected: {os.path.basename(path)}", text_color="green")

    def confirm(self):
        if not self.selected_path:
            self.info_label.configure(text="Error: No file selected", text_color="red")
            return

        if not os.path.isfile(self.selected_path):
            self.info_label.configure(text="Error: File not found", text_color="red")
            return

        if not self.selected_path.lower().endswith(".csv"):
            self.info_label.configure(text="Error: Not a CSV file", text_color="red")
            return

        # Success
        self.info_label.configure(text="CSV path accepted!", text_color="green")

        # Callback to parent with loaded matrix
        matrix1, _ = file_io.load_csv(self.selected_path)

        super().confirm()
        self.on_confirm(matrix1)