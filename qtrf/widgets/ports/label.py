from PySide2.QtWidgets import QLabel
from .mixin.list      import ListMixin

class PortsLabel(ListMixin, QLabel):
    def __init__(self, parent=None):
        QLabel   .__init__(self, parent)
        ListMixin.__init__(self)
