from PySide2.QtWidgets     import QLineEdit
from qtrf.mixins.line_edit import LineEditMixin
from qtrf.mixins.value     import ValueMixin

class ValueLineEdit(LineEditMixin, ValueMixin, QLineEdit):
    def __init__(self, parent=None):
        QLineEdit    .__init__(self, parent)
        ValueMixin   .__init__(self)
        LineEditMixin.__init__(self)
