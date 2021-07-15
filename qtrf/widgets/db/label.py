from qtrf.widgets.float_value.label import FloatValueLabel


class dBLabel(FloatValueLabel):
    def __init__(self, parent=None):
        FloatValueLabel.__init__(self, parent)
        self.prefix_keys = {}
        self.units       = 'dB'
