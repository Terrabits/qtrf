from qtrf.widgets.value.line_edit import ValueLineEdit
from qtrf.widgets.volts           import prefix_map, units

class VoltsLineEdit(ValueLineEdit):
    def __init__(self, parent=None):
        ValueLineEdit.__init__(self, parent)
        self.prefix_map = prefix_map
        self.units      = units
        self.update_validation()
