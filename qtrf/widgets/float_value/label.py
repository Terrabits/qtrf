from PySide6.QtWidgets import QLabel
from qtrf.mixins       import FloatValueMixin


class FloatValueLabel(FloatValueMixin, QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
