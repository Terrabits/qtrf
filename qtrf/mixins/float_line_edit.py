from .float_value        import FloatValueMixin
from .helpers            import float_validator
from .prefix_keys        import PrefixKeysMixin
from .special_keys       import SpecialKeysMixin
from PySide2.QtCore      import Slot
from qtrf.numeric_suffix import to_decimal


class FloatLineEditMixin(SpecialKeysMixin, PrefixKeysMixin, FloatValueMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_negative = True
        self.update_validator()
        self.connect_qt_signals_and_slots()

    @Slot()
    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.selectAll()

    @Slot()
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.enter_value()
        self.deselect()

    @Slot()
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()

    def connect_qt_signals_and_slots(self):
        self.special_key_pressed.connect(self.enter_value)
        self.prefix_key_pressed.connect(self.enter_value_with_prefix)


    # helpers

    def enter_value(self):
        self.value = to_decimal(self.text(), self.units, self.prefix_keys)
        self.selectAll()

    def enter_value_with_prefix(self, prefix):
        # base
        base_value = to_decimal(self.text(), self.units)
        if base_value is None:
            # clear value
            self.value = None
            return

        # get prefix value
        prefix = chr(prefix)
        if not prefix in self.prefix_keys:
            prefix = prefix.lower()
        prefix_value = self.prefix_keys[prefix]

        # set
        self.value = base_value * prefix_value
        self.selectAll()

    def update_validator(self):
        _validator = float_validator(self.prefix_keys, self.units, self.include_negative)
        self.setValidator(_validator)
