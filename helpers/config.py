import json
import os


class GetGUIConfig:
    def __init__(self, path) -> None:
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


class GetBankConfig:
    def __init__(self, path) -> None:
        self.json_path = path

    def getBankValueByCode(self, code: str):
        with open(self.json_path, "r") as file:
            jsonDict = json.loads(file.read())

            return jsonDict["banks"][code]


if __name__ == "__main__":
    print(GetBankConfig("./config/bank.json").getBankValueByCode("0102"))
