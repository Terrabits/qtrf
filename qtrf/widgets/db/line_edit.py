from qtrf.widgets.value.line_edit import ValueLineEdit

class dBLineEdit(ValueLineEdit):
    def __init__(self, parent=None):
        ValueLineEdit.__init__(self, parent)
        self.prefix_map = None
        self.units      = 'dB'
        self.update_validation()
