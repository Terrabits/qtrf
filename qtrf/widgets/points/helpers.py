from PySide6.QtCore import QRegularExpression
from PySide6.QtGui  import QRegularExpressionValidator


POINTS_REGEX = r'[1-9]\d*'


def points_validator():
    return QRegularExpressionValidator(QRegularExpression(POINTS_REGEX))
