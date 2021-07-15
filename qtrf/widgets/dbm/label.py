from qtrf.widgets.float_value.label import FloatValueLabel


class dBmLabel(FloatValueLabel):
    def __init__(self, parent=None):
        FloatValueLabel.__init__(self, parent)
        self.prefix_keys = {}
        self.units       = 'dBm'
