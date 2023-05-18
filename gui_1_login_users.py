import tkinter as tk
from tkinter import messagebox
import sqlite3
from helpers.encrypt import comparePassword
from gui_2_main_menu import GUI_mainmenu
from app_global_variables import guiConfig, dbPath


class GUI_root:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Login")
        self.root.resizable(0, 0)

        self.root.grid_rowconfigure((0, 1), weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.centralizeWindow()

    def destroyRoot(self):
        self.root.quit()
        self.root.destroy()

    def centralizeWindow(self):
        windows_width = 400
        windows_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_coordinate = int((screen_width/2) - (windows_width/2))
        y_coordinate = int((screen_height/2) - (windows_height/2))-50

        self.root.geometry(
            f"{windows_width}x{windows_height}+{x_coordinate}+{y_coordinate}")


class GUI_login(GUI_root):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)

        self.label_title: tk.Label = tk.Label(
            root, text="SISTEMA DE GESTIÓN\n AUTOMATIZADA DE\n TICKETS DE ALIMENTACIÓN")
        self.label_title.grid(row=0, column=0, sticky="WENS", padx=15)
        self.label_title.config(
            font=[guiConfig().getFonts()["main_font"], 17]
        )

        # form
        self.frame_form: tk.Frame = tk.Frame(root)
        self.frame_form.grid(row=1, column=0, sticky="WENS", padx=15, pady=10)

        self.frame_form.grid_columnconfigure(0, weight=1)

        # form__widgets
        self.label_username: tk.Label = tk.Label(
            self.frame_form, text="NOMBRE DE USUARIO")
        self.label_username.grid(row=0, column=0, sticky="W")
        self.label_username.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.entry_username: tk.Entry = tk.Entry(self.frame_form)
        self.entry_username.grid(row=1, column=0, sticky="WE", pady=10)
        self.entry_username.config(
            font=[guiConfig().getFonts()["terciary_font"], 15]
        )
        self.entry_username.focus()

        self.label_password: tk.Label = tk.Label(
            self.frame_form, text="CONTRASEÑA")
        self.label_password.grid(row=2, column=0, sticky="W")
        self.label_password.config(
            font=[guiConfig().getFonts()["secondary_font"], 15]
        )

        self.entry_password: tk.Entry = tk.Entry(self.frame_form)
        self.entry_password.grid(row=3, column=0, sticky="WE", pady=10)
        self.entry_password.config(
            font=[guiConfig().getFonts()["terciary_font"], 15],
            show="*"
        )

        self.button_login: tk.Button = tk.Button(
            self.frame_form, text="ENTRAR")
        self.button_login.grid(row=4, column=0, sticky="WE")
        self.button_login.config(
            font=[guiConfig().getFonts()["main_font"], 15],
            command=self.login
        )

        self.entry_username.bind(
            "<Key>", lambda key: self.eventQuickNavigation(key, "username"))
        self.entry_password.bind(
            "<Key>", lambda key: self.eventQuickNavigation(key, "password"))

    def eventQuickNavigation(self, key, entry: str):
        if key.char == "\r":
            if entry == "username":
                self.entry_password.focus()
            else:
                self.button_login.invoke()

    def emptyFields(self) -> bool:
        if len(self.entry_username.get().strip()) == 0:
            return True

        if len(self.entry_password.get().strip()) == 0:
            return True

        return False

    def displayError(self, msg):
        messagebox.showerror("Error", msg)
        self.entry_username.focus()

    def login(self):
        if self.emptyFields():
            self.displayError("No puede dejar datos vacios.")
            return False

        with sqlite3.connect(dbPath()) as bd:
            cursor = bd.cursor()
            cursor.execute("SELECT * FROM users where username=?",
                           (self.entry_username.get(),))
            user = cursor.fetchone()

            if user == None:
                self.displayError("Usuario no existe.")
                return False

            if not comparePassword(self.entry_password.get(), user[3]):
                self.displayError("Contraseña incorrecta.")
                return False

            cursor.execute("INSERT INTO active_user VALUES(?)", (user[0],))
            bd.commit()
            self.loadMainMenu()

    def loadMainMenu(self):
        self.destroyRoot()
        root2 = tk.Tk()
        GUI_mainmenu(root2)
        root2.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    GUI_login(root)
    root.mainloop()
