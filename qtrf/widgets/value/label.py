from PySide2.QtWidgets import QLabel
from qtrf.mixins.value import ValueMixin

class ValueLabel(ValueMixin, QLabel):
    def __init__(self, parent=None):
        QLabel    .__init__(self, parent)
        ValueMixin.__init__(self)
