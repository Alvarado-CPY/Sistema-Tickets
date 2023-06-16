import tkinter as tk
from tkinter import ttk
import sqlite3


class GUI_root:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Cambiar Trabajador de Categoría")
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.centralizeWindow()

    def centralizeWindow(self):
        windows_width = 450
        windows_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_coordinate = int((screen_width/2) - (windows_width/2))
        y_coordinate = int((screen_height/2) - (windows_height/2))-40

        self.root.geometry(
            f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")

    def destroyRoot(self):
        self.root.quit()
        self.root.destroy()

class GUI_frameWorkerData:
    def __init__(self, frame: tk.Frame, data: tuple) -> None:
        # frame master
        self.frame = frame
        self.data = data

        # inner frame
        self.frame_worker_data: tk.LabelFrame = tk.LabelFrame(self.frame, text="Datos del Trabajador")
        self.frame_worker_data.grid(row=0, column=0, sticky="WENS")

        self.frame_worker_data.grid_columnconfigure((0,1), weight=1)

        # widgets
        # ci
        self.label_ci: tk.Label = tk.Label(self.frame_worker_data, text="CÉDULA")
        self.label_ci.grid(row=0, column=0)

        self.entry_ci: tk.Entry = tk.Entry(self.frame_worker_data)
        self.entry_ci.grid(row=0, column=1, sticky="WENS", pady=5, padx=5)

        # name
        self.label_name: tk.Label = tk.Label(self.frame_worker_data, text="NOMBRE")
        self.label_name.grid(row=1, column=0)

        self.entry_name: tk.Entry = tk.Entry(self.frame_worker_data)
        self.entry_name.grid(row=1, column=1, sticky="WENS", pady=5, padx=5)

        # functions
        self.setWorkerData()

    def setWorkerData(self):
        self.entry_ci.insert(0, self.data[0])
        self.entry_name.insert(0, self.data[1])

        self.entry_ci.config(state="readonly")
        self.entry_name.config(state="readonly")


class GUI_SuspensionOption:
    def __init__(self, frame: tk.Frame) -> None:
        # frame master
        self.frame = frame

        # inner frame
        self.frame_suspension_option: tk.LabelFrame = tk.LabelFrame(self.frame, text="Datos Necesarios Para Suspender")
        self.frame_suspension_option.grid(row=0, column=0, sticky="WENS")

        self.frame_suspension_option.grid_columnconfigure(0, weight=1)

        # widgets
        # desincorporation date
        self.label_desincorporation_date: tk.Label = tk.Label(self.frame_suspension_option, text="FECHA DE DESINCORPORACIÓN")
        self.label_desincorporation_date.grid(row=0, column=0, sticky="W", pady=5)

        self.entry_desincorporation_date: tk.Entry = tk.Entry(self.frame_suspension_option)
        self.entry_desincorporation_date.grid(row=1, column=0, sticky="WENS", ipadx=5)

        # suspension reason
        self.label_suspension_reason: tk.Label = tk.Label(self.frame_suspension_option, text="RAZÓN DE SUSPENSIÓN")
        self.label_suspension_reason.grid(row=2, column=0, sticky="W", pady=5)

        self.entry_suspension_reason: tk.Entry = tk.Entry(self.frame_suspension_option)
        self.entry_suspension_reason.grid(row=3, column=0, sticky="WENS", ipadx=5)

        # support number
        self.label_support_number: tk.Label = tk.Label(self.frame_suspension_option, text="NÚMERO DE SOPORTE")
        self.label_support_number.grid(row=4, column=0, sticky="W", pady=5)

        self.entry_support_number: tk.Entry = tk.Entry(self.frame_suspension_option)
        self.entry_support_number.grid(row=5, column=0, sticky="WENS", ipadx=5)

class GUI_categoryOptions:
    def __init__(self, frame: tk.Frame, origin_category: str) -> None:
        # frame master
        self.frame = frame
        self.origin_category = origin_category

        # inner frame
        self.frame_category_choice: tk.LabelFrame = tk.LabelFrame(self.frame, text="Elegir Nueva Categoría")
        self.frame_category_choice.grid(row=1, column=0, sticky="WENS")

        self.frame_category_choice.grid_rowconfigure(1, weight=1)
        self.frame_category_choice.grid_columnconfigure((0,1), weight=1)

        # widgets
        # category choicer
        self.label_cagetory: tk.Label = tk.Label(self.frame_category_choice, text="CAMBIAR A")
        self.label_cagetory.grid(row=0, column=0)

        self.combobox_categories: ttk.Combobox = ttk.Combobox(self.frame_category_choice)
        self.combobox_categories.grid(row=0, column=1, sticky="WENS", padx=5)

        # changable frame
        self.frame_category_container: tk.Frame = tk.Frame(self.frame_category_choice)
        self.frame_category_container.grid(row=1, column=0, sticky="WENS", columnspan=2, padx=5, pady=5)

        self.frame_category_container.grid_rowconfigure(0, weight=1)
        self.frame_category_container.grid_columnconfigure(0, weight=1)

        self.insertComboBoxChoices()

        # events
        self.combobox_categories.bind("<<ComboboxSelected>>", lambda e: self.getComboBoxToChange())

    def cleanContainerFrame(self):
        for children in self.frame_category_container.winfo_children():
            children.destroy()

    def setCorrespondingCategoryOptions(self, category: str):
        self.cleanContainerFrame()
        if category == "Suspension":
            GUI_SuspensionOption(self.frame_category_container)

    def getComboBoxToChange(self):
        self.setCorrespondingCategoryOptions(self.combobox_categories.get())

    def insertComboBoxChoices(self):
        choices = []
        if self.origin_category == "Nuevo Ingreso":
            choices = (
                "Suspension",
                "Egreso"
            )
        elif self.origin_category == "Reactivacion":
            choices = (
                "Suspension",
                "Egreso"
            )
        elif self.origin_category == "Suspension":
            choices = (
                "Reactivacion",
                "Egreso"
            )
        else:
            choices = [
                "Reactivacion"
            ]

        self.combobox_categories.config(
            values=choices
        )
        if len(choices) > 1:
            choices = choices[0]

        self.combobox_categories.set(choices)
        self.setCorrespondingCategoryOptions(choices)

class GUI_change_category(GUI_root):
    def __init__(self, root: tk.Tk, data: str) -> None:
        super().__init__(root)

        # variables
        self.worker_data_to_change_category = data[0]
        self.worker_origin_category = data[1]

        # initial validation before everything loads
        self.validateIfOptionIsValid()

        # frames
        self.frame_main: tk.Frame = tk.Frame(self.root)
        self.frame_main.grid(row=0, column=0, sticky="WENS", pady=5, padx=5)

        self.frame_main.grid_rowconfigure(1, weight=1)
        self.frame_main.grid_columnconfigure(0, weight=1)

        # functions
        self.loadDefaultFrames()

    def validateIfOptionIsValid(self):
        valid_options = (
            "Nuevo Ingreso",
            "Reactivacion",
            "Suspension",
            "Egreso"
        )
        if self.worker_origin_category not in valid_options:
            self.destroyRoot()
            raise Exception("Opción de categoría no soportada")

    def loadDefaultFrames(self):
        GUI_frameWorkerData(frame=self.frame_main, data=self.worker_data_to_change_category)
        GUI_categoryOptions(frame=self.frame_main, origin_category=self.worker_origin_category)

