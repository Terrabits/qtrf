from PySide2.QtCore    import Signal
from qtrf.units        import prefix_map, to_decimal, to_str


# Use requires:
# - class be QWidget
# - methods: text() and setText(text)
class ValueMixin(object):
    def __init__(self):
        self.decimal_places = 3
        self.prefix_map     = prefix_map.copy()
        self.units          = 'U'

    # value
    @property
    def value(self):
        return to_decimal(self.text(), self.units)

    @value.setter
    def value(self, value):
        if self.value == value:
            return
        if value == None or value == '':
            self.clear()
        else:
            self.setText(self._to_str(value))
        self.value_changed.emit(self.value)

    # signals
    value_changed = Signal(float)

    # helper
    def _to_str(self, value):
        return to_str(value, self.decimal_places, self.prefix_map, self.units)
