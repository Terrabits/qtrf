from PySide2.QtCore    import QRegExp
from PySide2.QtGui     import QRegExpValidator
from PySide2.QtWidgets import QLineEdit


# regex
POINTS_REGEX = r'[1-9]\d*'


def int_or_none(value):
    if value is None:
        return None
    if value == '':
        return None

    return int(value)


class PointsLineEdit(QLineEdit):
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        self._set_validator()

    @property
    def value(self):
        if not self.text():
            return None

        return int(self.text())

    @value.setter
    def value(self, value):
        if value == self.value:
            # nothing to do
            return

        # set
        value = int_or_none(value)
        if value is None:
            self.clear()
        else:
            self.setText(str(value))

    def focusInEvent(self, event):
        QLineEdit.focusInEvent(self, event)
        self.selectAll()

    def mousePressEvent(self, event):
        QLineEdit.mousePressEvent(event)
        self.selectAll()

    # helpers
    def _set_validator(self):
        validator = QRegExpValidator(QRegExp(POINTS_REGEX))
        self.setValidator(validator)
