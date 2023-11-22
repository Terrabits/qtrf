from qtrf.QtWidgets import QLabel
from qtrf.mixins    import IntValueMixin


class IntValueLabel(QLabel, IntValueMixin):

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        IntValueMixin.__init__(self)
