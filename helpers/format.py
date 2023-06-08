def formatDate(date: str) -> str:
    if date == None:
        return "None"
    return date.split()[0]


def formatAddMissingZero(bank_number: int) -> str:
    return f"0{bank_number}"
