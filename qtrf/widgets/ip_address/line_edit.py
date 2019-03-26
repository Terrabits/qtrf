
from PySide2.QtCore    import QRegExp
from PySide2.QtGui     import QRegExpValidator
from PySide2.QtWidgets import QLineEdit

from_zero = r'(((00)?\d)|([01]?\d\d)|(2[0-4]\d)|(25[0-5]))'
from_one  = r'(((0|00)?[1-9])|(0?[1-9]\d)|(1\d\d)|(2[0-4]\d)|(25[0-5]))'
dot       = r'\.'
regex_str = '{from_one}{dot}{from_zero}{dot}{from_zero}{dot}{from_one}'.format(from_zero=from_zero, from_one=from_one, dot=dot)

class IPAddressLineEdit(QLineEdit):
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        validator = QRegExpValidator(QRegExp(regex_str))
        self.setValidator(validator)
    def focusInEvent(self, event):
        self.selectAll()
