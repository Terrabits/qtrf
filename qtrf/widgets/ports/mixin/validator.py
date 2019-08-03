from ..ports        import is_valid_regex
from PySide2.QtCore  import QRegExp
from PySide2.QtGui   import QRegExpValidator

def clean_intermediate_input(text):
    return text.strip().rstrip(',').rstrip('-')
def create_validator():
    return QRegExpValidator(QRegExp(is_valid_regex))

class ValidatorMixin(object):
    def __init__(self):
        self.update_validation()
    def update_validation(self):
        self.setValidator(create_validator())
    def clean_intermediate_input(self):
        self.setText(clean_intermediate_input(self.text()))
        self.list = self.list
