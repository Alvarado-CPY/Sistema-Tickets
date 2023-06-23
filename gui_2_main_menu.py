import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from app_global_variables import guiConfig, dbPath
from helpers.import_data import ImportData
from helpers.format import formatDate, formatAddMissingZero
from helpers.search_engine import SearchEngine
from helpers.gui_loader import loadGUI, setfullScreen
from gui_3_interface_new_income import GUI_workerForm
from gui_4_interface_change_category import GUI_change_category
from gui_5_reports import GUI_reportsMenu

class GUI_root:
    def __init__(self, root: tk.Tk) -> None:

        self.root = root
        self.root.title(
            "Sistema De Gestión Automatizada De Tickets De Alimentación")
        setfullScreen(self.root)
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

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
        self.Menu_function_report: tk.Menu = tk.Menu(self.Menu, tearoff=False)
        self.Menu_function_export: tk.Menu = tk.Menu(self.Menu, tearoff=False)
        self.Menu_function_help: tk.Menu = tk.Menu(self.Menu, tearoff=False)

        self.addCommandsToMenus()

        # adding menu functions to menubar
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
        self.addCommandsToReportMenu()
        self.addCommandsToExportMenu()
        self.addCommadsToHelpMenu()

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

        self.button_general: tk.Button = tk.Button(
            self.frame_buttons, text="General")
        self.button_general.grid(
            row=0, column=0, sticky="WENS", padx=10, pady=5)
        self.button_general.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_new_income: tk.Button = tk.Button(
            self.frame_buttons, text="Nuevo Ingreso")
        self.button_new_income.grid(
            row=1, column=0, sticky="WENS", padx=10, pady=5)
        self.button_new_income.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_reactivation: tk.Button = tk.Button(
            self.frame_buttons, text="Reactivaciones")
        self.button_reactivation.grid(
            row=2, column=0, sticky="WENS", padx=10, pady=5)
        self.button_reactivation.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_suspension: tk.Button = tk.Button(
            self.frame_buttons, text="Suspensiones")
        self.button_suspension.grid(
            row=3, column=0, sticky="WENS", padx=10, pady=5)
        self.button_suspension.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_discharge: tk.Button = tk.Button(
            self.frame_buttons, text="Egresos")
        self.button_discharge.grid(
            row=4, column=0, sticky="WENS", padx=10, pady=5)
        self.button_discharge.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_tickets: tk.Button = tk.Button(
            self.frame_buttons, text="Tickets")
        self.button_tickets.grid(
            row=5, column=0, sticky="WENS", padx=10, pady=5)
        self.button_tickets.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.button_users: tk.Button = tk.Button(
            self.frame_buttons, text="Usuarios")
        self.button_users.grid(row=6, column=0, sticky="WENS", padx=10, pady=5)
        self.button_users.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )


