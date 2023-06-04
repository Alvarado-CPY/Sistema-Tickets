import bcrypt


def encryptPassword(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def comparePassword(password, stored_password):
    return bcrypt.checkpw(password.encode(), stored_password)
