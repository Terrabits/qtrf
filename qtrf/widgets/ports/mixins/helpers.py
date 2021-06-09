from .regex         import ports_list_regex
from PySide2.QtCore import QRegExp
from PySide2.QtGui  import QRegExpValidator


def validator():
    return QRegExpValidator(QRegExp(ports_list_regex))
