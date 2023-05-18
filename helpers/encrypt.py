import bcrypt


def encryptPassword(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def comparePassword(password: str, stored_password: str):
    return bcrypt.checkpw(password.encode(), stored_password)
