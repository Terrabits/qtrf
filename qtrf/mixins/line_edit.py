from PySide2.QtCore    import QRegExp, Qt
from PySide2.QtGui     import QRegExpValidator
from PySide2.QtWidgets import QLineEdit
from qtrf.units        import prefix_map, regex_str, to_decimal


class LineEditMixin(object):
    def __init__(self):
        self.include_negative = True
        self.prefix_map       = prefix_map.copy()
        self.units            = 'U'
        self._special_keys = [Qt.Key_Space, Qt.Key_Enter, Qt.Key_Return]
        self.update_validation()

    def _update_prefix_keys(self):
        if self.prefix_map:
            self._prefix_keys = [ord(i.upper()) for i in self.prefix_map if i]
        else:
            self._prefix_keys = []

    def _create_validator(self):
        _regex_str = regex_str(self.prefix_map, self.units, self.include_negative)
        return QRegExpValidator(QRegExp(_regex_str))

    def _update_validator(self):
        self.setValidator(self._create_validator())

    def update_validation(self):
        self._update_prefix_keys()
        self._update_validator()

    def _is_special_key(self, key):
        return key in self._special_keys

    def _is_prefix_key(self, key):
        return key in self._prefix_keys

    def _prefix_value_from_ord(self, key):
        if not self.prefix_map:
            return None
        try:
            upper_chr = chr(key)
            lower_chr = upper_chr.lower()
        except ValueError:
            return None
        if upper_chr in self.prefix_map:
            return self.prefix_map[upper_chr]
        if lower_chr in self.prefix_map:
            return self.prefix_map[lower_chr]
        return None

    def keyPressEvent(self, event):
        key = event.key()
        if not self._is_special_key(key) and not self._is_prefix_key(key):
            QLineEdit.keyPressEvent(self, event)
            return
        prefix_value = self._prefix_value_from_ord(key)
        base_value   = to_decimal(self.text(), self.units, ignore_prefix=True)
        if base_value == 0:
            self.value = base_value
        elif base_value:
            if prefix_value:
                self.value = base_value * prefix_value
            else:
                self.value = base_value
        self.selectAll()
        event.accept()

    def focusInEvent(self, event):
        QLineEdit.focusInEvent(self, event)
        self.selectAll()

    def focusOutEvent(self, event):
        self.value = self.value
        QLineEdit.focusOutEvent(self, event)

    def mousePressEvent(self, event):
        QLineEdit.mousePressEvent(self, event)
        self.selectAll()
