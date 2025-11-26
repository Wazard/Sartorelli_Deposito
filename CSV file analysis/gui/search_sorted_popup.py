import customtkinter as ctk
from core.classes_utils import MyPopup


class SearchSortedPopup(MyPopup):
    def __init__(self, master, on_confirm):
        super().__init__(master)
        # attributes
        self.on_confirm = on_confirm  # callback to parent

        # TopLevel config
        self.top_level_config("Number Selector", "350x150")

        # Label
        self.path_label = ctk.CTkLabel(self, text="Select a number for Search Sorted")
        self.path_label.pack(pady=5)

        # row settings and pack
        self.search_entry = ctk.CTkEntry(self)
        self.search_entry.pack()

        # Confirm button
        self.confirm_btn = ctk.CTkButton(self, text="Confirm", command=self.confirm)
        self.confirm_btn.pack(pady=5)

        # Info label
        self.info_label = ctk.CTkLabel(self, text="")
        self.info_label.configure(wraplength=280)
        self.info_label.pack(pady=5)

    def confirm(self):
        try:
            search_number = int(self.search_entry.get())
            self.info_label.configure(text="Number selected correctly!", text_color='green')
        except Exception as e:
            self.info_label.configure(text=f"Error: {e}", text_color="red")
            return

        # Call back to parent with reshaped array
        super().confirm()
        self.on_confirm(search_number)