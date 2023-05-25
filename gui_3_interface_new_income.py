import tkinter as tk
from tkinter import ttk, messagebox


class GUI_root:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Trabajador")
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def destroyRoot(self):
        self.root.quit()
        self.root.destroy()


class GUI_framePersonalData:
    def __init__(self, frame: tk.Frame) -> None:
        self.frame = frame

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

        # initial frames
        self.frame_main: tk.Frame = tk.Frame(self.root)
        self.frame_main.grid(row=0, column=0, sticky="WENS")

        self.frame_title: tk.Frame = tk.Frame(self.root)
        self.frame_title.grid(row=0, column=0, sticky="WENS")

        self.frame_title.grid_rowconfigure(0, weight=1)
        self.frame_title.grid_columnconfigure(0, weight=1)

        self.frame_container: tk.Frame = tk.Frame(self.root)
        self.frame_container.grid(row=1, column=0, sticky="WENS")

        self.frame_container.grid_rowconfigure(0 , weight=1)
        self.frame_container.grid_columnconfigure(0, weight=1)

        self.frame_buttons: tk.Frame = tk.Frame(self.root)
        self.frame_buttons.grid(row=2, column=0, sticky="WENS")

        self.frame_buttons.grid_rowconfigure(0, weight=1)
        self.frame_buttons.grid_columnconfigure((0,1), weight=1)

        # title
        self.label_title: tk.Label = tk.Label(self.frame_title, text="Cambiante")
        self.label_title.grid(row=0, column=0, sticky="WENS")

        # changable frame
        self.setDefaultFrame()

        # buttons
        self.button_last_frame: tk.Button = tk.Button(self.frame_buttons, text="Anterior")
        self.button_last_frame.grid(row=0, column=0)

        self.button_next_frame: tk.Button = tk.Button(self.frame_buttons, text="Siguiente")
        self.button_next_frame.grid(row=0, column=1)

    def setDefaultFrame(self):
        GUI_framePersonalData(self.frame_container)


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
