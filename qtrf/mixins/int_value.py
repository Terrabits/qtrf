from PySide2.QtCore      import Signal
from qtrf.helpers        import int_or_none


class IntValueMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = None

    # value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        value = int_or_none(value)
        if self._value == value:
            # value is unchanged
            self._update_text()
            return

        # set
        self._value = value
        self._update_text()
        self.value_changed.emit(self.value)

    # signals
    value_changed = Signal(int)

    # helpers

    def _update_text(self):
        if self.value is None:
            self.clear()
        else:
            self.setText(str(self.value))
