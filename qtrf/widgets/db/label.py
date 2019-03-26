from qtrf.widgets.value.label import ValueLabel

class dBLabel(ValueLabel):
    def __init__(self, parent=None):
        ValueLabel.__init__(self, parent)
        self.prefix_map = None
        self.units      = 'dB'
