import string
from datetime import datetime

def validateNoEmptyEntrys(group: tuple[str], worker_data: dict = None) -> bool:
    if worker_data == None:
        raise Exception("Data dictorinary Not Provided")

    for key in group:
        if len(worker_data[key].strip()) == 0:
            return False

    return True

def validateInteger(data: str | int) -> bool:
    try:
        int(data)
        return True
    except ValueError:
        return False

def validateLen(desired_len: int, data: str) -> bool:
    if len(data) < desired_len:
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