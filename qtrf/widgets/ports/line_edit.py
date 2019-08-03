from PySide2.QtWidgets import QLineEdit
from .mixin.focus     import FocusMixin
from .mixin.list      import ListMixin
from .mixin.validator import ValidatorMixin

class PortsLineEdit(ValidatorMixin, FocusMixin, ListMixin, QLineEdit):
    def __init__(self, parent=None):
        QLineEdit     .__init__(self, parent)
        ListMixin     .__init__(self)
        FocusMixin    .__init__(self)
        ValidatorMixin.__init__(self)
