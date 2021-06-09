from qtrf.widgets.float_value.label import FloatValueLabel


class CelsiusLabel(FloatValueLabel):
    def __init__(self, parent=None):
        FloatValueLabel.__init__(self, parent)
        self.decimal_places = 1
        self.prefix_keys     = None
        self.units          = '°C'
