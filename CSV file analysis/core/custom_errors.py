import customtkinter as ctk
from core.classes_utils import MyPopup

class ErrorPopup(MyPopup):
    def __init__(self, master, message: str):
        super().__init__(master)
        self.title("Error")
        self.geometry("300x150")
        self.resizable(False, False)

        label = ctk.CTkLabel(self, text=message, text_color="red", wraplength=250)
        label.pack(pady=20)

        btn = ctk.CTkButton(self, text="OK", command=self.destroy)
        btn.pack(pady=10)


# --- Custom Exceptions ---
class BaseAppError(Exception):
    def __init__(self, master, message: str | None = None):
        super().__init__(message)
        # Show popup immediately
        ErrorPopup(master, message)

class UnsortedArrayError(BaseAppError):
    def __init__(self, master, message = None):
        msg = message or "Array must be sorted before operation."
        super().__init__(master, msg)

class OddShapeMatrixError(BaseAppError):
    def __init__(self, master, message = None):
        msg = message or "Matrix shape is incompatible"
        super().__init__(master, msg)

class CsvIOError(BaseAppError):
    def __init__(self, master, message = None):
        msg = message or "There was an error handling the Csv"
        super().__init__(master, msg)

class DbRelatedError(BaseAppError):
    def __init__(self, master, message = None):
        msg = message or "There was an error regarding the database"
        super().__init__(master, msg)
