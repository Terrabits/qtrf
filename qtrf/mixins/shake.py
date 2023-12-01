from qtrf.shake  import AnimationsList, shake
from qtrf.QtCore import Slot


# Use requires:
# - class be top-most parent QWidget
# (e.g. window or mainwindow)
class ShakeMixin:


    def __init__(self, parent=None):
        super().__init__(parent)

        # keep animations out of python garbage collection
        self.animations = AnimationsList(parent)


    Slot()
    def shake(self):
        animation = shake(self)
        self.animations.add(animation)
