import tkinter as tk
from tkinter import ttk, messagebox

class GUI_root:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Trabajador")
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

    def destroyRoot(self):
        self.root.quit()
        self.root.destroy()

class GUI_workerForm(GUI_root):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    GUI_workerForm(root)
    root.mainloop()