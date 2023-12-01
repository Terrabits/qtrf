from qtrf.widgets.file import FileWidget

class UserCorrectionsWidget(FileWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.filter = 'User Corrections File (*.uco *.ucor)'
