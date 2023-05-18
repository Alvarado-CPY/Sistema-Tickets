import openpyxl
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread
import sqlite3

class ImportData:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

        # Excel File
        self.working_book = ""
        self.sheet_on_working_book = []

    def setWorkBook(self) -> bool:
        filename = filedialog.askopenfilename()

        if filename == "":
            messagebox.showerror("Error", "Debe seleccionar un archivo")
            return False

        try:
            self.working_book = openpyxl.load_workbook(
                filename=filename,
                read_only=True,
                data_only=True,
                keep_links=False
            )
        except openpyxl.utils.exceptions.InvalidFileException:
            messagebox.showerror("Error", "Extensión de archivo invalido debe de ser .xlsx")
            return False

if __name__ == "__main__":
    ...