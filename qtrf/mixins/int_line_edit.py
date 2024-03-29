from .int_value    import IntValueMixin
from .helpers      import int_validator
from .special_keys import SpecialKeysMixin
from qtrf.QtCore   import Slot
from qtrf.QtGui    import QFocusEvent, QMouseEvent
from qtrf.helpers  import int_or_none


class IntLineEditMixin(SpecialKeysMixin, IntValueMixin):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_negative = True
        self.update_validator()
        self.connect_qt_signals_and_slots()


    @Slot(QFocusEvent)
    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.selectAll()


    @Slot(QFocusEvent)
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.enter_value()
        self.deselect()


    @Slot(QMouseEvent)
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()


    def connect_qt_signals_and_slots(self):
        self.special_key_pressed.connect(self.enter_value)


    # helpers

    def enter_value(self):
        self.value = int_or_none(self.text())
        self.selectAll()


    def update_validator(self):
        self.setValidator(int_validator(self.include_negative))
