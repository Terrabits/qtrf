from qtrf.widgets.amps            import prefix_map, units
from qtrf.widgets.value.line_edit import ValueLineEdit

class AmpsLineEdit(ValueLineEdit):
    def __init__(self, parent=None):
        ValueLineEdit.__init__(self, parent)
        self.prefix_map = prefix_map
        self.units      = units
        self.update_validation()
