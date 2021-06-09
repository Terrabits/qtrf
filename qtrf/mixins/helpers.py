from PySide2.QtCore      import QRegExp
from PySide2.QtGui       import QRegExpValidator
from qtrf.numeric_suffix import regex_str


POSITIVE_INT_REGEX =   r'(0|[1-9]\d+)'
INT_REGEX          = r'-?(0|[1-9]\d+)'


def float_validator(prefix_map, units, include_negative):
    _regex = regex_str(prefix_map, units, include_negative)
    return QRegExpValidator(QRegExp(_regex))


def int_validator(include_negative):
    regex = INT_REGEX if include_negative else POSITIVE_INT_REGEX
    return QRegExpValidator(QRegExp(regex))
