from qtrf.QtCore import Signal, Slot, Qt
from qtrf.QtGui  import QKeyEvent


# constants
SPECIAL_KEYS = [Qt.Key_Space, Qt.Key_Enter, Qt.Key_Return]


class SpecialKeysMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.special_keys = SPECIAL_KEYS


    special_key_pressed = Signal(int)


    # helpers

    @Slot(QKeyEvent)
    def keyPressEvent(self, event):

        # special key pressed?
        key = Qt.Key(event.key())
        if key in self.special_keys:
            event.accept()
            self.special_key_pressed.emit(event.key())
            return

        # call next class
        super().keyPressEvent(event)
