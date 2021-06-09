from PySide2.QtCore    import Signal, Slot, Qt


SPECIAL_KEYS = [Qt.Key_Space, Qt.Key_Enter, Qt.Key_Return]


class SpecialKeysMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.special_keys = SPECIAL_KEYS

    special_key_pressed = Signal(int)

    # helpers

    @Slot()
    def keyPressEvent(self, event):
        key = event.key()
        if key in self.special_keys:
            event.accept()
            self.special_key_pressed.emit(key)
        else:
            super().keyPressEvent(event)
