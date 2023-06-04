def formatDate(date):
    if date == None:
        return "None"
    return date.split()[0]

def formatAddMissingZero(bank_number):
    return f"0{bank_number}"