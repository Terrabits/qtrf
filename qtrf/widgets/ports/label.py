from .mixins        import PortsListMixin
from qtrf.QtWidgets import QLabel


class PortsLabel(QLabel, PortsListMixin):

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        PortsListMixin.__init__(self)
