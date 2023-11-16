from .regex         import ports_list_regex
from qtrf.QtCore import QRegularExpression
from qtrf.QtGui  import QRegularExpressionValidator


def validator():
    return QRegularExpressionValidator(QRegularExpression(ports_list_regex))
