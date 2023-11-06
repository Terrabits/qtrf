from PySide6.QtWidgets import QLineEdit
from qtrf.mixins       import IntLineEditMixin


class IntValueLineEdit(IntLineEditMixin, QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
