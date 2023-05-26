import tkinter as tk
from tkinter import ttk, messagebox
from app_global_variables import dbPath, guiConfig


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


class GUI_framePersonalData:
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        self.frame = frame

        # ci
        self.label_ci: tk.Label = tk.Label(self.frame, text="CÉDULA")
        self.label_ci.grid(row=0, column=0, sticky="WNS", pady=5)
        self.label_ci.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_ci: tk.Entry = tk.Entry(self.frame)
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

        self.entry_fullname: tk.Entry = tk.Entry(self.frame)
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

        self.entry_nacionality: tk.Entry = tk.Entry(self.frame)
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

        self.entry_birthday: tk.Entry = tk.Entry(self.frame)
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

        self.entry_age: tk.Entry = tk.Entry(self.frame)
        self.entry_age.grid(row=9, column=0, sticky="WENS", ipady=5)
        self.entry_age.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )

        # gender
        self.label_gender: tk.Label = tk.Label(self.frame, text="GENERO", pady=5)
        self.label_gender.grid(row=10, column=0, sticky="WNS")
        self.label_gender.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )

        self.entry_gender: tk.Entry = tk.Entry(self.frame)
        self.entry_gender.grid(row=11, column=0, sticky="WENS", ipady=5)
        self.entry_gender.config(
            font=[guiConfig().getFonts()["terciary_font"], 13]
        )


class GUI_frameWorkData:
    def __init__(self, frame: tk.Frame, data: dict) -> None:
        self.frame = frame

        # admission date
        self.label_admission_date: tk.Label = tk.Label(self.frame, text="FECHA DE INGRESO")
        self.label_admission_date.grid(row=0, column=0 , sticky="WNS", pady=5)
        self.label_admission_date.config(
            font=[guiConfig().getFonts()["secondary_font"], 13]
        )


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
        self.frame_container.grid(row=1, column=0, sticky="WENS", padx=20, pady=10)

        self.frame_container.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10, 11), weight=1)
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

        # changable frame
        self.setDefaultFrame()

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

    def setTitle(self, title):
        self.label_title["text"] = title

    def clearContainerFrame(self):
        for children in self.frame_container.winfo_children():
            children.destroy()

    def displayNextFrame(self):
        if self.displayed_frame == "personal data":
            self.setTitle("DATOS DE TRABAJO")
            self.displayed_frame = "work data"

            self.clearContainerFrame()
            GUI_frameWorkData(self.frame_container, self.worker_data)

            return True

        if self.displayed_frame == "work data":
            self.setTitle("DATOS DE PAGO")
            self.displayed_frame = "pay data"
            return True

    def displayLastFrame(self):
        if self.displayed_frame == "pay data":
            self.setTitle("DATOS DE TRABAJO")
            self.displayed_frame = "work data"
            return True

        if self.displayed_frame == "work data":
            self.setTitle("DATOS PERSONALES")
            self.displayed_frame = "personal data"

            self.clearContainerFrame()
            GUI_framePersonalData(self.frame_container, self.worker_data)

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