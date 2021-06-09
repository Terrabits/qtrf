from .helpers                 import ip_address_validator
from PySide2.QtCore           import Slot
from PySide2.QtWidgets        import QLineEdit
from qtrf.mixins.special_keys import SpecialKeysMixin


class IPAddressLineEdit(SpecialKeysMixin, QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.update_validator()
        self.connect_qt_signals_and_slots()

    @Slot()
    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.selectAll()

    @Slot()
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()


    # helpers

    def connect_qt_signals_and_slots(self):
        self.special_key_pressed.connect(self.selectAll)

    def update_validator(self):
        self.setValidator(ip_address_validator())
