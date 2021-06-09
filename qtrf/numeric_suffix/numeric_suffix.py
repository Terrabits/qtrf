from .helpers import to_base_and_prefix, round_decimal_places
from decimal  import Decimal, InvalidOperation


# validate str
def regex_str(prefixes, units, include_negative):
    sign_regex  = r'\-?' if include_negative else ''
    value_regex = r'[0-9]+(\.[0-9]*)?'
    if prefixes:
        prefixes_str   = ''.join(prefixes)
        prefixes_regex = f'[{prefixes_str}]?'
    else:
        prefixes_regex = ''
    units_regex = units or ''
    return f'{sign_regex}{value_regex} {prefixes_regex}{units}'.strip()


# str => float if successful else None
def to_decimal(text, units, prefix_map=None):
    # clean input
    try:
        text = text.strip().replace(' ', '')
    except AttributeError:
        return None
    if not text:
        return None

    # chop off units
    if units and text.endswith(units):
        unit_pos = -1 * len(units)
        text     = text[:unit_pos]

    # separate prefix
    prefix = ''
    if prefix_map and text[-1] in prefix_map:
        prefix = text[-1]
        text   = text[:-1]

    # get decimal value
    try:
        _decimal = Decimal(text)
    except InvalidOperation:
        return None

    if not prefix:
        return _decimal

    prefix_value = prefix_map[prefix]
    return _decimal * prefix_value


# number => str
def to_str(value, decimal_places, prefix_map, units):
    base, prefix = to_base_and_prefix(value, prefix_map)
    base = round_decimal_places(base, decimal_places)
    return f'{base} {prefix}{units}'.strip()
