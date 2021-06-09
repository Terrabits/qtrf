from PySide2.QtCore      import Signal
from qtrf.helpers        import float_or_none
from qtrf.numeric_suffix import prefix_map, to_str


# Use requires:
# - class be QWidget
# - methods: text() and setText(text)
class FloatValueMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.decimal_places = 3
        self.prefix_keys     = prefix_map.copy()
        self.units          = 'U'
        self._value         = None

    # value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        value = float_or_none(value)
        if self._value == value:
            # value is unchanged
            self._update_text()
            return

        # set
        self._value = value
        self._update_text()
        self.value_changed.emit(self.value)

    # signals
    value_changed = Signal(float)

    # helpers

    def _update_text(self):
        if self.value is None:
            self.clear()
            return

        _text = to_str(self.value, self.decimal_places, self.prefix_keys, self.units)
        self.setText(_text)
