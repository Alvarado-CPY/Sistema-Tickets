import sqlite3
import tkinter as tk
from tkinter import messagebox
from app_global_variables import dbPath, guiConfig, bankCodesPath
from helpers.config import GetBankConfig
from helpers.writer_interface import INTERFACE_writer
from helpers.validate_worker_data import *


class GUI_root:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Trabajador")
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

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


class GUI_framePersonalData(INTERFACE_writer):
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        self.data = data
        self.frame = frame

        # variables
        self.variable_ci = tk.StringVar()
        self.variable_fullname = tk.StringVar()
        self.variable_nacionality = tk.StringVar()
        self.variable_birthday = tk.StringVar()
        self.variable_age = tk.StringVar()
        self.variable_gender = tk.StringVar()

        # ci
        self.label_ci: tk.Label = tk.Label(self.frame, text="CÉDULA")
        self.label_ci.grid(row=0, column=0, sticky="WNS", pady=5)
        self.label_ci.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_ci: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_ci)
        self.entry_ci.grid(row=1, column=0, sticky="WENS", ipady=5)
        self.entry_ci.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # fullname
        self.label_fullname: tk.Label = tk.Label(
            self.frame, text="NOMBRE COMPLETO")
        self.label_fullname.grid(row=2, column=0, sticky="WNS", pady=5)
        self.label_fullname.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_fullname: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_fullname)
        self.entry_fullname.grid(row=3, column=0, sticky="WENS", ipady=5)
        self.entry_fullname.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # nacionality
        self.label_nacionality: tk.Label = tk.Label(
            self.frame, text="NACIONALIDAD")
        self.label_nacionality.grid(row=4, column=0, sticky="WNS", pady=5)
        self.label_nacionality.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_nacionality: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_nacionality)
        self.entry_nacionality.grid(row=5, column=0, sticky="WENS", ipady=5)
        self.entry_nacionality.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # birthday
        self.label_birthday: tk.Label = tk.Label(
            self.frame, text="FECHA DE NACIMIENTO")
        self.label_birthday.grid(row=6, column=0, sticky="WNS", pady=5)
        self.label_birthday.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_birthday: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_birthday)
        self.entry_birthday.grid(row=7, column=0, sticky="WENS", ipady=5)
        self.entry_birthday.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # age
        self.label_age: tk.Label = tk.Label(self.frame, text="EDAD", pady=5)
        self.label_age.grid(row=8, column=0, sticky="WNS")
        self.label_age.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_age: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_age)
        self.entry_age.grid(row=9, column=0, sticky="WENS", ipady=5)
        self.entry_age.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # gender
        self.label_gender: tk.Label = tk.Label(
            self.frame, text="GENERO", pady=5)
        self.label_gender.grid(row=10, column=0, sticky="WNS")
        self.label_gender.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_gender: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_gender)
        self.entry_gender.grid(row=11, column=0, sticky="WENS", ipady=5)
        self.entry_gender.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # keeping track of user input
        self.variable_ci.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="ci", variable=self.variable_ci))

        self.variable_fullname.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="fullname", variable=self.variable_fullname))

        self.variable_nacionality.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="nacionality", variable=self.variable_nacionality))

        self.variable_birthday.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="birthday", variable=self.variable_birthday))

        self.variable_age.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="age", variable=self.variable_age))

        self.variable_gender.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="gender", variable=self.variable_gender))

        self.loadDataToEntrys()

    def loadDataToEntrys(self):
        self.entry_ci.insert(0, self.data["ci"])
        self.entry_fullname.insert(0, self.data["fullname"])
        self.entry_nacionality.insert(0, self.data["nacionality"])
        self.entry_birthday.insert(0, self.data["birthday"])
        self.entry_age.insert(0, self.data["age"])
        self.entry_gender.insert(0, self.data["gender"])


