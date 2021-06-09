from .mixins           import PortsListMixin
from PySide2.QtWidgets import QLabel


class PortsLabel(PortsListMixin, QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
