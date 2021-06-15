from .mixins           import PortsListMixin, ValidatorMixin
from .mixins.ports     import to_list
from PySide2.QtCore    import Slot
from PySide2.QtWidgets import QLineEdit
from qtrf.mixins       import SpecialKeysMixin


class PortsLineEdit(SpecialKeysMixin, ValidatorMixin, PortsListMixin, QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.special_key_pressed.connect(self.enter_value)

    @Slot()
    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.selectAll()

    @Slot()
    def focusOutEvent(self, event):
        event.accept()
        self.enter_value()
        self.deselect()

    @Slot()
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()


    # helpers

    def enter_value(self):
        self.list = to_list(self.text())
