from qtrf.shake     import AnimationsList, shake
from PySide2.QtCore import Slot


# Use requires:
# - class be top-most parent QWidget
# (e.g. window or mainwindow)
class ShakeMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # keep animations out of
        # python garbage collection
        self.animations = AnimationsList()

    Slot()
    def shake(self):
        animation = shake(self)
        self.animations.add(animation)
