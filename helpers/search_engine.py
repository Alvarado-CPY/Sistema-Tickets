from tkinter import ttk
import re


class SearchEngine:
    def __init__(self, table: ttk.Treeview):
        self.BACKSPACE = "\x08"

        self.search_ci = ""
        self.table = table

    def searchCI(self, key):
        if key.char != self.BACKSPACE:
            self.search_ci += key.char
            self.searchInTable()

        elif key.char == self.BACKSPACE:
            self.search_ci = self.search_ci[:-1]
            self.searchInTable()

    def searchInTable(self):
        if self.search_ci == "":
            self.table.selection_clear()

        for row in self.table.get_children():
            ci_in_table = str(self.table.item(row)["values"][2])

            if re.search(f"^{self.search_ci}", ci_in_table):
                self.table.see(row)
                self.table.selection_set(row)
                break
            else:
                continue
