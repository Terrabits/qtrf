from PySide2.QtCore    import Qt
from PySide2.QtWidgets import QLineEdit

class FocusMixin(object):
    def __init__(self):
        self._special_keys = [Qt.Key_Enter, Qt.Key_Return]
    def keyPressEvent(self, event):
        key = event.key()
        if self._is_special_key(key):
            self.clean_intermediate_input()
            self.selectAll()
            event.accept()
        else:
            QLineEdit.keyPressEvent(self, event)
    def _is_special_key(self, key):
        return key in self._special_keys

    def focusInEvent(self, event):
        QLineEdit.focusInEvent(self, event)
        self.selectAll()
    def focusOutEvent(self, event):
        self.clean_intermediate_input()
        QLineEdit.focusOutEvent(self, event)
