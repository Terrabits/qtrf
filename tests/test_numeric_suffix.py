from   ddt                 import ddt, data
from   decimal             import Decimal
from   qtrf.numeric_suffix import prefix_map, to_decimal, to_str
import unittest


# frequency prefixes
frequency_prefix_map = prefix_map.copy()
del(frequency_prefix_map['f'])
del(frequency_prefix_map['p'])
del(frequency_prefix_map['n'])
del(frequency_prefix_map['m'])

# farads prefixes
farads_prefix_map = prefix_map.copy()
del(farads_prefix_map['K'])
del(farads_prefix_map['M'])
del(farads_prefix_map['G'])
del(farads_prefix_map['T'])


@ddt
class TestUnits(unittest.TestCase):
    @data({'text': None,     'units': '',  'value': None            },
          {'text': '',       'units': '',  'value': None            },
          {'text': 'm',      'units': '',  'value': None            },
          {'text': 'M',      'units': '',  'value': None            },
          {'text': '0.',     'units': 'U', 'value': Decimal('0')    },
          {'text': '1.',     'units': 'U', 'value': Decimal('1')    },
          {'text': '0',      'units': 'U', 'value': Decimal('0')    },
          {'text': '1',      'units': 'U', 'value': Decimal('1')    },
          {'text': '1.0',    'units': 'U', 'value': Decimal('1')    },
          {'text': '2.1 GU', 'units': 'U', 'value': Decimal('2.1e9')})
    def test_to_decimal_with_prefixes(self, data):
        text  = data['text' ]
        units = data['units']
        value = data['value']
        self.assertEqual(to_decimal(text, units, prefix_map), value)

    @data({'text': None,     'units': '',  'value': None            },
          {'text': '',       'units': '',  'value': None            },
          {'text': 'm',      'units': '',  'value': None            },
          {'text': 'M',      'units': '',  'value': None            },
          {'text': '0.',     'units': 'U', 'value': Decimal('0')    },
          {'text': '1.',     'units': 'U', 'value': Decimal('1')    },
          {'text': '0',      'units': 'U', 'value': Decimal('0')    },
          {'text': '1',      'units': 'U', 'value': Decimal('1')    },
          {'text': '1.0',    'units': 'U', 'value': Decimal('1')    },
          {'text': '2.1 U',  'units': 'U', 'value': Decimal('2.1')  })
    def test_to_decimal_no_prefixes(self, data):
        text  = data['text' ]
        units = data['units']
        value = data['value']
        self.assertEqual(to_decimal(text, units), value)

    @data({'value': Decimal('0'),       'decimals': 3, 'prefix_map': prefix_map,           'units': '',    'text': '0.000'      },
          {'value': Decimal('1'),       'decimals': 3, 'prefix_map': prefix_map,           'units': '',    'text': '1.000'      },
          {'value': Decimal('2'),       'decimals': 1, 'prefix_map': prefix_map,           'units': '',    'text': '2.0'        },
          {'value': Decimal('1.005e3'), 'decimals': 2, 'prefix_map': prefix_map,           'units': '',    'text': '1.01 K'     },
          {'value': Decimal('100.3e3'), 'decimals': 3, 'prefix_map': frequency_prefix_map, 'units': 'Hz',  'text': '100.300 KHz'},
          {'value': Decimal('3.01e-5'), 'decimals': 0, 'prefix_map': farads_prefix_map,    'units': 'F',   'text': '30 uF'      },
          {'value': Decimal('1234.56'), 'decimals': 1, 'prefix_map': None,                 'units': 'dBm', 'text': '1234.6 dBm' },
          {'value': Decimal('-1e-2'),   'decimals': 2, 'prefix_map': None,                 'units': 'dBm', 'text': '-0.01 dBm'  })
    def test_to_str(self, data):
        value      = data['value'     ]
        decimals   = data['decimals'  ]
        prefix_map = data['prefix_map']
        units      = data['units'     ]
        text       = data['text'      ]
        self.assertEqual(to_str(value, decimals, prefix_map, units), text)
