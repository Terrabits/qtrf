from   ddt                      import ddt, data
from   qtrf.widgets.ports.ports import entry_to_list, is_valid_regex, list_to_entry
import re
import unittest

@ddt
class TestUnits(unittest.TestCase):
    @data({'entry': '',           'list': []},
          {'entry': '1',          'list': [1]},
          {'entry': '1,2',        'list': [1,2]},
          {'entry': '1, 2, 3, 4', 'list': [1,2,3,4]},
          {'entry': '1-4',        'list': [1,2,3,4]},
          {'entry': '1, 3, 1-4',  'list': [1,2,3,4]})
    def test_entry_to_list(self, data):
        entry = data['entry']
        list  = data['list' ]
        self.assertEqual(entry_to_list(entry), list)

    @data({'list': [],                'entry': ''    },
          {'list': [1],               'entry': '1'   },
          {'list': [1,2],             'entry': '1-2' },
          {'list': [1,3],             'entry': '1, 3'},
          {'list': [1,4,9,10,11],     'entry': '1, 4, 9-11'},
          {'list': [1,2,3,4,9,10,11], 'entry': '1-4, 9-11' })
    def test_list_to_entry(self, data):
        list  = data['list']
        entry = data['entry']
        self.assertEqual(list_to_entry(list), entry)
    @data({'entry': '',           'is_valid': False},
          {'entry': '1',          'is_valid': True},
          {'entry': '1,2',        'is_valid': True},
          {'entry': '1, 2',       'is_valid': True},
          {'entry': '1-4',        'is_valid': True},
          {'entry': '1-2,3, 4-5', 'is_valid': True})
    def test_is_valid_regex(self, data):
        entry    = data['entry']
        is_valid = data['is_valid']
        self.assertEqual(bool(re.match(is_valid_regex, entry)), is_valid)
