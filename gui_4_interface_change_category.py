import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from app_global_variables import guiConfig, dbPath
from helpers.writer_interface import INTERFACE_writer
from helpers.validate_worker_data import *


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
        self.frame_worker_data: tk.LabelFrame = tk.LabelFrame(
            self.frame, text="Datos del Trabajador")
        self.frame_worker_data.grid(row=0, column=0, sticky="WENS")

        self.frame_worker_data.grid_columnconfigure((0, 1), weight=1)

        # widgets
        # ci
        self.label_ci: tk.Label = tk.Label(
            self.frame_worker_data, text="CÉDULA")
        self.label_ci.grid(row=0, column=0)

        self.entry_ci: tk.Entry = tk.Entry(self.frame_worker_data)
        self.entry_ci.grid(row=0, column=1, sticky="WENS", pady=5, padx=5)

        # name
        self.label_name: tk.Label = tk.Label(
            self.frame_worker_data, text="NOMBRE")
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


class GUI_reactivationOption(INTERFACE_writer):
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        # variables
        self.data = data
        self.variable_reactivation_date: tk.StringVar = tk.StringVar()
        self.variable_account_type: tk.StringVar = tk.StringVar()

        # frame master
        self.frame = frame

        # inner frame
        self.frame_reactivation_option: tk.LabelFrame = tk.LabelFrame(
            self.frame, text="Datos Necesarios para Reactivar")
        self.frame_reactivation_option.grid(row=0, column=0, sticky="WENS")
        self.frame_reactivation_option.grid_columnconfigure(0, weight=1)

        # widgets
        # reactivation date
        self.label_reactivation_date: tk.Label = tk.Label(
            self.frame_reactivation_option, text="FECHA DE REACTIVACIÓN")
        self.label_reactivation_date.grid(row=0, column=0, sticky="W", pady=5)
        self.label_reactivation_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_reactivation_date: tk.Entry = tk.Entry(
            self.frame_reactivation_option, textvariable=self.variable_reactivation_date)
        self.entry_reactivation_date.grid(
            row=1, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_reactivation_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # account type
        self.label_account_type: tk.Label = tk.Label(
            self.frame_reactivation_option, text="TIPO DE CUENTA")
        self.label_account_type.grid(row=2, column=0, sticky="W", pady=5)
        self.label_account_type.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_account_type: tk.Entry = tk.Entry(
            self.frame_reactivation_option, textvariable=self.variable_account_type)
        self.entry_account_type.grid(
            row=3, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_account_type.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # functions
        self.loadInfoToEntrys()

        # events
        self.variable_reactivation_date.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="reactivation_date", variable=self.variable_reactivation_date))

        self.variable_account_type.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="account_type", variable=self.variable_account_type))

    def loadInfoToEntrys(self):
        self.entry_reactivation_date.insert(0, self.data["reactivation_date"])
        self.entry_account_type.insert(0, self.data["account_type"])


