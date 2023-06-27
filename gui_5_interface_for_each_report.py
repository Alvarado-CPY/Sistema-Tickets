import tkinter as tk

class GUI_root:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Reportes")
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.centralizeWindow()

    def destroyRoot(self):
        self.root.quit()
        self.root.destroy()

    def centralizeWindow(self):
        windows_width = 450
        windows_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_coordinate = int((screen_width/2) - (windows_width/2))
        y_coordinate = int((screen_height/2) - (windows_height/2))-40

        self.root.geometry(
            f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")


class GUI_new_income_report_between_dates(GUI_root):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)