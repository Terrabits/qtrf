from qtrf.widgets.ohms            import prefix_map, units
from qtrf.widgets.value.line_edit import ValueLineEdit

class OhmsLineEdit(ValueLineEdit):
    def __init__(self, parent=None):
        ValueLineEdit.__init__(self, parent)
        self.prefix_map       = prefix_map
        self.include_negative = False
        self.units            = units
        self.update_validation()
