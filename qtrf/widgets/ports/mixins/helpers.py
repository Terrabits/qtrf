from .regex         import ports_list_regex
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui  import QRegularExpressionValidator


def validator():
    return QRegularExpressionValidator(QRegularExpression(ports_list_regex))
