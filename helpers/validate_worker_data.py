import string
from datetime import datetime
import json


def validateNoEmptyEntrys(group: tuple[str], worker_data: dict = None) -> bool:
    if worker_data == None:
        raise Exception("Data dictorinary Not Provided")

    for key in group:
        if len(worker_data[key].strip()) == 0:
            return False

    return True


def validateInteger(data: str) -> bool:
    for character in data:
        if character in string.ascii_letters or character in string.punctuation:
            return False

    return True


def validateLen(desired_len: int, data: str, limit=False) -> bool:
    if limit == False:
        if len(data) < desired_len:
            return False
    else:
        if len(data) < desired_len or len(data) > desired_len:
            return False

    return True


def validateUniqueCharacter(data: str) -> bool:
    if len(data) != 1:
        return False

    return True


def validateNotSpecialCharacters(data: str) -> bool:
    for character in data:
        if character in string.punctuation:
            return False

    return True


def validateNotNumbers(data: str) -> bool:
    for character in data:
        if character in string.digits:
            return False

    return True


def validateDateFormat(data: str) -> bool:
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return False

    return True


def validateBankCode(data: str, path: str) -> bool:
    bank_code_list: dict = {}
    with open(path, "r") as file:
        jsonDict = json.loads(file.read())
        bank_code_list = jsonDict["banks"]

        if data not in bank_code_list.keys():
            return False

    return True
