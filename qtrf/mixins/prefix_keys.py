from PySide2.QtCore      import Signal, Slot
from qtrf.numeric_suffix import prefix_map


class PrefixKeysMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix_keys = prefix_map.copy()

    prefix_key_pressed = Signal(int)

    # helpers

    @Slot()
    def keyPressEvent(self, event):
        key_value = event.key()
        try:
            character = chr(key_value)
        except ValueError:
            # not character
            super().keyPressEvent(event)
            return

        if character in self.prefix_keys:
            event.accept()
            self.prefix_key_pressed.emit(key_value)
        elif character.lower() in self.prefix_keys:
            event.accept()
            self.prefix_key_pressed.emit(key_value)
        else:
            # not prefix
            super().keyPressEvent(event)
