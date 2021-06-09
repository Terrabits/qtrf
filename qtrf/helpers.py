def type_or_none(Type, value):
    if value is None or value == '':
        return None
    # else
    return Type(value)


def float_or_none(value):
    return type_or_none(float, value)


def int_or_none(value):
    return type_or_none(int, value)
