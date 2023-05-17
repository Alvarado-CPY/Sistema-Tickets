import tkinter as tk
import os
from gui_1_login_users import GUI_login
from helpers.database import BBDD
from helpers.encrypt import encryptPassword

if __name__ == "__main__":
    if not os.path.exists("database"):
        os.mkdir("database")

    db = BBDD()
    db.generateDatabaseTables()
    db.setDefaultUser(password=encryptPassword("1234"))

    root = tk.Tk()
    GUI_login(root)
    root.mainloop()
