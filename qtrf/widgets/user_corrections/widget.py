from qtrf.widgets.file import FileWidget

class UserCorrectionsWidget(FileWidget):
    def __init__(self, parent=None):
        FileWidget.__init__(self, parent)
        self.filter = 'User Corrections File (*.uco *.ucor)'
