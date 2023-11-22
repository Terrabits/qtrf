from qtrf.QtWidgets import QLineEdit
from qtrf.mixins    import IntLineEditMixin


class IntValueLineEdit(QLineEdit, IntLineEditMixin):

    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        IntLineEditMixin.__init__(self)
