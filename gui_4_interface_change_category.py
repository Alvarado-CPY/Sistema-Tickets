import tkinter as tk
from tkinter import ttk
import sqlite3


class GUI_root:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Cambiar Trabajador de Categoría")
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

    def destroyRoot(self):
        self.root.quit()
        self.root.destroy()


class GUI_change_category(GUI_root):
    def __init__(self, root: tk.Tk, data: str) -> None:
        super().__init__(root)

        # variables
        self.worker_data_to_change_category = data

if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    GUI_change_category(root, "new income")
    root.mainloop()