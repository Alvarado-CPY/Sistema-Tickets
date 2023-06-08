from helpers.config import GetGUIConfig
import os


def guiConfig():
    return GetGUIConfig(os.path.join("config", "gui.json"))


def bankCodesPath():
    return os.path.join("config", "bank.json")


def dbPath():
    return os.path.join("database", "workers.db")
