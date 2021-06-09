from PySide2.QtCore    import QRegExp
from PySide2.QtGui     import QRegExpValidator


# hostname regex
# https://stackoverflow.com/a/106223/1390788
hostname   = r'(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])'


# ip address regex
from_zero  = r'(((00)?\d)|([01]?\d\d)|(2[0-4]\d)|(25[0-5]))'
from_one   = r'(((0|00)?[1-9])|(0?[1-9]\d)|(1\d\d)|(2[0-4]\d)|(25[0-5]))'
dot        = r'\.'
ip_address = f'{from_one}{dot}{from_zero}{dot}{from_zero}{dot}{from_one}'


IP_ADDRESS_REGEX = f'(({ip_address})|({hostname}))'


def ip_address_validator():
    return QRegExpValidator(QRegExp(IP_ADDRESS_REGEX))
