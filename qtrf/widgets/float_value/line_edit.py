from PySide2.QtWidgets           import QLineEdit
from qtrf.mixins.float_line_edit import FloatLineEditMixin


class FloatValueLineEdit(FloatLineEditMixin, QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
