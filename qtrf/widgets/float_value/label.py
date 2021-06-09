from PySide2.QtWidgets       import QLabel
from qtrf.mixins.float_value import FloatValueMixin


class FloatValueLabel(FloatValueMixin, QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
