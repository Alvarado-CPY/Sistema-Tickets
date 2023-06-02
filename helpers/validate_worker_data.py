def validateNoEmptyEntrys(worker_data: dict, group: tuple[str]):
    for key in group:
        if len(worker_data[key].strip()) == 0:
            return False

    return True
