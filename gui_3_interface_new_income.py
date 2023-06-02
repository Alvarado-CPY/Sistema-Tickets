import tkinter as tk
from tkinter import messagebox
from app_global_variables import dbPath, guiConfig
from helpers.validate_worker_data import *

class INTERFACE_writer:
    def writeDataToHashMap(self, map: dict, key_map: str, variable: tk.StringVar):
        map[key_map] = variable.get()
        print(map)

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

        self.entry_ci: tk.Entry = tk.Entry(self.frame, textvariable=self.variable_ci)
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

        self.entry_fullname: tk.Entry = tk.Entry(self.frame, textvariable=self.variable_fullname)
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

        self.entry_nacionality: tk.Entry = tk.Entry(self.frame, textvariable=self.variable_nacionality)
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

        self.entry_birthday: tk.Entry = tk.Entry(self.frame, textvariable=self.variable_birthday)
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

        self.entry_age: tk.Entry = tk.Entry(self.frame, textvariable=self.variable_age)
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

        self.entry_gender: tk.Entry = tk.Entry(self.frame, textvariable=self.variable_gender)
        self.entry_gender.grid(row=11, column=0, sticky="WENS", ipady=5)
        self.entry_gender.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        self.variable_ci.trace_add("write", lambda x,y,z: self.writeDataToHashMap(map=self.data, key_map="ci", variable=self.variable_ci))
        self.variable_fullname.trace_add("write", lambda x,y,z: self.writeDataToHashMap(map=self.data, key_map="fullname", variable=self.variable_fullname))
        self.variable_nacionality.trace_add("write", lambda x,y,z: self.writeDataToHashMap(map=self.data, key_map="nacionality", variable=self.variable_nacionality))
        self.variable_birthday.trace_add("write", lambda x,y,z: self.writeDataToHashMap(map=self.data, key_map="birthday", variable=self.variable_birthday))
        self.variable_age.trace_add("write", lambda x,y,z: self.writeDataToHashMap(map=self.data, key_map="age", variable=self.variable_age))
        self.variable_gender.trace_add("write", lambda x,y,z: self.writeDataToHashMap(map=self.data, key_map="gender", variable=self.variable_gender))

        self.loadDataToEntrys()

    def callback(self, variable, map, key_map):
        map[key_map] = variable.get()
        print(map)

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

        # admission date
        self.label_admission_date: tk.Label = tk.Label(
            self.frame, text="FECHA DE INGRESO")
        self.label_admission_date.grid(row=0, column=0, sticky="WNS", pady=5)
        self.label_admission_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_admission_date: tk.Entry = tk.Entry(self.frame)
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

        self.entry_title_of_position: tk.Entry = tk.Entry(self.frame)
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

        self.entry_workload: tk.Entry = tk.Entry(self.frame)
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

        self.entry_working_hours: tk.Entry = tk.Entry(self.frame)
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

        self.entry_speciality: tk.Entry = tk.Entry(self.frame)
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

        self.entry_type_of_staff: tk.Entry = tk.Entry(self.frame)
        self.entry_type_of_staff.grid(row=11, column=0, sticky="WENS", ipady=5)
        self.entry_type_of_staff.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        self.loadDataToEntrys()

        self.entry_admission_date.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "admission_date"))
        self.entry_title_of_position.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "title"))
        self.entry_workload.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "workload"))
        self.entry_working_hours.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "working_hours"))
        self.entry_speciality.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "speciality"))
        self.entry_type_of_staff.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "type_of_staff"))

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

        # administrative location
        self.label_administrative_location: tk.Label = tk.Label(
            self.frame, text="UBICACIÓN ADMINISTRATIVA")
        self.label_administrative_location.grid(
            row=0, column=0, sticky="WNS", pady=5)
        self.label_administrative_location.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_administrative_location: tk.Entry = tk.Entry(self.frame)
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

        self.entry_physical_location: tk.Entry = tk.Entry(self.frame)
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

        self.entry_state: tk.Entry = tk.Entry(self.frame)
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

        self.entry_bank_account: tk.Entry = tk.Entry(self.frame)
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

        self.entry_bank_code: tk.Entry = tk.Entry(self.frame)
        self.entry_bank_code.grid(row=9, column=0, sticky="WENS", ipady=5)
        self.entry_bank_code.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # bank
        self.label_bank: tk.Label = tk.Label(
            self.frame, text="BANCO")
        self.label_bank.grid(
            row=10, column=0, sticky="WNS", pady=5)
        self.label_bank.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_bank: tk.Entry = tk.Entry(self.frame)
        self.entry_bank.grid(row=11, column=0, sticky="WENS", ipady=5)
        self.entry_bank.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        self.loadDataToEntrys()

        self.entry_administrative_location.bind("<Key>", lambda key: self.writeDataToHashMap(
            key, self.data, "administrative_location"))
        self.entry_physical_location.bind("<Key>", lambda key: self.writeDataToHashMap(
            key, self.data, "physical_location"))
        self.entry_state.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "state"))
        self.entry_bank_account.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "bank_account"))
        self.entry_bank_code.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "bank_code"))
        self.entry_bank.bind(
            "<Key>", lambda key: self.writeDataToHashMap(key, self.data, "bank"))

    def loadDataToEntrys(self):
        self.entry_administrative_location.insert(
            0, self.data["administrative_location"])
        self.entry_physical_location.insert(0, self.data["physical_location"])
        self.entry_state.insert(0, self.data["state"])
        self.entry_bank_account.insert(0, self.data["bank_account"])
        self.entry_bank_code.insert(0, self.data["bank_code"])
        self.entry_bank.insert(0, self.data["bank"])


