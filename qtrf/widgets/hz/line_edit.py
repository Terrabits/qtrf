from qtrf.widgets.hz              import prefix_map, units
from qtrf.widgets.value.line_edit import ValueLineEdit

class HzLineEdit(ValueLineEdit):
    def __init__(self, parent=None):
        ValueLineEdit.__init__(self, parent)
        self.prefix_map       = prefix_map
        self.include_negative = False
        self.units            = units
        self.update_validation()