class GUI_frameWorkData(INTERFACE_writer):
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        self.data = data
        self.frame = frame

        # variables
        self.variable_admission_date = tk.StringVar()
        self.variable_title_of_position = tk.StringVar()
        self.variable_workload = tk.StringVar()
        self.variable_working_hours = tk.StringVar()
        self.variable_speciality = tk.StringVar()
        self.variable_type_of_staff = tk.StringVar()

        # admission date
        self.label_admission_date: tk.Label = tk.Label(
            self.frame, text="FECHA DE INGRESO")
        self.label_admission_date.grid(row=0, column=0, sticky="WNS", pady=5)
        self.label_admission_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_admission_date: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_admission_date)
        self.entry_admission_date.grid(row=1, column=0, sticky="WENS", ipady=5)
        self.entry_admission_date.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # title of position
        self.label_title_of_position: tk.Label = tk.Label(
            self.frame, text="DENOMINACIÓN DE CARGO")
        self.label_title_of_position.grid(
            row=2, column=0, sticky="WNS", pady=5)
        self.label_title_of_position.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_title_of_position: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_title_of_position)
        self.entry_title_of_position.grid(
            row=3, column=0, sticky="WENS", ipady=5)
        self.entry_title_of_position.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # workload
        self.label_workload: tk.Label = tk.Label(
            self.frame, text="CARGA LABORAL")
        self.label_workload.grid(row=4, column=0, sticky="WNS", pady=5)
        self.label_workload.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_workload: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_workload)
        self.entry_workload.grid(row=5, column=0, sticky="WENS", ipady=5)
        self.entry_workload.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # working hours
        self.label_working_hours: tk.Label = tk.Label(
            self.frame, text="HORARIO LABORAL")
        self.label_working_hours.grid(row=6, column=0, sticky="WNS", pady=5)
        self.label_working_hours.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_working_hours: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_working_hours)
        self.entry_working_hours.grid(row=7, column=0, sticky="WENS", ipady=5)
        self.entry_working_hours.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # speciality
        self.label_speciality: tk.Label = tk.Label(
            self.frame, text="ESPECIALIDAD")
        self.label_speciality.grid(row=8, column=0, sticky="WNS", pady=5)
        self.label_speciality.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_speciality: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_speciality)
        self.entry_speciality.grid(row=9, column=0, sticky="WENS", ipady=5)
        self.entry_speciality.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # type of staff
        self.label_type_off_staff: tk.Label = tk.Label(
            self.frame, text="TIPO DE PERSONAL")
        self.label_type_off_staff.grid(row=10, column=0, sticky="WNS", pady=5)
        self.label_type_off_staff.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_type_of_staff: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_type_of_staff)
        self.entry_type_of_staff.grid(row=11, column=0, sticky="WENS", ipady=5)
        self.entry_type_of_staff.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # keeping track of user input
        self.variable_admission_date.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="admission_date", variable=self.variable_admission_date))

        self.variable_title_of_position.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="title", variable=self.variable_title_of_position))

        self.variable_workload.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="workload", variable=self.variable_workload))

        self.variable_working_hours.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="working_hours", variable=self.variable_working_hours))

        self.variable_speciality.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="speciality", variable=self.variable_speciality))

        self.variable_type_of_staff.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="type_of_staff", variable=self.variable_type_of_staff))

        self.loadDataToEntrys()

    def loadDataToEntrys(self):
        self.entry_admission_date.insert(0, self.data["admission_date"])
        self.entry_title_of_position.insert(0, self.data["title"])
        self.entry_workload.insert(0, self.data["workload"])
        self.entry_working_hours.insert(0, self.data["working_hours"])
        self.entry_speciality.insert(0, self.data["speciality"])
        self.entry_type_of_staff.insert(0, self.data["type_of_staff"])


