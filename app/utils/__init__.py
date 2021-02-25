def is_none(value) -> bool:
    return value is None


def is_empty(value) -> bool:
    return len(value.split()) == 0


def is_empty_or_none(value) -> bool:
    return is_none(value) or is_empty(value)
