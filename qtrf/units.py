from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

prefix_map = {
    'f': Decimal('1e-15'),
    'p': Decimal('1e-12'),
    'n': Decimal('1e-9'),
    'u': Decimal('1e-6'),
    'm': Decimal('1e-3'),
    '' : Decimal('1'),
    'K': Decimal('1e3'),
    'M': Decimal('1e6'),
    'G': Decimal('1e9'),
    'T': Decimal('1e12')
}

# validate str
def regex_str(prefixes=list(prefix_map), units='U', include_negative=True):
    sign_regex  = r'\-?' if include_negative else ''
    value_regex = r'[0-9]+(\.[0-9]*)?'
    units_regex = units or ''
    if prefixes:
        prefixes_regex = '[{}]?'.format(''.join(prefixes))
    else:
        prefixes_regex = ''
    return '{}{} {}{}'.format(sign_regex, value_regex, prefixes_regex, units).strip()

# str => float if successful else None
def to_decimal(text, units='', ignore_prefix=False):
    # clean input
    try:
        text = text.strip().replace(' ', '')
    except AttributeError:
        return None
    if not text:
        return None
    # chop off units
    if units and text.endswith(units):
        unit_pos = -1*len(units)
        text = text[:unit_pos]
    # separate prefix
    prefix = ''
    if text[-1] in prefix_map:
        prefix = text[-1]
        text   = text[:-1]
    prefix = prefix if not ignore_prefix else ''
    try:
        return Decimal(text) * prefix_map[prefix]
    except InvalidOperation:
        return None

# number => str
def to_base_and_prefix(value, prefix_map=prefix_map):
    if not prefix_map:
        return value, ''
    value     = Decimal(value)
    abs_value = abs  (value)
    if abs_value == 0:
        if '' in prefix_map:
            return value, ''
        else:
            value, list(prefix_map)[-1]
    prefix = list(prefix_map)[-1]
    for i in prefix_map:
        if abs_value < prefix_map[i] * Decimal('1e3'):
            prefix = i
            break
    prefix_value = prefix_map[prefix]
    return value/prefix_value, prefix
def round_decimal_places(value, decimal_places=3):
    value = Decimal(value)
    if decimal_places >= 1:
        zeros  = '0' * (decimal_places-1)
        format = Decimal('.' + zeros + '1')
    else:
        format = Decimal('1.')
    return value.quantize(format, ROUND_HALF_UP)
def to_str(value, decimal_places=3, prefix_map=prefix_map, units='U'):
    base, prefix = to_base_and_prefix(value, prefix_map)
    base = round_decimal_places(base, decimal_places)
    return '{} {}{}'.format(base, prefix, units).strip()
