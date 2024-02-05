import re


def name_validator(name, message):
    if isinstance(name, str) and re.match("^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)


def family_validator(family, message):
    if isinstance(family, str) and re.match("^[a-zA-Z\s]{3,30}$", family):
        return family
    else:
        raise ValueError(message)


def username_validator(username, message):
    if isinstance(username, str) and re.match("^[a-zA-Z]{3,30}$", username):
        return username
    else:
        raise ValueError(message)


def password_validator(password, message):
    if isinstance(password, str) and re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$",
                                              password):
        return password
    else:
        raise ValueError(message)


def date_validator(date, message):
    if isinstance(date, str) and re.match("^([1][0-9][0-9][0-9])\.[0-1][0-9]\.(([0-2][0-9])|(30))$", date):
        return date
    else:
        raise ValueError(message)


def time_validator(time, message):
    if isinstance(time, str) and re.match("^([01]\d|2[0-3]):([0-5]\d)$", time):
        return time
    else:
        raise ValueError(message)


def phone_validator(phone, message):
    if re.match("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone):
        return phone
    else:
        raise ValueError(message)