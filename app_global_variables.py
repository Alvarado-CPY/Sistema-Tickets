from helpers.config import GetGUIConfig
import os


def guiConfig():
    return GetGUIConfig(os.path.join("config", "gui.json"))


def dbPath():
    return os.path.join("database", "workers.db")
