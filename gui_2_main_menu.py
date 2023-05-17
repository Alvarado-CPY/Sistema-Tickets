import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import os
from app_global_variables import guiConfig, dbPath


class GUI_root:
    def __init__(self, root: tk.Tk) -> None:

        self.root = root
        self.root.title(
            "Sistema De Gestión Automatizada De Tickets De Alimentación")
        self.setfullScreen()
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure((0,1), weight=1)

    def setfullScreen(self):
        if os.name == "nt":
            self.root.state("zoomed")
        else:
            self.root.attributes("-fullscreen", True)

    def destroyRoot(self):
        if messagebox.askyesno("Atención", "¿Está seguro de salir de la aplicación?"):
            self.deleteActiveUser()
            self.root.quit()
            self.root.destroy()

    def deleteActiveUser(self):
        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            cursor.execute("DELETE FROM active_user")
            bd.commit()


class GUI_barmenu(GUI_root):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)

        self.Menu: tk.Menu = tk.Menu(self.root)
        self.root.config(menu=self.Menu)

        # creating menu functions
        self.Menu_function_new: tk.Menu = tk.Menu(self.Menu, tearoff=False)
        self.Menu_function_report: tk.Menu = tk.Menu(self.Menu, tearoff=False)
        self.Menu_function_export: tk.Menu = tk.Menu(self.Menu, tearoff=False)
        self.Menu_function_help: tk.Menu = tk.Menu(self.Menu, tearoff=False)

        self.addCommandsToMenus()

        # adding menu functions to menubar
        self.Menu.add_cascade(
            label="Nuevo",
            menu=self.Menu_function_new
        )
        self.Menu.add_cascade(
            label="Reporte",
            menu=self.Menu_function_report
        )
        self.Menu.add_cascade(
            label="Base de Datos",
            menu=self.Menu_function_export
        )
        self.Menu.add_cascade(
            label="Ayuda",
            menu=self.Menu_function_help
        )

    def addCommandsToMenus(self):
        self.addCommandsToNewMenu()
        self.addCommandsToReportMenu()
        self.addCommandsToExportMenu()
        self.addCommadsToHelpMenu()

    def addCommandsToNewMenu(self):
        functions = {
            "Nuevo Ingreso": lambda: print("1"),
            "Nuevo Reactivación": lambda: print("2"),
            "Nuevo Suspensión": lambda: print("3"),
            "Nuevo Egreso": lambda: print("4"),
            "Nuevo Usuario": lambda: print("5")
        }

        for key in functions.keys():
            self.Menu_function_new.add_command(
                label=key,
                command=functions[key]
            )

    def addCommandsToReportMenu(self):
        functions = {
            "Reporte General": lambda: print("1"),
            "Reporte Nuevo Ingresos": lambda: print("2"),
            "Reporte Reactivaciones": lambda: print("3"),
            "Reporte Suspensiones": lambda: print("4"),
            "Reporte Egresos": lambda: print("5"),
            "Reporte Tickets": lambda: print("6"),
            "Reporte Historial de Usuarios": lambda: print("7")
        }

        for key in functions.keys():
            self.Menu_function_report.add_command(
                label=key,
                command=functions[key]
            )

    def addCommandsToExportMenu(self):
        functions = {
            "Exportar Base de Datos": lambda: print("1"),
            "Respaldar Base de Datos": lambda: print("2"),
        }

        for key in functions.keys():
            self.Menu_function_export.add_command(
                label=key,
                command=functions[key]
            )

    def addCommadsToHelpMenu(self):
        functions = {
            "Sobre el sistema": lambda: print("1"),
            "Ayuda": lambda: print("2")
        }

        for key in functions.keys():
            self.Menu_function_help.add_command(
                label=key,
                command=functions[key]
            )

class GUI_lateralmenu(GUI_root):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)

        # frames
        self.frame_lateral: tk.Frame = tk.Frame(self.root)
        self.frame_lateral.grid(row=0, column=0, sticky="WNS", ipadx=10, ipady=10)
        self.frame_lateral.config(
            bg="red",
            width=300
        )

        self.frame_lateral.grid_rowconfigure(1, weight=1)
        self.frame_lateral.grid_columnconfigure(0, weight=1)

        # title
        self.label_title: tk.Label = tk.Label(self.frame_lateral, text="SISTEMA DE GESTIÓN\nAUTOMATIZADA DE\nTICKETS DE ALIMENTACIÓN")
        self.label_title.grid(row=0, column=0, sticky="WENS", padx=15, pady=15)
        self.label_title.config(
            justify="left"
        )

        # main functions
        self.frame_buttons: tk.Frame = tk.Frame(self.frame_lateral)
        self.frame_buttons.grid(row=1, column=0, sticky="WENS")
        self.frame_buttons.config(
            bg="green"
        )

        self.button_new_income: tk.Button = tk.Button(self.frame_buttons, text="Nuevo Ingreso")
        self.button_new_income.grid(row=0, column=0, sticky="WENS")

        # time and hour
        self.frame_time_hour: tk.Frame = tk.Frame(self.frame_lateral)
        self.frame_time_hour.grid(row=2, column=0, sticky="WENS")

class GUI_mainmenu(GUI_barmenu, GUI_lateralmenu):
    def __init__(self, root) -> None:
        super().__init__(root)


if __name__ == "__main__":
    root = tk.Tk()
    GUI_mainmenu(root)
    root.mainloop()
