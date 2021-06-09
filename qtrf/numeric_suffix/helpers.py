from decimal import Decimal, InvalidOperation, ROUND_HALF_UP



def to_base_and_prefix(value, prefix_map):
    if not prefix_map:
        # no prefixes
        return value, ''

    # do not prefix zero
    if value == 0:
        return 0, ''

    value = Decimal(value)

    # get prefix
    prefix = list(prefix_map)[-1]
    for i in prefix_map:
        if abs(value) < prefix_map[i] * Decimal('1e3'):
            prefix = i
            break

    # calculate base value
    prefix_value = prefix_map[prefix]
    base_value   = value / prefix_value

    return base_value, prefix


def round_decimal_places(value, decimal_places):
    value = Decimal(value)
    if decimal_places >= 1:
        zeros  = '0' * (decimal_places-1)
        format = Decimal('.' + zeros + '1')
    else:
        format = Decimal('1.')
    return value.quantize(format, ROUND_HALF_UP)
