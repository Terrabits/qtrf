from .ui_filewidget             import Ui_FileWidget
from pathlib                    import Path
from PySide2.QtCore             import Slot
from PySide2.QtWidgets          import QFileDialog, QWidget

class FileWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_FileWidget()
        self.ui.setupUi(self)
        self.caption   = 'Open...'
        self.filter    = ''
        self._filename = None

    @property
    def filename(self):
        return self._filename
    @filename.setter
    def filename(self, value):
        self._filename = value
        self.update_filename()

    def _dir(self):
        if self.filename:
            return str(Path(self.filename).parent)
        else:
            return ''

    @Slot()
    def on_open_clicked(self):
        filename, filter = QFileDialog.getOpenFileName(self.window(), self.caption, self._dir(), self.filter)
        if filename:
            self.filename = filename
    @Slot()
    def on_clear_clicked(self):
        self.filename = None

    def update_filename(self):
        if self._filename:
            self.ui.filename.setText(Path(self._filename).name)
        else:
            self.ui.filename.clear()