class GUI_framePayData(INTERFACE_writer):
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        self.data = data
        self.frame = frame

        self.variable_administrative_location = tk.StringVar()
        self.variable_physical_location = tk.StringVar()
        self.variable_state = tk.StringVar()
        self.variable_bank_account = tk.StringVar()
        self.variable_bank_code = tk.StringVar()
        self.variable_account_type = tk.StringVar()

        # administrative location
        self.label_administrative_location: tk.Label = tk.Label(
            self.frame, text="UBICACIÓN ADMINISTRATIVA")
        self.label_administrative_location.grid(
            row=0, column=0, sticky="WNS", pady=5)
        self.label_administrative_location.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_administrative_location: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_administrative_location)
        self.entry_administrative_location.grid(
            row=1, column=0, sticky="WENS", ipady=5)
        self.entry_administrative_location.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # physical location
        self.label_physical_location: tk.Label = tk.Label(
            self.frame, text="UBICACIÓN FÍSICA")
        self.label_physical_location.grid(
            row=2, column=0, sticky="WNS", pady=5)
        self.label_physical_location.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_physical_location: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_physical_location)
        self.entry_physical_location.grid(
            row=3, column=0, sticky="WENS", ipady=5)
        self.entry_physical_location.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # state
        self.label_state: tk.Label = tk.Label(
            self.frame, text="ESTADO")
        self.label_state.grid(
            row=4, column=0, sticky="WNS", pady=5)
        self.label_state.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_state: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_state)
        self.entry_state.grid(row=5, column=0, sticky="WENS", ipady=5)
        self.entry_state.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # bank account
        self.label_bank_account: tk.Label = tk.Label(
            self.frame, text="CUENTA BANCARIA")
        self.label_bank_account.grid(
            row=6, column=0, sticky="WNS", pady=5)
        self.label_bank_account.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_bank_account: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_bank_account)
        self.entry_bank_account.grid(row=7, column=0, sticky="WENS", ipady=5)
        self.entry_bank_account.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # bank code
        self.label_bank_code: tk.Label = tk.Label(
            self.frame, text="CÓDIGO DEL BANCO")
        self.label_bank_code.grid(
            row=8, column=0, sticky="WNS", pady=5)
        self.label_bank_code.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_bank_code: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_bank_code)
        self.entry_bank_code.grid(row=9, column=0, sticky="WENS", ipady=5)
        self.entry_bank_code.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # account type
        self.label_account_type: tk.Label = tk.Label(
            self.frame, text="TIPO DE CUENTA")
        self.label_account_type.grid(
            row=10, column=0, sticky="WNS", pady=5)
        self.label_account_type.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_account_type: tk.Entry = tk.Entry(
            self.frame, textvariable=self.variable_account_type)
        self.entry_account_type.grid(row=11, column=0, sticky="WENS", ipady=5)
        self.entry_account_type.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # keeping track of user input
        self.variable_administrative_location.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="administrative_location", variable=self.variable_administrative_location))

        self.variable_physical_location.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="physical_location", variable=self.variable_physical_location))

        self.variable_state.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="state", variable=self.variable_state))

        self.variable_bank_account.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="bank_account", variable=self.variable_bank_account))

        self.variable_bank_code.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="bank_code", variable=self.variable_bank_code))

        self.variable_account_type.trace_add("write", lambda x, y, z: self.writeDataToHashMap(
            map=self.data, key_map="account_type", variable=self.variable_account_type))

        self.loadDataToEntrys()

    def loadDataToEntrys(self):
        self.entry_administrative_location.insert(
            0, self.data["administrative_location"])
        self.entry_physical_location.insert(0, self.data["physical_location"])
        self.entry_state.insert(0, self.data["state"])
        self.entry_bank_account.insert(0, self.data["bank_account"])
        self.entry_bank_code.insert(0, self.data["bank_code"])
        self.entry_account_type.insert(0, self.data["account_type"])


