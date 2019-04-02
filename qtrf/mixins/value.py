from decimal           import Decimal
from qtrf.units        import prefix_map, to_decimal, to_str

# Requires text(), setText(text) methods
# to exist in inheriting class
class ValueMixin(object):
    def __init__(self):
        self.decimal_places = 3
        self.prefix_map     = prefix_map.copy()
        self.units          = 'U'
    @property
    def value(self):
        return to_decimal(self.text(), self.units)
    @value.setter
    def value(self, value):
        if value == None or value == '':
            self.clear()
            return
        self.setText(self._to_str(value))
    def _to_str(self, value):
        return to_str(value, self.decimal_places, self.prefix_map, self.units)
