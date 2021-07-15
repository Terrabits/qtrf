from decimal import Decimal


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
