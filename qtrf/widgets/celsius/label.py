from qtrf.widgets.value.label import ValueLabel

class CelsiusLabel(ValueLabel):
    def __init__(self, parent=None):
        ValueLabel.__init__(self, parent)
        self.decimal_places = 1
        self.prefix_map     = None
        self.units          = '°C'
