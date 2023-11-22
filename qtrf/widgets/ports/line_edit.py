from .mixins        import PortsListMixin, ValidatorMixin
from .mixins.ports  import to_list
from qtrf.QtCore    import Slot
from qtrf.QtWidgets import QLineEdit
from qtrf.mixins    import SpecialKeysMixin


class PortsLineEdit(QLineEdit, SpecialKeysMixin, ValidatorMixin, PortsListMixin):

    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        SpecialKeysMixin.__init__(self)
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
