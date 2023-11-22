from qtrf.QtWidgets import QLabel
from qtrf.mixins    import FloatValueMixin


class FloatValueLabel(QLabel, FloatValueMixin):

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        FloatValueMixin.__init__(self)
