import tkinter as tk
from app_global_variables import guiConfig


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


class GUI_newIncomeReportOptions:
    def __init__(self, frame: tk.Frame):
        # frame master
        self.frame = frame

        # inner frame
        self.frame_new_income_reports: tk.Frame = tk.Frame(self.frame)
        self.frame_new_income_reports.grid(
            row=0, column=0, sticky="WENS", padx=5, pady=5)

        self.frame_new_income_reports.grid_columnconfigure(0, weight=1)

        # widgets
        self.button_report_who_is_new: tk.Button = tk.Button(
            self.frame_new_income_reports, text="Reportar Nuevos Entre Fechas")
        self.button_report_who_is_new.grid(row=0, column=0, sticky="WENS")
        self.button_report_who_is_new.config(
            font=[guiConfig().getFonts()["main_font"], 15]
        )


class GUI_reportsMenu(GUI_root):
    def __init__(self, root: tk.Tk, data):
        super().__init__(root)
        # variables
        self.category = data

        # frames
        self.frame_main: tk.LabelFrame = tk.LabelFrame(
            self.root, text="ELIGE LA OPCIÓN A REPORTAR PARA ")
        self.frame_main.grid(row=0, column=0, sticky="WENS", padx=5, pady=5)

        self.frame_main.grid_rowconfigure(0, weight=1)
        self.frame_main.grid_columnconfigure(0, weight=1)

        # load options
        self.loadRespectiveCategoryOptions()

    def loadRespectiveCategoryOptions(self):
        if self.category == "Nuevo Ingreso":
            self.frame_main["text"] += "NUEVOS INGRESOS"
            GUI_newIncomeReportOptions(self.frame_main)
