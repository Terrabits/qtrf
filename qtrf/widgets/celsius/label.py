from qtrf.widgets.float_value.label import FloatValueLabel


class CelsiusLabel(FloatValueLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys    = {}
        self.units          = '°C'
        self.decimal_places = 1