class GUI_workersTableData:
    def __init__(self, frame: tk.Frame, root=None):
        self.frame = frame

        # widgets
        self.frame_workers: tk.Frame = tk.Frame(self.frame)
        self.frame_workers.grid(
            row=0, column=0, sticky="WENS", padx=20, pady=20)
        self.frame_workers.config(
            bg=guiConfig().getColors()["main_color"]
        )

        self.frame_workers.grid_rowconfigure((1), weight=1)
        self.frame_workers.grid_columnconfigure(0, weight=1)

        self.label_title: tk.Label = tk.Label(
            self.frame_workers, text="TABLA GENERAL DE NOMINA")
        self.label_title.grid(row=0, column=0, sticky="WENS", pady=10)
        self.label_title.config(
            bg=guiConfig().getColors()["main_color"],
            font=[guiConfig().getFonts()["main_font"], 18]
        )

        self.table_workers: ttk.Treeview = ttk.Treeview(
            self.frame_workers, selectmode="browse")
        self.table_workers.grid(row=1, column=0, sticky="WENS")
        self.table_workers.config(
            columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                     "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        )

        # headings
        self.table_workers.heading("#1", text="ID")
        self.table_workers.heading("#2", text="NACIONALIDAD")
        self.table_workers.heading("#3", text="CÉDULA")
        self.table_workers.heading("#4", text="NOMBRE COMPLETO")
        self.table_workers.heading("#5", text="FECHA DE NACIMIENTO")
        self.table_workers.heading("#6", text="EDAD")
        self.table_workers.heading("#7", text="SEXO")
        self.table_workers.heading("#8", text="FECHA DE INGRESO")
        self.table_workers.heading("#9", text="DENOMINACIÓN DE CARGO")
        self.table_workers.heading("#10", text="CARGA HORARIA")
        self.table_workers.heading("#11", text="HORARIO LABORAL")
        self.table_workers.heading("#12", text="ESPECIALIDAD")
        self.table_workers.heading("#13", text="TIPO DE PERSONAL")
        self.table_workers.heading("#14", text="UBICACIÓN ADMINISTRATIVA")
        self.table_workers.heading("#15", text="UBICACIÓN FÍSICA")
        self.table_workers.heading("#16", text="COMISIÓN DE SERVICIO")
        self.table_workers.heading("#17", text="ESTADO")
        self.table_workers.heading("#18", text="CUENTA BANCARIA")
        self.table_workers.heading("#19", text="CODIGO DEL BANCO")
        self.table_workers.heading("#20", text="BANCO")

        # columns
        self.table_workers.column("#0", width=0, stretch=False)
        self.table_workers.column("#1", width=80, anchor="center")
        self.table_workers.column("#2", width=100, anchor="center")
        self.table_workers.column("#3", width=100, anchor="center")
        self.table_workers.column("#4", width=300)
        self.table_workers.column("#5", width=140, anchor="center")
        self.table_workers.column("#6", width=80, anchor="center")
        self.table_workers.column("#7", width=80, anchor="center")
        self.table_workers.column("#8", width=140, anchor="center")
        self.table_workers.column("#9", width=370)
        self.table_workers.column("#10", width=120, anchor="center")
        self.table_workers.column("#11", width=120, anchor="center")
        self.table_workers.column("#13", width=300)
        self.table_workers.column("#16", anchor="center")
        self.table_workers.column("#17", width=150, anchor="center")
        self.table_workers.column("#18", anchor="center")
        self.table_workers.column("#19", width=150, anchor="center")
        self.table_workers.column("#20", width=150, anchor="center")

        # search engine
        self.search_engine = SearchEngine(self.table_workers)
        self.table_workers.bind(
            "<Key>", lambda key: self.search_engine.searchCI(key))

        # avoid resizing
        self.table_workers.bind("<Button-1>", self.avoidRezisable)

        # scroll bars
        self.scrollbar_x: ttk.Scrollbar = ttk.Scrollbar(
            self.frame_workers, orient="horizontal", command=self.table_workers.xview)
        self.scrollbar_x.grid(row=2, column=0, sticky="WE")

        self.scrollbar_y: ttk.Scrollbar = ttk.Scrollbar(
            self.frame_workers, orient="vertical", command=self.table_workers.yview)
        self.scrollbar_y.grid(row=1, column=1, sticky="NS")

        self.table_workers.config(
            xscrollcommand=self.scrollbar_x.set,
            yscrollcommand=self.scrollbar_y.set
        )

        self.loadWorkerData()

    def avoidRezisable(self, event):
        if self.table_workers.identify_region(event.x, event.y) == "separator":
            return "break"

    def loadWorkerData(self):
        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            cursor.execute("SELECT * FROM workers")
            workers = cursor.fetchall()

            for worker in workers:
                self.table_workers.insert(parent="", index=tk.END, values=(
                    worker[0],
                    worker[1],
                    worker[2],
                    worker[3],
                    formatDate(worker[4]),
                    worker[5],
                    worker[6],
                    formatDate(worker[7]),
                    worker[8],
                    worker[9],
                    worker[10],
                    worker[11],
                    worker[12],
                    worker[13],
                    worker[14],
                    worker[15],
                    worker[16],
                    formatAddMissingZero(worker[17]),
                    formatAddMissingZero(worker[18]),
                    worker[19],
                ))


class GUI_displayChargeButton:
    def __init__(self, frame: tk.Frame, button_list: list[tk.Button], Menu: tk.Menu) -> None:
        self.frame = frame
        self.menu = Menu
        self.button_list = button_list

        # widgets
        self.frame_widgets: tk.Frame = tk.Frame(self.frame)
        self.frame_widgets.grid(row=0, column=0, sticky="WENS")
        self.frame_widgets.config(
            bg=guiConfig().getColors()["main_color"]
        )

        self.frame_widgets.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame_widgets.grid_columnconfigure(0, weight=1)

        self.frame_container: tk.Frame = tk.Frame(self.frame_widgets)
        self.frame_container.grid(row=1, column=0, sticky="WE")
        self.frame_container.config(
            bg=guiConfig().getColors()["main_color"]
        )

        self.frame_container.grid_columnconfigure(0, weight=1)

        self.label_charge_msg: tk.Label = tk.Label(
            self.frame_container, text="No se encuentran datos cargados de nomina en la base de datos\nAntes de poder trabajar con el sistema debe de cargar una nomina de tickets.\nEsto puede tardar unos segundos, no cierre el sistema durante el proceso")
        self.label_charge_msg.grid(row=0, column=0, sticky="WENS")
        self.label_charge_msg.config(
            bg=guiConfig().getColors()["main_color"],
            font=[guiConfig().getFonts()["main_font"], 13],
            justify="left"
        )

        self.button_charge: tk.Button = tk.Button(
            self.frame_container, text="Cargar Nomina")
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

            self.cleanFrame()
            GUI_workersTableData(self.frame)

    def toggleMenu(self, menu_state: str):
        self.menu.entryconfig("Reporte", state=menu_state)
        self.menu.entryconfig("Base de Datos", state=menu_state)
        self.menu.entryconfig("Ayuda", state=menu_state)

    def toggleButtons(self, button_state: str):
        for button in self.button_list:
            button.config(state=button_state)

    def cleanFrame(self):
        self.frame_widgets.destroy()


class GUI_categoryButtons:
    def __init__(self, frame):
        self.frame = frame

        self.frame_buttons: tk.Frame = tk.Frame(self.frame)
        self.frame_buttons.grid(
            row=0, column=0, sticky="WENS", columnspan=2, pady=5)

        self.frame_buttons.grid_rowconfigure(0, weight=1)
        self.frame_buttons.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.button_first_category_function: tk.Button = tk.Button(
            self.frame_buttons)
        self.button_first_category_function.grid(
            row=0, column=0, sticky="WENS", padx=2)
        self.button_first_category_function.config(
            font=[guiConfig().getFonts()["secondary_font"], 12]
        )

        self.button_second_category_function: tk.Button = tk.Button(
            self.frame_buttons)
        self.button_second_category_function.grid(
            row=0, column=1, sticky="WENS", padx=2)
        self.button_second_category_function.config(
            font=[guiConfig().getFonts()["secondary_font"], 12]
        )

        self.button_third_category_function: tk.Button = tk.Button(
            self.frame_buttons)
        self.button_third_category_function.grid(
            row=0, column=2, sticky="WENS", padx=2)
        self.button_third_category_function.config(
            font=[guiConfig().getFonts()["secondary_font"], 12]
        )

        self.button_four_category_function: tk.Button = tk.Button(
            self.frame_buttons)
        self.button_four_category_function.grid(
            row=0, column=3, sticky="WENS", padx=2)
        self.button_four_category_function.config(
            font=[guiConfig().getFonts()["secondary_font"], 12]
        )


class GUI_newIncome(GUI_categoryButtons):
    def __init__(self, frame, root: tk.Tk):
        self.frame: tk.Frame = frame
        self.root = root

        # frames
        self.frame_income_container: tk.Frame = tk.Frame(self.frame)
        self.frame_income_container.grid(
            row=0, column=0, sticky="WENS", padx=20, pady=20)
        self.frame_income_container.config(
            bg=guiConfig().getColors()["main_color"]
        )

        self.frame_income_container.grid_rowconfigure(1, weight=1)
        self.frame_income_container.grid_columnconfigure(0, weight=1)

        # for the table and the buttons
        self.frame_income_components: tk.Frame = tk.Frame(
            self.frame_income_container)
        self.frame_income_components.grid(row=1, column=0, sticky="WENS")
        self.frame_income_components.config(
            bg=guiConfig().getColors()["main_color"]
        )

        self.frame_income_components.grid_rowconfigure(1, weight=1)
        self.frame_income_components.grid_columnconfigure(0, weight=1)

        # Widgets tittle
        self.label_title: tk.Label = tk.Label(
            self.frame_income_container, text="TABLA NUEVO INGRESO")
        self.label_title.grid(row=0, column=0, sticky="WENS", pady=10)
        self.label_title.config(
            bg=guiConfig().getColors()["main_color"],
            font=[guiConfig().getFonts()["main_font"], 18]
        )

        # Widgest buttons
        super().__init__(self.frame_income_components)

        # table
        self.table_new_income: ttk.Treeview = ttk.Treeview(
            self.frame_income_components, selectmode="browse")
        self.table_new_income.grid(row=1, column=0, sticky="WENS")
        self.table_new_income.config(
            columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                     "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
        )

        # headings
        self.table_new_income.heading("#1", text="ID")
        self.table_new_income.heading("#2", text="NACIONALIDAD")
        self.table_new_income.heading("#3", text="CÉDULA")
        self.table_new_income.heading("#4", text="NOMBRE COMPLETO")
        self.table_new_income.heading("#5", text="FECHA DE NACIMIENTO")
        self.table_new_income.heading("#6", text="EDAD")
        self.table_new_income.heading("#7", text="SEXO")
        self.table_new_income.heading("#8", text="FECHA DE INGRESO")
        self.table_new_income.heading("#9", text="DENOMINACIÓN DE CARGO")
        self.table_new_income.heading("#10", text="CARGA HORARIA")
        self.table_new_income.heading("#11", text="HORARIO LABORAL")
        self.table_new_income.heading("#12", text="ESPECIALIDAD")
        self.table_new_income.heading("#13", text="TIPO DE PERSONAL")
        self.table_new_income.heading("#14", text="UBICACIÓN ADMINISTRATIVA")
        self.table_new_income.heading("#15", text="UBICACIÓN FÍSICA")
        self.table_new_income.heading("#16", text="COMISIÓN DE SERVICIO")
        self.table_new_income.heading("#17", text="ESTADO")
        self.table_new_income.heading("#18", text="CUENTA BANCARIA")
        self.table_new_income.heading("#19", text="CODIGO DEL BANCO")
        self.table_new_income.heading("#20", text="BANCO")
        self.table_new_income.heading("#21", text="TIPO DE CUENTA")

        # columns
        self.table_new_income.column("#0", width=0, stretch=False)
        self.table_new_income.column("#1", width=80, anchor="center")
        self.table_new_income.column("#2", width=100, anchor="center")
        self.table_new_income.column("#3", width=100, anchor="center")
        self.table_new_income.column("#4", width=300)
        self.table_new_income.column("#5", width=140, anchor="center")
        self.table_new_income.column("#6", width=80, anchor="center")
        self.table_new_income.column("#7", width=80, anchor="center")
        self.table_new_income.column("#8", width=140, anchor="center")
        self.table_new_income.column("#9", width=370)
        self.table_new_income.column("#10", width=120, anchor="center")
        self.table_new_income.column("#11", width=120, anchor="center")
        self.table_new_income.column("#13", width=300)
        self.table_new_income.column("#16", anchor="center")
        self.table_new_income.column("#17", width=150, anchor="center")
        self.table_new_income.column("#18", anchor="center")
        self.table_new_income.column("#19", width=150, anchor="center")
        self.table_new_income.column("#20", width=150, anchor="center")
        self.table_new_income.column("#21", width=150, anchor="center")

        # avoid resizing
        self.table_new_income.bind("<Button-1>", self.avoidRezisable)

        # scroll bars
        self.scrollbar_x: ttk.Scrollbar = ttk.Scrollbar(
            self.frame_income_components, orient="horizontal", command=self.table_new_income.xview)
        self.scrollbar_x.grid(row=2, column=0, sticky="WE")

        self.scrollbar_y: ttk.Scrollbar = ttk.Scrollbar(
            self.frame_income_components, orient="vertical", command=self.table_new_income.yview)
        self.scrollbar_y.grid(row=1, column=1, sticky="NS")

        self.table_new_income.config(
            xscrollcommand=self.scrollbar_x.set,
            yscrollcommand=self.scrollbar_y.set
        )

        self.loadNewIncomeData()
        self.setFunctionalityToCategoryButtons()

        # search engine
        self.search_engine = SearchEngine(self.table_new_income)
        self.table_new_income.bind(
            "<Key>", lambda key: self.search_engine.searchCI(key))

    def avoidRezisable(self, event):
        if self.table_new_income.identify_region(event.x, event.y) == "separator":
            return "break"

    def loadNewIncomeData(self):
        for item in self.table_new_income.get_children():
            self.table_new_income.delete(item)

        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            new_income = cursor.execute("SELECT * FROM newIncome").fetchall()
            new_income_data = []

            for worker in new_income:
                data = cursor.execute(
                    "SELECT * FROM workers where worker_ci=?", (worker[0],)).fetchall()
                data.append(worker[1])
                new_income_data.append(data)

            for worker_data in new_income_data:
                account_type = worker_data[1]
                worker_data = worker_data[0]
                self.table_new_income.insert(parent="", index=tk.END, values=(
                    worker_data[0],
                    worker_data[1],
                    worker_data[2],
                    worker_data[3],
                    formatDate(worker_data[4]),
                    worker_data[5],
                    worker_data[6],
                    formatDate(worker_data[7]),
                    worker_data[8],
                    worker_data[9],
                    worker_data[10],
                    worker_data[11],
                    worker_data[12],
                    worker_data[13],
                    worker_data[14],
                    worker_data[15],
                    worker_data[16],
                    formatAddMissingZero(worker_data[17]),
                    formatAddMissingZero(worker_data[18]),
                    worker_data[19],
                    account_type,
                ))

    def setFunctionalityToCategoryButtons(self):
        self.button_first_category_function.config(
            text="REPORTE",
            command=self.reportNewIncome
        )

        self.button_second_category_function.config(
            text="CAMBIAR CATEGORÍA",
            command=self.changeCategory
        )

        self.button_third_category_function.config(
            text="MODIFICIAR",
            command=self.getWorkerDataToUpdate
        )

        self.button_four_category_function.config(
            text="AÑADIR TRABAJADOR",
            command=self.loadWorkerFormToInsertNewWorker
        )

    def reportNewIncome(self):
        loadGUI(root=self.root, GUI_to_load=GUI_reportsMenu, data="Nuevo Ingreso")

    def changeCategory(self):
        focus = self.table_new_income.item(self.table_new_income.focus())
        if focus['values'] == '':
            messagebox.showerror(
                "Error", "Debe seleccionar a un trabajador para poder cambiar su categoría")
            return False

        worker_data = (focus['values'][2], focus['values']
                       [3], focus['values'][-1])
        loadGUI(root=self.root, GUI_to_load=GUI_change_category,
                data=(worker_data, "Nuevo Ingreso"))
        self.loadNewIncomeData()

    def loadWorkerFormToInsertNewWorker(self):
        loadGUI(root=self.root, GUI_to_load=GUI_workerForm, option="add")
        self.loadNewIncomeData()

    def getWorkerDataToUpdate(self):
        focus = self.table_new_income.item(self.table_new_income.focus())
        if focus['values'] == '':
            messagebox.showerror(
                "Error", "Debe seleccionar a un trabajador para poder actualizar sus datos")
            return False

        worker_data = focus["values"]
        loadGUI(root=self.root, GUI_to_load=GUI_workerForm,
                option="update", data=worker_data)
        self.loadNewIncomeData()


class GUI_mainMenu(GUI_barmenu, GUI_lateralmenu):
    def __init__(self, root) -> None:
        super().__init__(root)
        # variables
        self.button_list: list = [
            self.button_general,
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

        self.frame_main.grid_rowconfigure(0, weight=1)
        self.frame_main.grid_columnconfigure(0, weight=1)

        self.setLateralFunctions()

        # display one frame or another
        self.seeIfThereIsChargedData()

    def seeIfThereIsChargedData(self):
        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            cursor.execute("SELECT * FROM workers")
            exist_data = cursor.fetchone()

            if not exist_data:
                GUI_displayChargeButton(
                    self.frame_main, button_list=self.button_list, Menu=self.Menu)
            else:
                GUI_workersTableData(self.frame_main, self.root)

    def setLateralFunctions(self):
        self.button_general.config(
            command=lambda: self.displayGuiPart(
                GUI_workersTableData)
        )
        self.button_new_income.config(
            command=lambda: self.displayGuiPart(GUI_newIncome)
        )

    def displayGuiPart(self, guiToDisplay):
        self.clearFrameMainChildren()
        guiToDisplay(self.frame_main, root=self.root)

    def clearFrameMainChildren(self):
        for children in self.frame_main.winfo_children():
            children.grid_forget()
            children.grid_remove()
            children.destroy()
            del children


if __name__ == "__main__":
    root = tk.Tk()
    GUI_mainMenu(root)
    root.mainloop()
