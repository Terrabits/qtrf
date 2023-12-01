from qtrf.numeric_suffix import prefix_map
from qtrf.QtCore         import Signal, Slot, Qt
from qtrf.QtGui          import QKeyEvent


# constants
ALPHABET_KEYS = [Qt.Key(i) for i in range(int(Qt.Key_A), int(Qt.Key_Z) + 1)]


class PrefixKeysMixin:


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix_keys = prefix_map.copy()


    prefix_key_pressed = Signal(str)


    @Slot(QKeyEvent)
    def keyPressEvent(self, event):

        # key is not a letter?
        key = Qt.Key(event.key())
        if key not in ALPHABET_KEYS:
            # not a letter; let next class handle event
            super().keyPressEvent(event)
            return


        # is prefix?
        is_shift  = bool(event.modifiers() & Qt.KeyboardModifiers.ShiftModifier)
        character = chr(event.key())
        character = character.upper() if is_shift else character.lower()
        if character in self.prefix_keys:
            event.accept()
            self.prefix_key_pressed.emit(character)
            return

        # toggle case; is prefix now?
        character = character.lower() if is_shift else character.upper()
        if character in self.prefix_keys:
            event.accept()
            self.prefix_key_pressed.emit(character)
            return

        # handle in next class?
        super().keyPressEvent(event)