class GUI_suspensionOption(INTERFACE_writer):
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        # variables
        self.data = data
        self.variable_desincorporation_date: tk.StringVar = tk.StringVar()
        self.variable_suspension_reason: tk.StringVar = tk.StringVar()
        self.variable_support_number: tk.StringVar = tk.StringVar()

        # frame master
        self.frame = frame

        # inner frame
        self.frame_suspension_option: tk.LabelFrame = tk.LabelFrame(
            self.frame, text="Datos Necesarios Para Suspender")
        self.frame_suspension_option.grid(row=0, column=0, sticky="WENS")

        self.frame_suspension_option.grid_columnconfigure(0, weight=1)

        # widgets
        # desincorporation date
        self.label_desincorporation_date: tk.Label = tk.Label(
            self.frame_suspension_option, text="FECHA DE DESINCORPORACIÓN")
        self.label_desincorporation_date.grid(
            row=0, column=0, sticky="W", pady=5)
        self.label_desincorporation_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_desincorporation_date: tk.Entry = tk.Entry(
            self.frame_suspension_option, textvariable=self.variable_desincorporation_date)
        self.entry_desincorporation_date.grid(
            row=1, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_desincorporation_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # suspension reason
        self.label_suspension_reason: tk.Label = tk.Label(
            self.frame_suspension_option, text="RAZÓN DE SUSPENSIÓN")
        self.label_suspension_reason.grid(row=2, column=0, sticky="W", pady=5)
        self.label_suspension_reason.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_suspension_reason: tk.Entry = tk.Entry(
            self.frame_suspension_option, textvariable=self.variable_suspension_reason)
        self.entry_suspension_reason.grid(
            row=3, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_suspension_reason.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # support number
        self.label_support_number: tk.Label = tk.Label(
            self.frame_suspension_option, text="NÚMERO DE SOPORTE")
        self.label_support_number.grid(row=4, column=0, sticky="W", pady=5)
        self.label_support_number.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_support_number: tk.Entry = tk.Entry(
            self.frame_suspension_option, textvariable=self.variable_support_number)
        self.entry_support_number.grid(
            row=5, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_support_number.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # functions
        self.loadInfoToEntrys()

        # events
        self.variable_desincorporation_date.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="desincorporation_date", variable=self.variable_desincorporation_date))

        self.variable_suspension_reason.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="suspension_reason", variable=self.variable_suspension_reason))

        self.variable_support_number.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="support_number", variable=self.variable_support_number))

    def loadInfoToEntrys(self):
        self.entry_desincorporation_date.insert(
            0, self.data["desincorporation_date"])
        self.entry_suspension_reason.insert(0, self.data["suspension_reason"])
        self.entry_support_number.insert(0, self.data["support_number"])


class GUI_dischargeOption(INTERFACE_writer):
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        # variables
        self.variable_discharge_date: tk.StringVar = tk.StringVar()
        self.variable_discharge_reason: tk.StringVar = tk.StringVar()
        self.variable_support_number: tk.StringVar = tk.StringVar()

        # frame master
        self.frame = frame
        self.data = data

        # inner frame
        self.frame_discharge_option: tk.LabelFrame = tk.LabelFrame(
            self.frame, text="Datos Necesarios Para Egresar")
        self.frame_discharge_option.grid(row=0, column=0, sticky="WENS")
        self.frame_discharge_option.grid_columnconfigure(0, weight=1)

        # widgets
        # discharge date
        self.label_discharge_date: tk.Label = tk.Label(
            self.frame_discharge_option, text="FECHA DE DESINCORPORACIÓN")
        self.label_discharge_date.grid(row=0, column=0, sticky="W", pady=5)
        self.label_discharge_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_discharge_date: tk.Entry = tk.Entry(
            self.frame_discharge_option, textvariable=self.variable_discharge_date)
        self.entry_discharge_date.grid(
            row=1, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_discharge_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # discharge reason
        self.label_discharge_reason: tk.Label = tk.Label(
            self.frame_discharge_option, text="RAZÓN DE EGRESO")
        self.label_discharge_reason.grid(row=2, column=0, sticky="W", pady=5)
        self.label_discharge_reason.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_discharge_reason: tk.Entry = tk.Entry(
            self.frame_discharge_option, textvariable=self.variable_discharge_reason)
        self.entry_discharge_reason.grid(
            row=3, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_discharge_reason.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # support number
        self.label_support_number: tk.Label = tk.Label(
            self.frame_discharge_option, text="NÚMERO DE SOPORTE")
        self.label_support_number.grid(row=4, column=0, sticky="W", pady=5)
        self.label_support_number.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_support_number: tk.Entry = tk.Entry(
            self.frame_discharge_option, textvariable=self.variable_support_number)
        self.entry_support_number.grid(
            row=5, column=0, sticky="WENS", ipadx=5, padx=5)
        self.entry_support_number.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        # functions
        self.loadInfoToEntrys()

        # events
        self.variable_discharge_date.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="discharge_date", variable=self.variable_discharge_date))

        self.variable_discharge_reason.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="discharge_reason", variable=self.variable_discharge_reason))

        self.variable_support_number.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="support_number", variable=self.variable_support_number))

    def loadInfoToEntrys(self):
        self.entry_discharge_date.insert(0, self.data["discharge_date"])
        self.entry_discharge_reason.insert(0, self.data["discharge_reason"])
        self.entry_support_number.insert(0, self.data["support_number"])


