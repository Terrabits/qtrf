from PySide2.QtWidgets import QLabel
from qtrf.mixins       import IntValueMixin


class IntValueLabel(IntValueMixin, QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
