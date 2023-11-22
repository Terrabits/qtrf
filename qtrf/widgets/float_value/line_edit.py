from qtrf.QtWidgets import QLineEdit
from qtrf.mixins    import FloatLineEditMixin


class FloatValueLineEdit(QLineEdit, FloatLineEditMixin):

    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        FloatLineEditMixin.__init__(self)