class GUI_categoryOptions:
    def __init__(self, frame: tk.Frame, origin_data: str, data_set: list[dict]) -> None:
        # variables
        self.worker_data = origin_data[0]
        self.origin_category = origin_data[1]
        self.data_set = data_set

        # frame master
        self.frame = frame

        # inner frame
        self.frame_category_choice: tk.LabelFrame = tk.LabelFrame(
            self.frame, text="Elegir Nueva Categoría")
        self.frame_category_choice.grid(row=1, column=0, sticky="WENS")

        self.frame_category_choice.grid_rowconfigure(1, weight=1)
        self.frame_category_choice.grid_columnconfigure((0, 1), weight=1)

        # widgets
        # category choicer
        self.label_cagetory: tk.Label = tk.Label(
            self.frame_category_choice, text="CAMBIAR A")
        self.label_cagetory.grid(row=0, column=0)

        self.combobox_categories: ttk.Combobox = ttk.Combobox(
            self.frame_category_choice)
        self.combobox_categories.grid(row=0, column=1, sticky="WENS", padx=5)

        # changable frame
        self.frame_category_container: tk.Frame = tk.Frame(
            self.frame_category_choice)
        self.frame_category_container.grid(
            row=1, column=0, sticky="WENS", columnspan=2, padx=5, pady=5)

        self.frame_category_container.grid_rowconfigure(0, weight=1)
        self.frame_category_container.grid_columnconfigure(0, weight=1)

        self.insertComboBoxChoices()

        # button
        self.button_save_data: tk.Button = tk.Button(
            self.frame, text="CAMBIAR CATEGORÍA")
        self.button_save_data.grid(row=2, column=0)
        self.button_save_data.config(
            font=[guiConfig().getFonts()["main_font"], 15],
            command=self.validateWhatCategoryTheUserChoiced
        )

        # events
        self.combobox_categories.bind(
            "<<ComboboxSelected>>", lambda e: self.getComboBoxToChange())

    def cleanContainerFrame(self):
        for children in self.frame_category_container.winfo_children():
            children.destroy()

    def setCorrespondingCategoryOptions(self, category: str):
        self.cleanContainerFrame()
        if category == "Reactivacion":
            GUI_reactivationOption(
                self.frame_category_container, data=self.data_set[2])

        elif category == "Suspension":
            GUI_suspensionOption(
                self.frame_category_container, data=self.data_set[0])

        elif category == "Egreso":
            GUI_dischargeOption(
                self.frame_category_container, data=self.data_set[1])

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

        self.combobox_categories.config(
            values=choices
        )
        if len(choices) > 1:
            choices = choices[0]

        self.combobox_categories.set(choices)
        self.setCorrespondingCategoryOptions(self.combobox_categories.get())

    def validateSuspensionCategory(self):
        suspension_data = self.data_set[0]

        # no empty fields
        if validateNoEmptyEntrys(("desincorporation_date", "suspension_reason", "support_number"), suspension_data) == False:
            return "Ningún campo puede estar vacío"

        # desincorporation date
        if validateDateFormat(suspension_data["desincorporation_date"]) == False:
            return "La fecha de desincorporación debe tener el formato DD-MM-YYYY"

        # suspension reason
        if validateNotSpecialCharacters(suspension_data["suspension_reason"]) == False:
            return "La razón de suspensión no debe tener carácteres especiales"

        if validateNotNumbers(suspension_data["suspension_reason"]) == False:
            return "La razón de suspensión no debe tener números"

        # support number
        if validateInteger(suspension_data["support_number"]) == False:
            return "El número de soporte solo debe contener números enteros"

        return "No Errors"

    def validateDischargeCategory(self):
        discharge_data = self.data_set[1]

        # no empty fields
        if validateNoEmptyEntrys(("discharge_date", "discharge_reason", "support_number"), discharge_data) == False:
            return "Ningún campo puede estar vacío"

        # desincorporation date
        if validateDateFormat(discharge_data["discharge_date"]) == False:
            return "La fecha de egreso debe tener el formato DD-MM-YYYY"

        # suspension reason
        if validateNotSpecialCharacters(discharge_data["discharge_reason"]) == False:
            return "La razón de egreso no debe tener carácteres especiales"

        if validateNotNumbers(discharge_data["discharge_reason"]) == False:
            return "La razón de egreso no debe tener números"

        # support number
        if validateInteger(discharge_data["support_number"]) == False:
            return "El número de soporte solo debe contener números enteros"

        return "No Errors"

    def validateReactivationCategory(self):
        reactivation_data = self.data_set[2]

        # no empty fields
        if validateNoEmptyEntrys(("reactivation_date", "account_type"), reactivation_data) == False:
            return "Ningún campo puede estar vacío"

        # reactivation date
        if validateDateFormat(reactivation_data["reactivation_date"]) == False:
            return "La fecha de reactivación debe tener el formato DD-MM-YYYY"

        # account type
        if validateUniqueCharacter(reactivation_data["account_type"]) == False:
            return "El tipo de cuenta debe de ser de un único carácter"

        if validateNotNumbers(reactivation_data["account_type"]) == False:
            return "El tipo de cuenta no puede llevar números"

        if validateNotSpecialCharacters(reactivation_data["account_type"]) == False:
            return "El tipo de cuenta no puede llevar carácteres especiales"

        return "No Errors"

    def sqlOperation(self, query: str, params: tuple):
        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            cursor.execute(query, params)
            bd.commit()

    def sqlDeletePreviousRecord(self):
        table = ""
        if self.origin_category == "Nuevo Ingreso":
            table = "newIncome"
        elif self.origin_category == "Reactivacion":
            table = "reactivations"
        elif self.origin_category == "Suspension":
            table = "suspensions"

        query = f"DELETE FROM {table} WHERE worker_ci=?"
        params = self.worker_data[0]

        self.sqlOperation(query, (params,))

    def validateWhatCategoryTheUserChoiced(self):
        category = self.combobox_categories.get()
        validationResult = ""
        query = ""
        params = ()

        # validations
        if category == "Suspension":
            validationResult = self.validateSuspensionCategory()

        elif category == "Egreso":
            validationResult = self.validateDischargeCategory()

        elif category == "Reactivacion":
            validationResult = self.validateReactivationCategory()

        if validationResult == "":
            messagebox.showerror("Error", "Categoría no valida")
            return False

        if validationResult != "No Errors":
            messagebox.showerror("Error", validationResult)
            return False

        # change to choiced category
        # primero mover los datos, luego eliminar de donde estaba
        if category == "Suspension":
            query = ("INSERT INTO suspensions VALUES(?,?,?,?)")
            params = (
                self.worker_data[0],
                self.data_set[0]["desincorporation_date"],
                self.data_set[0]["suspension_reason"],
                self.data_set[0]["support_number"]
            )

        if category == "Egreso":
            query = ("INSERT INTO discharge VALUES(?,?,?,?)")
            params = (
                self.worker_data[0],
                self.data_set[1]["discharge_date"],
                self.data_set[1]["discharge_reason"],
                self.data_set[1]["support_number"]
            )

        if category == "Reactivacion":
            query = ("INSERT INTO reactivations VALUES(?,?,?)")
            params = (
                self.worker_data[0],
                self.data_set[2]["account_type"],
                self.data_set[2]["reactivation_date"]
            )

        self.sqlOperation(query, params)
        self.sqlDeletePreviousRecord()
        messagebox.showinfo(
            "Atención", "Cambio de categoría realizado con éxito")
        return True


class GUI_change_category(GUI_root):
    def __init__(self, root: tk.Tk, data: str) -> None:
        super().__init__(root)

        # variables
        self.worker_data_to_change_category = data[0]
        self.worker_origin_category = data[1]

        self.suspension_data_set = {
            "desincorporation_date": "",
            "suspension_reason": "",
            "support_number": ""
        }

        self.discharge_data_set = {
            "discharge_date": "",
            "discharge_reason": "",
            "support_number": ""
        }

        self.reactivation_data_set = {
            "reactivation_date": "",
            "account_type": ""
        }

        self.data_set = [
            self.suspension_data_set,
            self.discharge_data_set,
            self.reactivation_data_set
        ]

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
        )
        if self.worker_origin_category not in valid_options:
            self.destroyRoot()
            raise Exception("Opción de categoría no soportada")

    def loadDefaultFrames(self):
        GUI_frameWorkerData(frame=self.frame_main,
                            data=self.worker_data_to_change_category)
        GUI_categoryOptions(frame=self.frame_main,
                            origin_data=(
                                self.worker_data_to_change_category, self.worker_origin_category),
                            data_set=self.data_set)
