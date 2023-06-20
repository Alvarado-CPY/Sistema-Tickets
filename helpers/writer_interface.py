import tkinter as tk

class INTERFACE_writer:
    def writeDataToHashMap(self, map: dict, key_map: str, variable: tk.StringVar):
        map[key_map] = variable.get()