import string
from datetime import datetime


def validateNoEmptyEntrys(group, worker_data):
    if worker_data == None:
        raise Exception("Data dictorinary Not Provided")

    for key in group:
        if len(worker_data[key].strip()) == 0:
            return False

    return True


def validateInteger(data):
    for character in data:
        if character in string.ascii_letters or character in string.punctuation:
            return False

    return True


def validateLen(desired_len, data):
    if len(data) < desired_len:
        return False

    return True


def validateUniqueCharacter(data):
    if len(data) != 1:
        return False

    return True


def validateNotSpecialCharacters(data):
    for character in data:
        if character in string.punctuation:
            return False

    return True


def validateNotNumbers(data):
    for character in data:
        if character in string.digits:
            return False

    return True


def validateDateFormat(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return False

    return True