class GUI_addWorker(GUI_root):
    def __init__(self, root: tk.Tk, option: str) -> None:
        super().__init__(root)

        # variables
        self.worker_data = {
            "ci": "",
            "fullname": "",
            "nacionality": "",
            "birthday": "",
            "age": "",
            "gender": "",
            "admission_date": "",
            "title": "",
            "workload": "",
            "working_hours": "",
            "speciality": "",
            "type_of_staff": "",
            "administrative_location": "",
            "physical_location": "",
            "service_commission": "",
            "state": "",
            "bank_account": "",
            "bank_code": "",
            "account_type": "",
        }
        self.displayed_frame = ""
        self.option = option
        self.current_ci = ""

        # initial frames
        self.frame_main: tk.Frame = tk.Frame(self.root)
        self.frame_main.grid(row=0, column=0, sticky="WENS")

        self.frame_title: tk.Frame = tk.Frame(self.root)
        self.frame_title.grid(row=0, column=0, sticky="WENS", pady=10)

        self.frame_title.grid_rowconfigure(0, weight=1)
        self.frame_title.grid_columnconfigure(0, weight=1)

        self.frame_container: tk.Frame = tk.Frame(self.root)
        self.frame_container.grid(
            row=1, column=0, sticky="WENS", padx=20, pady=10)

        self.frame_container.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
        self.frame_container.grid_columnconfigure(0, weight=1)

        self.frame_buttons: tk.Frame = tk.Frame(self.root)
        self.frame_buttons.grid(row=2, column=0, sticky="WENS", pady=10)

        self.frame_buttons.grid_rowconfigure(0, weight=1)
        self.frame_buttons.grid_columnconfigure((0, 1), weight=1)

        # title
        self.label_title: tk.Label = tk.Label(
            self.frame_title, text="Cambiante")
        self.label_title.grid(row=0, column=0, sticky="WENS")
        self.label_title.config(
            font=[guiConfig().getFonts()["main_font"], 18]
        )

        # buttons
        self.button_last_frame: tk.Button = tk.Button(
            self.frame_buttons, text="Anterior")
        self.button_last_frame.grid(row=0, column=0)
        self.button_last_frame.config(
            width=10,
            font=[guiConfig().getFonts()["main_font"], 15],
            command=self.displayLastFrame
        )

        self.button_next_frame: tk.Button = tk.Button(
            self.frame_buttons, text="Siguiente")
        self.button_next_frame.grid(row=0, column=1)
        self.button_next_frame.config(
            width=10,
            font=[guiConfig().getFonts()["main_font"], 15],
            command=self.displayNextFrame
        )

    def setDefaultFrame(self):
        self.setTitle("DATOS PERSONALES")
        self.displayed_frame = "personal data"
        GUI_framePersonalData(self.frame_container, self.worker_data)
        self.toggleOrDisableLastButton()

    def setTitle(self, title):
        self.label_title["text"] = title

    def clearContainerFrame(self):
        for children in self.frame_container.winfo_children():
            children.destroy()

    def updateNextButtonWhenFrameIsDisplayed(self):
        if self.button_next_frame["text"] == "Siguiente":
            self.button_next_frame["text"] = "Guardar"
            self.button_next_frame.config(
                command=self.saveInformation
            )
        else:
            self.button_next_frame["text"] = "Siguiente"
            self.button_next_frame.config(
                command=self.displayNextFrame
            )

    def toggleOrDisableLastButton(self):
        if self.button_last_frame["state"] == "normal":
            self.button_last_frame["state"] = "disable"
        else:
            self.button_last_frame["state"] = "normal"

    def validateFirstEntryGroup(self) -> str:
        # no empty
        if validateNoEmptyEntrys(worker_data=self.worker_data, group=("ci", "fullname", "nacionality", "birthday", "age", "gender")) == False:
            return "No puede dejar los datos personales vacios"

        # ci
        if validateInteger(self.worker_data["ci"]) == False:
            return "La cédula solo debe contener numeros enteros"

        if validateLen(5, self.worker_data["ci"]) == False:
            return "La cédula no puede ser menor a 5 carácteres"

        # validate then if the ci that the user is trying to insert already exists
        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            worker = cursor.execute(
                "SELECT * FROM workers WHERE worker_ci=?", (int(self.worker_data["ci"]),)).fetchone()

            if self.option == "add":
                if worker != None:
                    return "La cédula que usted marcó ya se encuentra registrada"

            elif self.option == "update":
                if worker != None and int(self.worker_data["ci"]) != int(self.current_ci):
                    return "La cédula que usted marcó ya se encuentra registrada para otro trabajador"

        # name
        if validateNotSpecialCharacters(self.worker_data["fullname"]) == False:
            return "El nombre no debe tener carácteres especiales"

        if validateNotNumbers(self.worker_data["fullname"]) == False:
            return "El nombre no debe tener números"

        # nacionality
        if validateUniqueCharacter(self.worker_data["nacionality"]) == False:
            return "La nacionalidad debe ser de un único carácter"

        if validateNotSpecialCharacters(self.worker_data["nacionality"]) == False:
            return "La nacionalidad no debe tener carácteres especiales"

        if validateNotNumbers(self.worker_data["nacionality"]) == False:
            return "La nacionalidad no debe tener números"

        # birthday
        if validateDateFormat(self.worker_data["birthday"]) == False:
            return "El formato de las fechas debe ser DD-MM-AAAA"

        # age
        if validateInteger(self.worker_data["age"]) == False:
            return "La edad debe solo contener números"

        # gender
        if validateUniqueCharacter(self.worker_data["gender"]) == False:
            return "El genero debe de ser de un único carácter"

        if validateNotNumbers(self.worker_data["gender"]) == False:
            return "El genero no puede contener números"

        if validateNotSpecialCharacters(self.worker_data["gender"]) == False:
            return "El genero no debe tener carácteres especiales"

        return "No Errors"

    def validateSecondEntryGroup(self):
        # commition of service and speciality are exceptions, those can be empty
        if validateNoEmptyEntrys(worker_data=self.worker_data, group=("admission_date", "title", "workload", "working_hours", "type_of_staff")) == False:
            return "No puede dejar los datos de trabajo vacios"

        # admission date
        if validateDateFormat(self.worker_data["admission_date"]) == False:
            return "El formato de las fechas debe ser DD-MM-AAAA"

        # title of position
        if validateNotNumbers(self.worker_data["title"]) == False:
            return "El cargo no puede llevar números"

        if validateNotSpecialCharacters(self.worker_data["title"]) == False:
            return "El cargo no puede llevar carácteres especiales"

        # workload
        if validateNotSpecialCharacters(self.worker_data["workload"]) == False:
            return "La carga laboral no puede llevar carácteres especiales"

        # working hours
        if validateNotSpecialCharacters(self.worker_data["working_hours"]) == False:
            return "El horario laboral no puede llevar carácteres especiales"

        # speciality
        if validateNotSpecialCharacters(self.worker_data["speciality"]) == False:
            return "La especialidad no puede llevar carácteres especiales"

        if validateNotNumbers(self.worker_data["speciality"]) == False:
            return "La especialidad no puede llevar números"

        # type of staff
        if validateNotSpecialCharacters(self.worker_data["type_of_staff"]) == False:
            return "El tipo de personal no puede llevar carácteres especiales"

        if validateNotNumbers(self.worker_data["type_of_staff"]) == False:
            return "El tipo de personal no puede llevar números"

        return "No Errors"

    def validateThirdEntryGroup(self):
        # no empty
        if validateNoEmptyEntrys(worker_data=self.worker_data, group=("administrative_location", "physical_location", "state", "bank_account", "bank_code", "account_type")) == False:
            return "No puede dejar los datos de pago vacíos"

        # administrative_location
        if validateNotSpecialCharacters(self.worker_data["administrative_location"]) == False:
            return "La ubicación administrativa no puede llevar carácteres especiales"

        if validateNotNumbers(self.worker_data["administrative_location"]) == False:
            return "La ubicación administrativa no puede llevar números"

        # physical_location
        if validateNotSpecialCharacters(self.worker_data["physical_location"]) == False:
            return "La ubicación física no puede llevar carácteres especiales"

        if validateNotNumbers(self.worker_data["physical_location"]) == False:
            return "La ubicación físcia no puede llevar números"

        # state
        if validateNotSpecialCharacters(self.worker_data["state"]) == False:
            return "El estado no puede llevar carácteres especiales"

        if validateNotNumbers(self.worker_data["state"]) == False:
            return "El estado no puede llevar números"

        # bank_account
        if validateInteger(self.worker_data["bank_account"]) == False:
            return "La cuenta bancaria solo puede tener números"

        if self.worker_data["bank_account"][0] != "0":
            return "La cuenta bancaria debe empezar por cero"

        if validateLen(20, self.worker_data["bank_account"], limit=True) == False:
            return "La cuenta bancaria debe tener 20 carácteres de largo"

        # bank_code
        if validateLen(4, self.worker_data["bank_code"], limit=True) == False:
            return "El codigo del banco debe tener 4 carácteres de largo"

        if validateInteger(self.worker_data["bank_code"]) == False:
            return "El codigo del banco solo puede tener números"

        if self.worker_data["bank_code"][0] != "0":
            return "El codigo del banco debe empezar por cero"

        if validateBankCode(self.worker_data["bank_code"], bankCodesPath()) == False:
            return "El codigo del banco es un codigo no valido"

        # account type
        if validateUniqueCharacter(self.worker_data["account_type"]) == False:
            return "El tipo de cuenta debe de ser de un único carácter"

        if validateNotNumbers(self.worker_data["account_type"]) == False:
            return "El tipo de cuenta no puede llevar números"

        if validateNotSpecialCharacters(self.worker_data["account_type"]) == False:
            return "El tipo de cuenta no puede llevar carácteres especiales"

        return "No Errors"

    def saveInformation(self):
        # validate first the last group of entrys
        validationResults = self.validateThirdEntryGroup()
        if validationResults != "No Errors":
            messagebox.showerror("Error", validationResults)
            return False

        # save data to db
        data_to_save_in_worker_table = [
            self.worker_data["nacionality"].upper(),
            int(self.worker_data["ci"]),
            self.worker_data["fullname"].upper(),
            self.worker_data["birthday"],
            int(self.worker_data["age"]),
            self.worker_data["gender"].upper(),
            self.worker_data["admission_date"],
            self.worker_data["title"].upper(),
            self.worker_data["workload"].upper(),
            self.worker_data["working_hours"].upper(),
            self.worker_data["speciality"].upper(),
            self.worker_data["type_of_staff"].upper(),
            self.worker_data["administrative_location"].upper(),
            self.worker_data["physical_location"].upper(),
            self.worker_data["service_commission"],
            self.worker_data["state"].upper(),
            self.worker_data["bank_account"],
            self.worker_data["bank_code"],
            GetBankConfig(bankCodesPath()).getBankValueByCode(
                self.worker_data["bank_code"]).upper()
        ]

        data_to_save_in_new_income_table = [
            int(self.worker_data["ci"]),
            self.worker_data["account_type"].upper()
        ]

        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()

            if self.option == "add":
                cursor.execute(
                    "INSERT INTO workers VALUES(NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    data_to_save_in_worker_table
                )
                cursor.execute(
                    "INSERT INTO newIncome VALUES (?,?)",
                    data_to_save_in_new_income_table
                )
            elif self.option == "update":
                cursor.execute(
                    """UPDATE workers SET
                    nationality=?,
                    worker_ci=?,
                    worker_fullname=?,
                    birthday=?,
                    age=?,
                    gender=?,
                    admission_date=?,
                    title_of_position=?,
                    workload=?,
                    working_hours=?,
                    specialty=?,
                    type_of_staff=?,
                    administrative_location=?,
                    physical_location=?,
                    service_commission=?,
                    state=?,
                    bank_account=?,
                    bank_code=?,
                    bank=?
                    WHERE worker_ci=?
                    """,
                    (*data_to_save_in_worker_table, self.current_ci)
                )

                cursor.execute(
                    """UPDATE newIncome SET
                    worker_ci=?,
                    account_type=?
                    WHERE worker_ci=?
                    """,
                    (*data_to_save_in_new_income_table, self.current_ci)
                )

            bd.commit()
            messagebox.showinfo("Atención", "Datos guardados éxitosamente")
            self.destroyRoot()

    def displayNextFrame(self):
        if self.displayed_frame == "personal data":

            validationResults = self.validateFirstEntryGroup()
            if validationResults != "No Errors":
                messagebox.showerror("Error", validationResults)
                return False

            self.setTitle("DATOS DE TRABAJO")
            self.displayed_frame = "work data"

            self.clearContainerFrame()
            GUI_frameWorkData(self.frame_container, self.worker_data)
            self.toggleOrDisableLastButton()

            return True

        if self.displayed_frame == "work data":

            validationResults = self.validateSecondEntryGroup()
            if validationResults != "No Errors":
                messagebox.showerror("Error", validationResults)
                return False

            self.setTitle("DATOS DE PAGO")
            self.displayed_frame = "pay data"

            self.clearContainerFrame()
            GUI_framePayData(self.frame_container, self.worker_data)
            self.updateNextButtonWhenFrameIsDisplayed()

            return True

    def displayLastFrame(self):
        if self.displayed_frame == "pay data":
            self.setTitle("DATOS DE TRABAJO")
            self.displayed_frame = "work data"

            self.clearContainerFrame()
            GUI_frameWorkData(self.frame_container, self.worker_data)
            self.updateNextButtonWhenFrameIsDisplayed()

            return True

        if self.displayed_frame == "work data":
            self.setTitle("DATOS PERSONALES")
            self.displayed_frame = "personal data"

            self.clearContainerFrame()
            GUI_framePersonalData(self.frame_container, self.worker_data)
            self.toggleOrDisableLastButton()

            return True

    def loadExistingDataFromUserInWorkerDict(self, data):
        """THIS METHOND WILL ONLY BE TRIGGED WHEN THE USER WANTS TO MODIFY AN EXISTING WORKER
            IT WILL LOAD THE DATA FROM THAT WORKER INTO THE DICTIONARY TO THEN LOAD IT INTO THE GUI
        """
        # load data into temp memory
        self.current_ci = str(data[2])
        self.worker_data["nacionality"] = str(data[1])
        self.worker_data["ci"] = str(data[2])
        self.worker_data["fullname"] = str(data[3])
        self.worker_data["birthday"] = str(data[4])
        self.worker_data["age"] = str(data[5])
        self.worker_data["gender"] = str(data[6])
        self.worker_data["admission_date"] = str(data[7])
        self.worker_data["title"] = str(data[8])
        self.worker_data["workload"] = str(data[9])
        self.worker_data["working_hours"] = str(data[10])
        self.worker_data["speciality"] = str(data[11])
        self.worker_data["type_of_staff"] = str(data[12])
        self.worker_data["administrative_location"] = str(data[13])
        self.worker_data["physical_location"] = str(data[14])
        self.worker_data["service_commission"] = str(data[15])
        self.worker_data["state"] = str(data[16])
        self.worker_data["bank_account"] = f"0{data[17]}"
        self.worker_data["bank_code"] = f"0{data[18]}"
        self.worker_data["account_type"] = str(data[20])

class GUI_workerForm:
    def __init__(self, root: tk.Tk, option: str, data=None) -> None:
        self.root = root
        self.worker_info = data
        self.setRequiredFormClass(option)

    def setRequiredFormClass(self, option):
        gui_interface = GUI_addWorker(self.root, option=option)
        if option == "update":
            if self.worker_info == None:
                raise Exception("No worker data passed to be update")
            else:
                gui_interface.loadExistingDataFromUserInWorkerDict(
                    self.worker_info)

        gui_interface.setDefaultFrame()