class GUI_addWorker(GUI_root):
    def __init__(self, root: tk.Tk) -> None:
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
            "bank": ""
        }
        self.displayed_frame = ""

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

        # changable frame
        self.setDefaultFrame()

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
        else:
            self.button_next_frame["text"] = "Siguiente"

    def toggleOrDisableLastButton(self):
        if self.button_last_frame["state"] == "normal":
            self.button_last_frame["state"] = "disable"
        else:
            self.button_last_frame["state"] = "normal"

    def validateFirstEntryGroup(self) -> str:
        # ci
        if validateInteger(self.worker_data["ci"]) == False:
            return "La cédula solo debe contener numeros enteros"

        if validateLen(5, self.worker_data["ci"]) == False:
            return "La cédula no puede ser menor a 5 carácteres"

        # name
        if validateNotSpecialCharacters(self.worker_data["fullname"]) == False:
            return "El nombre no debe tener carácteres especiales"

        if validateNotNumbers(self.worker_data["fullname"]) == False:
            return "El nombre no debe tener números"

        # nacionality
        if validateNotSpecialCharacters(self.worker_data["nacionality"]) == False:
            return "La nacionalidad no debe tener carácteres especiales"

        if validateNotNumbers(self.worker_data["nacionality"]) == False:
            return "La nacionalidad no debe tener números"

        # birthday


        # age

        # gender

        # "ci": "",
        #     "fullname": "",
        #     "nacionality": "",
        #     "birthday": "",
        #     "age": "",
        #     "gender": "",
        #     "admission_date": "",
        #     "title": "",
        #     "workload": "",
        #     "working_hours": "",
        #     "speciality": "",
        #     "type_of_staff": "",
        #     "administrative_location": "",
        #     "physical_location": "",
        #     "service_commission": "",
        #     "state": "",
        #     "bank_account": "",
        #     "bank_code": "",
        #     "bank": ""

        return "No Errors"

    def displayNextFrame(self):
        if self.displayed_frame == "personal data":
            if validateNoEmptyEntrys(worker_data=self.worker_data, group=("ci", "fullname", "nacionality", "birthday", "age", "gender")) == False:
                messagebox.showerror("Error", "No puede dejar los datos personales vacios")
                return False

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
            #commition of service is an exception, that can be empty
            if validateNoEmptyEntrys(group=("admission_date", "title", "workload", "working_hours", "speciality", "type_of_staff")) == False:
                messagebox.showerror("Error", "No puede dejar los datos de trabajo vacios")
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


class GUI_workerForm:
    def __init__(self, root: tk.Tk, option: str) -> None:
        self.root = root
        self.setRequiredFormClass(option)

    def setRequiredFormClass(self, option):
        if option == "add":
            GUI_addWorker(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    GUI_workerForm(root, option="add")
    root.mainloop()
