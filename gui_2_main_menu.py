import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import os
from app_global_variables import guiConfig, dbPath
from helpers.import_data import ImportData

class GUI_root:
    def __init__(self, root: tk.Tk) -> None:

        self.root = root
        self.root.title(
            "Sistema De Gestión Automatizada De Tickets De Alimentación")
        self.setfullScreen()
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

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
        self.frame_lateral.grid(
            row=0, column=0, sticky="WNS", ipadx=10, ipady=10)
        self.frame_lateral.config(
            bg=guiConfig().getColors()["secondary_color"]
        )

        self.frame_lateral.grid_rowconfigure((1, 2), weight=1)
        self.frame_lateral.grid_columnconfigure(0, weight=1)

        # title
        self.label_title: tk.Label = tk.Label(
            self.frame_lateral, text="SISTEMA DE GESTIÓN\nAUTOMATIZADA DE\nTICKETS DE ALIMENTACIÓN")
        self.label_title.grid(row=0, column=0, sticky="WENS", pady=15)
        self.label_title.config(
            justify="left",
            font=[guiConfig().getFonts()["main_font"], 13],
            bg=guiConfig().getColors()["secondary_color"]
        )

        # main functions
        self.frame_buttons: tk.Frame = tk.Frame(self.frame_lateral)
        self.frame_buttons.grid(row=1, column=0, sticky="WENS")
        self.frame_buttons.config(
            bg=guiConfig().getColors()["secondary_color"]
        )

        self.frame_buttons.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.frame_buttons.grid_columnconfigure(0, weight=1)

        self.button_new_income: tk.Button = tk.Button(
            self.frame_buttons, text="Nuevo Ingreso")
        self.button_new_income.grid(
            row=0, column=0, sticky="WENS", padx=10, pady=5)
        self.button_new_income.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_reactivation: tk.Button = tk.Button(
            self.frame_buttons, text="Reactivaciones")
        self.button_reactivation.grid(
            row=1, column=0, sticky="WENS", padx=10, pady=5)
        self.button_reactivation.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_suspension: tk.Button = tk.Button(
            self.frame_buttons, text="Suspensiones")
        self.button_suspension.grid(
            row=2, column=0, sticky="WENS", padx=10, pady=5)
        self.button_suspension.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_discharge: tk.Button = tk.Button(
            self.frame_buttons, text="Egresos")
        self.button_discharge.grid(
            row=3, column=0, sticky="WENS", padx=10, pady=5)
        self.button_discharge.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_tickets: tk.Button = tk.Button(
            self.frame_buttons, text="Tickets")
        self.button_tickets.grid(
            row=4, column=0, sticky="WENS", padx=10, pady=5)
        self.button_tickets.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_users: tk.Button = tk.Button(
            self.frame_buttons, text="Usuarios")
        self.button_users.grid(row=5, column=0, sticky="WENS", padx=10, pady=5)
        self.button_users.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )


class GUI_displayChargeButton:
    def __init__(self, frame: tk.Frame, button_list: list[tk.Button], Menu: tk.Menu) -> None:
        self.frame = frame
        self.menu = Menu
        self.button_list = button_list

        self.frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # widgets
        self.frame_widgets: tk.Frame = tk.Frame(self.frame)
        self.frame_widgets.grid(row=1, column=0, sticky="NS")
        self.frame_widgets.config(
            bg=guiConfig().getColors()["main_color"]
        )

        self.frame_widgets.grid_rowconfigure(0, weight=1)
        self.frame_widgets.grid_columnconfigure(0, weight=1)

        self.label_charge_msg: tk.Label = tk.Label(
            self.frame_widgets, text="No se encuentran datos cargados de nomina en la base de datos\nAntes de poder trabajar con el sistema debe de cargar una nomina de tickets.\nEsto puede tardar unos segundos, no cierre el sistema durante el proceso")
        self.label_charge_msg.grid(row=0, column=0)
        self.label_charge_msg.config(
            bg=guiConfig().getColors()["main_color"],
            font=[guiConfig().getFonts()["main_font"], 13],
            justify="left"
        )

        self.button_charge: tk.Button = tk.Button(
            self.frame_widgets, text="Cargar Nomina")
        self.button_charge.grid(row=1, column=0)
        self.button_charge.config(
            width=15,
            font=[guiConfig().getFonts()["secondary_font"], 14],
            command=self.loadWorkerData
        )

        self.toggleMenu("disabled")
        self.toggleButtons("disabled")

    def loadWorkerData(self):
        import_function = ImportData(dbPath())

        if import_function.operate() != False:
            messagebox.showinfo("Atención", "Datos cargados con éxito")
            self.toggleMenu("normal")
            self.toggleButtons("normal")

    def toggleMenu(self, menu_state: str):
        self.menu.entryconfig("Nuevo", state=menu_state)
        self.menu.entryconfig("Reporte", state=menu_state)
        self.menu.entryconfig("Base de Datos", state=menu_state)
        self.menu.entryconfig("Ayuda", state=menu_state)

    def toggleButtons(self, button_state: str):
        for button in self.button_list:
            button.config(state=button_state)

class GUI_mainmenu(GUI_barmenu, GUI_lateralmenu):
    def __init__(self, root) -> None:
        super().__init__(root)
        # variables
        self.button_list: list = [
            self.button_new_income,
            self.button_discharge,
            self.button_reactivation,
            self.button_suspension,
            self.button_tickets,
            self.button_users
        ]

        # frames
        self.frame_main: tk.Frame = tk.Frame(self.root)
        self.frame_main.grid(row=0, column=1, sticky="WENS")
        self.frame_main.config(
            bg=guiConfig().getColors()["main_color"]
        )

        # display one frame or another
        self.seeIfThereIsChargedData()

    def seeIfThereIsChargedData(self):
        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            cursor.execute("SELECT * FROM workers")
            exist_data = cursor.fetchone()

            if not exist_data:
                GUI_displayChargeButton(self.frame_main, button_list=self.button_list, Menu=self.Menu)


if __name__ == "__main__":
    root = tk.Tk()
    GUI_mainmenu(root)
    root.mainloop()
