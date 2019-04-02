from qtrf.widgets.file import FileWidget

class TouchstoneWidget(FileWidget):
    def __init__(self, parent=None):
        FileWidget.__init__(self, parent)
        self.ports = '*'

    @property
    def ports(self):
        return self._ports
    @ports.setter
    def ports(self, value):
        self._ports  = value
        self.filter = 'Touchstone File (*.s{}p)'.format(self._ports)
