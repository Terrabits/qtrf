from   ddt                             import ddt, data
import re
from   qtrf.widgets.ports.mixins.regex import ports_list_regex
from   qtrf.widgets.ports.mixins.ports import to_list, to_str
import unittest

@ddt
class TestUnits(unittest.TestCase):
    @data({'text': '',           'list': []},
          {'text': '1',          'list': [1]},
          {'text': '1,2',        'list': [1,2]},
          {'text': '1, 2, 3, 4', 'list': [1,2,3,4]},
          {'text': '1-4',        'list': [1,2,3,4]},
          {'text': '1, 3, 1-4',  'list': [1,2,3,4]})
    def test_to_list(self, data):
        text = data['text']
        list = data['list']
        self.assertEqual(to_list(text), list)

    @data({'list': [],                'text': ''    },
          {'list': [1],               'text': '1'   },
          {'list': [1,2],             'text': '1-2' },
          {'list': [1,3],             'text': '1, 3'},
          {'list': [1,4,9,10,11],     'text': '1, 4, 9-11'},
          {'list': [1,2,3,4,9,10,11], 'text': '1-4, 9-11' })
    def test_to_str(self, data):
        list = data['list']
        text = data['text']
        self.assertEqual(to_str(list), text)

    @data({'text': '',           'valid': False},
          {'text': '1',          'valid': True},
          {'text': '1,2',        'valid': True},
          {'text': '1, 2',       'valid': True},
          {'text': '1-4',        'valid': True},
          {'text': '1-2,3, 4-5', 'valid': True})
    def test_port_list_regex(self, data):
        text   = data['text']
        valid  = data['valid']
        _valid = bool(re.match(ports_list_regex, text))
        self.assertEqual(_valid, valid)
