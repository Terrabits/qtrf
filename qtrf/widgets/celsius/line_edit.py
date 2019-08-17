from qtrf.widgets.value.line_edit import ValueLineEdit

class CelsiusLineEdit(ValueLineEdit):
    def __init__(self, parent=None):
        ValueLineEdit.__init__(self, parent)
        self.decimal_places = 1
        self.prefix_map     = None
        self.units          = '°C'
        self.update_validation()
