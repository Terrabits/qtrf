from qtrf.widgets.value.line_edit import ValueLineEdit

class dBmLineEdit(ValueLineEdit):
    def __init__(self, parent=None):
        ValueLineEdit.__init__(self, parent)
        self.prefix_map = None
        self.units      = 'dBm'
        self.update_validation()
