import json
import os


class GetGUIConfig:
    def __init__(self, path):
        self.json_path = path
        self.colors = {}
        self.fonts = {}
        self.hover_colors = {}

        self.getConfigFromJsonFile()

    def getConfigFromJsonFile(self):
        with open(self.json_path, "r") as file:
            jsonDict = json.loads(file.read())

            self.colors = jsonDict["colors"]
            self.fonts = jsonDict["fonts"]
            self.hover_colors = jsonDict["hover_colors"]

    def getColors(self):
        return self.colors

    def getHovercolors(self):
        return self.hover_colors

    def getFonts(self):
        return self.fonts


if __name__ == "__main__":
    a = GetGUIConfig(os.path.join("config", "gui.json"))
