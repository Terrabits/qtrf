from PySide2.QtCore import QRegExp
from PySide2.QtGui  import QRegExpValidator


POINTS_REGEX = r'[1-9]\d*'


def points_validator():
    return QRegExpValidator(QRegExp(POINTS_REGEX))
