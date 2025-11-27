import customtkinter as ctk
from core import file_io as IO
from gui import matrix_frame, array_frame
import numpy as np

class App(ctk.CTk):
    def __init__(self, min_size:str = "640x480" , max_size:str = "960x720"):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Attributes
        self.data = None
        self.file_name = None
        self.arr_type = None

        self.title("CSV Loader")
        self.geometry(min_size)

        # Max window size
        self.max_size = max_size
        self.min_size = min_size

        # Scrollable container
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(expand=True, fill="both")

        self.show_main()

    def show_main(self, data=None):
        self.data = data
        self.start_btn = None

        if self.data is None:
            self.info_label = ctk.CTkLabel(self.scroll_frame, text="No file loaded yet")

        self.array_info_label = ctk.CTkLabel(self.scroll_frame, text="")
        self.browse_btn = ctk.CTkButton(self.scroll_frame, text="Browse CSV", command=self.browse_file)

        # packs
        self.info_label.pack(pady=20)
        self.browse_btn.pack(pady=10)
        self.array_info_label.pack(pady=10)

        self.update_preview()
        self.auto_resize()

    def browse_file(self):
        path = ctk.filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")],
            title="Select a CSV file"
        )
        if path:
            self.selected_path = path
            self.file_name = self.selected_path.split('/')[-1]
            self.info_label.configure(text=f"Selected: {self.file_name}", text_color='green')

        arr, arr_type = IO.load_csv(self.selected_path)

        if arr is None:
            self.info_label.configure(text="No file loaded or error", text_color="red")
            return

        self.data = arr
        self.arr_type = arr_type
        self.update_preview()
        self.auto_resize()

    def update_preview(self):
        if self.data is None:
            return

        preview = np.array2string(self.data)
        self.info_label.configure(text=f"{self.file_name} loaded")
        self.array_info_label.configure(text=f"{self.arr_type}:\n{preview}")

        # Show Start button dynamically
        if not self.start_btn:
            self.start_btn = ctk.CTkButton(self.scroll_frame, text="Start", command=self.go_next)
            self.start_btn.pack(pady=10)
        
        self.auto_resize()

    def go_next(self):
        # Clear scroll frame
        for widget in self.scroll_frame.winfo_children():
            widget.pack_forget()

        # Decide automatically
        if self.data.ndim == 1:
            frame = array_frame.ArrayFrame(self.scroll_frame, self.data, app=self)
        else:
            frame = matrix_frame.MatrixFrame(self.scroll_frame, self.data, app=self)

        frame.pack(expand=True, fill="both")
        self.auto_resize()
    

    def auto_resize(self):
        """Resize window to fit content, between min and max size."""
        self.update_idletasks()
        req_w = self.scroll_frame.winfo_reqwidth()
        req_h = self.scroll_frame.winfo_reqheight()
        
        split_size = self.min_size.split('x')
        min_width, min_height = int(split_size[0]),int(split_size[1])
        split_size = self.max_size.split('x')
        max_width, max_height = int(split_size[0]),int(split_size[1])
        

        # Clamp to min and max
        width = max(min_width, min(req_w + 50, max_width))
        height = max(min_height, min(req_h + 50, max_height))

        self.geometry(f"{width}x{height}")