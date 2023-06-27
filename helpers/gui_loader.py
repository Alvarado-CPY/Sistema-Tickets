import tkinter as tk
import os


def setfullScreen(root: tk.Tk):
    if os.name == "nt":
        root.state("zoomed")
    else:
        root.attributes("-fullscreen", True)


def loadGUI(root: tk, GUI_to_load: object, option: str = None, data=None, full=True):
    root.withdraw()
    sub_root = tk.Toplevel(root)

    if option != None:
        if data != None:
            GUI_to_load(sub_root, option=option, data=data)
        else:
            GUI_to_load(sub_root, option=option)

    else:
        if data != None:
            GUI_to_load(sub_root, data=data)
        else:
            GUI_to_load(sub_root)

    sub_root.mainloop()

    root.deiconify()

    if full:
        setfullScreen(root)
