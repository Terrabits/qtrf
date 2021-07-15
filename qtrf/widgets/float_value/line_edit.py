from PySide2.QtWidgets import QLineEdit
from qtrf.mixins       import FloatLineEditMixin


class FloatValueLineEdit(FloatLineEditMixin, QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
